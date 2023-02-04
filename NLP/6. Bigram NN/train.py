from collections import Counter
from nltk import bigrams, word_tokenize
from utils import read_csv, ENCODING, clean_text

DEFAULT_PREDICTION = "the:0.2 be:0.2 to:0.2 of:0.1 and:0.1 a:0.1 :0.1"

def train_model(data, model,vocab,alpha):
    for _, row in data.iterrows():
        words = word_tokenize(clean_text(row["607"]))
        for w1, w2 in bigrams(words, pad_left=True, pad_right=True):
            if w1 and w2:
                model[w2][w1] += 1
                vocab.add(w2)
                vocab.add(w1)

    for w2 in model:
        total_count = float(sum(model[w2].values()))
        denominator = total_count + alpha * len(vocab)
        for w1 in model[w2]:
            nominator = model[w2][w1] + alpha
            model[w2][w1] = nominator / denominator


def predict_data(read_path, save_path, model):
    data = read_csv(read_path)

    with open(save_path, "w", encoding=ENCODING) as f:
        for _, row in data.iterrows():
            words = word_tokenize(clean_text(row[7]))
            if len(words) < 3:
                prediction = DEFAULT_PREDICTION
            else:
                prediction = predict(words[0], model)
            f.write(prediction + "\n")


def predict(word, model):
    predictions = dict(model[word])
    most_common = dict(Counter(predictions).most_common(6))

    total_prob = 0.0
    str_prediction = ""

    for word, prob in most_common.items():
        total_prob += prob
        str_prediction += f"{word}:{prob} "

    if total_prob == 0.0:
        return DEFAULT_PREDICTION

    rem_prob = 1 - total_prob
    if rem_prob < 0.01:
        rem_prob = 0.01

    str_prediction += f":{rem_prob}"

    return str_prediction