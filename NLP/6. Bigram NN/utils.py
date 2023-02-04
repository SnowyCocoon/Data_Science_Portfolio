import pandas as pd
import regex as re
from csv import QUOTE_NONE

ENCODING = "utf-8"

REP = re.compile(r"[{}\[\]\&%^$*#\(\)@\t\n0123456789]+")
REM = re.compile(r"'s|[\-]\\n|\-\\n|\p{P}")

def read_csv(fname):
    return pd.read_csv(
        fname,
        sep="\t",
        on_bad_lines='skip',
        header=None,
        quoting=QUOTE_NONE,
        encoding=ENCODING
    )

def clean_text(text):
    res = str(text).lower().strip()
    res = res.replace("’", "'")
    res = REM.sub("", res)
    res = REP.sub(" ", res)
    res = res.replace("'t", " not")
    res = res.replace("'s", " is")
    res = res.replace("'ll", " will")
    res = res.replace("won't", "will not")
    res = res.replace("isn't", "is not")
    res = res.replace("aren't", "are not")
    res = res.replace("'ve'", "have")
    return res.replace("'m", " am")

def get_words_from_line(line, specials = True):
    line = line.rstrip()
    if specials:
      yield '<s>'
    for m in re.finditer(r'[\p{L}0-9\*]+|\p{P}+', line):
        yield m.group(0).lower()
    if specials:
      yield '</s>'


def get_word_lines_from_data(d):
    for line in d:
        yield get_words_from_line(line)

