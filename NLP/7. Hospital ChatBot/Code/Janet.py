#import jsgf

from Modules.NLG_module import NLG
from Modules.DP_module import DP
from Modules.DST_module import Rules_DST
# from Modules.Book_NLU_module import Book_NLU
from Modules.ML_NLU_module import ML_NLU

import random
import torch
random.seed(42)
torch.manual_seed(42)

if torch.cuda.is_available():
    torch.cuda.manual_seed(0)
    torch.cuda.manual_seed_all(0)
    torch.backends.cudnn.enabled = False
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True

class Janet:
    def __init__(self):
        self.nlg = NLG()
        self.dp = DP()
        self.dst = Rules_DST()
        #self.nlu = Book_NLU(jsgf.parse_grammar_file('book.jsgf'))
        self.nlu_v2 = ML_NLU()

    def process(self, command):
        act = self.nlu_v2.test_nlu(command)
        system_acts = self.dp.predict(self.dst.update_user(act))
        return self.nlg.change_to_text(system_acts)


def main():
    janet = Janet()
    while(1):
        print('\n')
        text = input("Wpisz tekst: ")
        print(janet.process(text))

if __name__ == "__main__":
    main()