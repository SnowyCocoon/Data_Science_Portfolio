from conllu import parse_incr
from tabulate import tabulate
from flair.data import Corpus, Sentence, Token
from flair.datasets import SentenceDataset
from flair.embeddings import StackedEmbeddings
from flair.embeddings import WordEmbeddings
from flair.embeddings import CharacterEmbeddings
from flair.embeddings import FlairEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer

def nolabel2o(line, i):
    return 'O' if line[i] == 'NoLabel' else line[i]

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

fields = ['id', 'form', 'frame', 'slot']

with open('Janet.conllu', encoding='utf-8') as trainfile:
    slot_trainset = list(parse_incr(trainfile, fields=fields, field_parsers={'slot': nolabel2o}))
with open('Janet.conllu', encoding='utf-8') as trainfile:
    frame_trainset = list(parse_incr(trainfile, fields=fields, field_parsers={'frame': nolabel2o}))

tabulate(slot_trainset[0], tablefmt='html')


slot_corpus = Corpus(train=conllu2flair(slot_trainset, 'slot'), test=conllu2flair(slot_trainset, 'slot'))
frame_corpus = Corpus(train=conllu2flair(frame_trainset, 'frame'), test=conllu2flair(frame_trainset, 'frame'))

slot_tag_dictionary = slot_corpus.make_tag_dictionary(tag_type='slot')
frame_tag_dictionary = frame_corpus.make_tag_dictionary(tag_type='frame')

print(slot_tag_dictionary)
print(frame_tag_dictionary)


embedding_types = [
    WordEmbeddings('pl'),
    FlairEmbeddings('pl-forward'),
    FlairEmbeddings('pl-backward'),
    CharacterEmbeddings(),
]

embeddings = StackedEmbeddings(embeddings=embedding_types)
slot_tagger = SequenceTagger(hidden_size=256, embeddings=embeddings,
                        tag_dictionary=slot_tag_dictionary,
                        tag_type='slot', use_crf=True)
frame_tagger = SequenceTagger(hidden_size=256, embeddings=embeddings,
                        tag_dictionary=frame_tag_dictionary,
                        tag_type='frame', use_crf=True)

slot_trainer = ModelTrainer(slot_tagger, slot_corpus)
slot_trainer.train('slot-model',
            learning_rate=0.1,
            mini_batch_size=32,
            max_epochs=30,
            train_with_dev=False)

            
frame_trainer = ModelTrainer(frame_tagger, frame_corpus)
frame_trainer.train('frame-model',
            learning_rate=0.1,
            mini_batch_size=32,
            max_epochs=30,
            train_with_dev=False)