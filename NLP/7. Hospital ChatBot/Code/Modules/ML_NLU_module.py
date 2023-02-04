from flair.data import Sentence, Token
from flair.datasets import SentenceDataset
from flair.models import SequenceTagger

class ML_NLU:
    def __init__(self):
        self.slot_model, self.frame_model = self.setup()

    def nolabel2o(self, line, i):
        return 'O' if line[i] == 'NoLabel' else line[i]

    def conllu2flair(self, sentences, label=None):
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


    def predict(self, sentence):
        csentence = [{'form': word} for word in sentence]
        fsentence = self.conllu2flair([csentence])[0]
        self.slot_model.predict(fsentence)
        self.frame_model.predict(fsentence)
        possible_intents = {}
        for token in fsentence:
            for intent in token.annotation_layers["frame"]:
                if(intent.value in possible_intents):
                    possible_intents[intent.value] += intent.score
                else:
                    possible_intents[intent.value] = intent.score
        return [(token, ftoken.get_tag('slot').value) for token, ftoken in zip(sentence, fsentence)], max(possible_intents)

    def setup(self):
        slot_model = SequenceTagger.load('slot-model/final-model.pt')
        frame_model = SequenceTagger.load('frame-model/final-model.pt')
        return slot_model, frame_model

    def test_nlu(self, utterance):
        if utterance:
            slots, act = self.predict(utterance.split())
            slots = [x for x in slots if x[1] != 'O']
            arguments = self.convert_slot_to_argument(slots)
            return self.convert_act_to_list(act, arguments)
        else:
            return 'Critical Error'
    
    def convert_slot_to_argument(self, slots):
        arguments = []
        candidate = None
        for slot in slots:
            if slot[1].startswith("B-"):
                if(candidate != None):
                    arguments.append(candidate)
                candidate = [slot[1].replace("B-", ""), slot[0]]
            if slot[1].startswith("I-") and candidate != None and slot[1].endswith(candidate[0]):
                candidate[1] += " " + slot[0]
        if(candidate != None):
            arguments.append(candidate)
        return [(x[0], x[1]) for x in arguments]

    def convert_act_to_list(self, act, slots):
        result = []
        for i in range(len(slots)):
            intent = act
            domain = act.split('/')[0]
            slot = slots[i][0]
            value = slots[i][1]
            result.append([intent, domain, slot, value])
        return result