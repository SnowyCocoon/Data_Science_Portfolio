import torch
import csv
torch.cuda.empty_cache()
from torch.utils.data import DataLoader
import pandas as pd
from os.path import exists

from utils import read_csv, clean_text, get_words_from_line
from nn import Bigrams, Model

data = read_csv("train/in.tsv.xz")
train_words = read_csv("train/expected.tsv")

train_data = data[[6, 7]]
train_data = pd.concat([train_data, train_words], axis=1)
train_data = train_data[6] + train_data[0] + train_data[7]
train_data = train_data.apply(clean_text)

vocab_size = 30000
embed_size = 150

train_dataset = Bigrams(train_data, vocab_size)

##################################################################################

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = Model(vocab_size, embed_size).to(device)
print(device)
if(not exists('model1.bin')):
    data = DataLoader(train_dataset, batch_size=8000)
    optimizer = torch.optim.Adam(model.parameters())
    criterion = torch.nn.NLLLoss()

    model.train()
    step = 0
    for i in range(2):
      print(f"EPOCH {i}=========================")
      for x, y in data:
          x = x.to(device)
          y = y.to(device)
          optimizer.zero_grad()
          ypredicted = model(x)
          loss = criterion(torch.log(ypredicted), y)
          if step % 100 == 0:
              print(step, loss)
          step += 1
          loss.backward()
          optimizer.step()

    torch.save(model.state_dict(), 'model1.bin')
else:
    print("Loading model1")
    model.load_state_dict(torch.load('model1.bin'))

###################################################################

vocab = train_dataset.vocab

def predict(tokens):
    ixs = torch.tensor(vocab.forward(tokens)).to(device)
    out = model(ixs)
    top = torch.topk(out[0], 8)
    top_indices = top.indices.tolist()
    top_probs = top.values.tolist()
    top_words = vocab.lookup_tokens(top_indices)
    result = ""
    for word, prob in list(zip(top_words, top_probs)):
                result += f"{word}:{prob} "
    # result  += f':0.01'
    return result

DEFAULT_PREDICTION = "a:0.2 the:0.2 to:0.2 of:0.1 and:0.1 of:0.1 :0.1"

def predict_file(result_path, data):
    with open(result_path, "w+", encoding="UTF-8") as f:
        for row in data:
            result = {}
            before = None
            for before in get_words_from_line(clean_text(str(row)), False):
              pass
            before = [before]
            print(before)
            if(len(before) < 1):
                result = DEFAULT_PREDICTION
            else:
                result = predict(before)
            result = result.strip()
            f.write(result + "\n")
            print(result)

dev_data = pd.read_csv("dev-0/in.tsv.xz", sep='\t', header=None, quoting=csv.QUOTE_NONE)[6]
dev_data = dev_data.apply(clean_text)
predict_file("dev-0/out.tsv", dev_data)

test_data = pd.read_csv("test-A/in.tsv.xz", sep='\t', header=None, quoting=csv.QUOTE_NONE)[6]
test_data = test_data.apply(clean_text)
predict_file("test-A/out.tsv", test_data)