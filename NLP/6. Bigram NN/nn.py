import torch
from utils import get_word_lines_from_data
from torchtext.vocab import build_vocab_from_iterator
import itertools


class Bigrams(torch.utils.data.IterableDataset):
    def __init__(self, data, vocabulary_size):
        self.vocab = build_vocab_from_iterator(
           get_word_lines_from_data(data),
           max_tokens = vocabulary_size,
           specials = ['<unk>'])
        self.vocab.set_default_index(self.vocab['<unk>'])
        self.vocabulary_size = vocabulary_size
        self.data = data

    @staticmethod
    def look_ahead_iterator(gen):
        w1 = None
        for item in gen:
            if w1 is not None:
                yield (w1, item)
            w1 = item

    def __iter__(self):
       return self.look_ahead_iterator(
           (self.vocab[t] for t in itertools.chain.from_iterable(get_word_lines_from_data(self.data))))

class Model(torch.nn.Module):
    def __init__(self, vocabulary_size, embedding_size):
        super(Model, self).__init__()
        self.model = torch.nn.Sequential(
            torch.nn.Embedding(vocabulary_size, embedding_size),
            torch.nn.Linear(embedding_size, vocabulary_size),
            torch.nn.Linear(embedding_size, vocabulary_size),
            torch.nn.Softmax()
        )

    def forward(self, x):
        return self.model(x)
