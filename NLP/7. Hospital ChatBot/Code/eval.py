import pandas as pd
from tabulate import tabulate
from flair.data import Sentence, Token
from flair.datasets import SentenceDataset
from flair.models import SequenceTagger

def conllu2flair(sentences, label=None):
    fsentences = []
    for sentence in sentences:
        fsentence = Sentence()
        for token in sentence:
            ftoken = Token(token['form'])
            if label:
                ftoken.add_tag(label, token[label])
            fsentence.add_token(ftoken)
        fsentences.append(fsentence)
    return SentenceDataset(fsentences)

def predict(frame_model, sentence):
    csentence = [{'form': word} for word in sentence]
    fsentence = conllu2flair([csentence])[0]
    frame_model.predict(fsentence)
    possible_intents = {}
    for token in fsentence:
        for intent in token.annotation_layers["frame"]:
            if(intent.value in possible_intents):
                possible_intents[intent.value] += intent.score
            else:
                possible_intents[intent.value] = intent.score
    return max(possible_intents)

frame_model = SequenceTagger.load('frame-model/final-model.pt')
data = []
with open('data.tsv') as f:
    lines = f.readlines()

for line in lines[1:]:
    data.append((line.split("\t")[0], line.split("\t")[1]))

correct = 0
for sentence in data:
    predicted_intent = predict(frame_model, sentence[0].split())
    if predicted_intent == sentence[1].replace('\n',''):
        correct+=1
    else:
        print(predicted_intent + " != " + sentence[1].replace('\n',''))

print(f"{correct/len(data)} {correct}/{len(data)}")