import pandas as pd
import numpy as np
import torch
from nltk.tokenize import word_tokenize
import gensim.downloader as api

# Wczytanie X i Y do Train oraz X do Dev i Test
X_train = pd.read_table('train/in.tsv', sep='\t', error_bad_lines=False, quoting=3, header=None, names=['content', 'id'], usecols=['content'])
y_train = pd.read_table('train/expected.tsv', sep='\t', error_bad_lines=False, quoting=3, header=None, names=['label'])
X_dev = pd.read_table('dev-0/in.tsv', sep='\t', error_bad_lines=False, header=None, quoting=3, names=['content', 'id'], usecols=['content'])
X_test = pd.read_table('test-A/in.tsv', sep='\t', error_bad_lines=False, header=None, quoting=3, names=['content', 'id'], usecols=['content'])

# lowercase-ing zbiorów
# https://www.datacamp.com/community/tutorials/case-conversion-python
X_train = X_train.content.str.lower()
X_dev = X_dev.content.str.lower()
X_test = X_test.content.str.lower()

y_train = y_train['label'] #Df do Series?

# tokenizacja zbiorów
#https://www.nltk.org/_modules/nltk/tokenize.html
X_train = [word_tokenize(doc) for doc in X_train]
X_dev = [word_tokenize(doc) for doc in X_dev]
X_test = [word_tokenize(doc) for doc in X_test]

# word2vec zgodnie z poradą Pana Jakuba
# https://radimrehurek.com/gensim/auto_examples/howtos/run_downloader_api.html
# https://www.kaggle.com/kstathou/word-embeddings-logistic-regression
w2v = api.load('word2vec-google-news-300')

def document_vector(doc):
    """Create document vectors by averaging word vectors. Remove out-of-vocabulary words."""
    return np.mean([w2v[w] for w in doc if w in w2v] or [np.zeros(300)], axis=0)

X_train = [document_vector(doc) for doc in X_train]
X_dev = [document_vector(doc) for doc in X_dev]
X_test = [document_vector(doc) for doc in X_test]


#Sieć neuronowa z ćwiczeń 8
#https://git.wmi.amu.edu.pl/filipg/aitech-eks-pub/src/branch/master/cw/08_regresja_logistyczna.ipynb
class NeuralNetwork(torch.nn.Module): 
    def __init__(self, hidden_size):
        super(NeuralNetwork, self).__init__()
        self.l1 = torch.nn.Linear(300, hidden_size) #Korzystamy z word2vec-google-news-300 który ma zawsze na wejściu wymiar 300
        self.l2 = torch.nn.Linear(hidden_size, 1)

    def forward(self, x):
        x = self.l1(x)
        x = torch.relu(x)
        x = self.l2(x)
        x = torch.sigmoid(x)
        return x

model = NeuralNetwork(600)
criterion = torch.nn.BCELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.1)
batch_size = 15

# Trening modelu z ćwiczeń 8
#https://git.wmi.amu.edu.pl/filipg/aitech-eks-pub/src/branch/master/cw/08_regresja_logistyczna.ipynb
for epoch in range(5):
    model.train()
    for i in range(0, y_train.shape[0], batch_size):
        X = X_train[i:i+batch_size]
        X = torch.tensor(X)
        y = y_train[i:i+batch_size]
        y = torch.tensor(y.astype(np.float32).to_numpy()).reshape(-1,1)

        outputs = model(X.float())
        loss = criterion(outputs, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

y_dev = []
y_test = []

#Predykcje
#model.eval() will notify all your layers that you are in eval mode
model.eval()

#torch.no_grad() impacts the autograd engine and deactivate it. It will reduce memory usage and speed up
with torch.no_grad():
    for i in range(0, len(X_dev), batch_size):
        X = X_dev[i:i+batch_size]
        X = torch.tensor(X)
        outputs = model(X.float())
        
        y = (outputs > 0.5)
        y_dev.extend(y)

    for i in range(0, len(X_test), batch_size):
        X = X_test[i:i+batch_size]
        X = torch.tensor(X)
        outputs = model(X.float())

        y = (outputs > 0.5)
        y_test.extend(y)


#Wygenerowanie plików outputowych
y_dev = np.asarray(y_dev, dtype=np.int32)
y_test = np.asarray(y_test, dtype=np.int32)

y_dev_df = pd.DataFrame({'label':y_dev})
y_test_df = pd.DataFrame({'label':y_test})

y_dev_df.to_csv(r'dev-0/out.tsv', sep='\t', index=False,  header=False)
y_test_df.to_csv(r'test-A/out.tsv', sep='\t', index=False,  header=False)