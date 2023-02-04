'''
Autor: Dominik Strzałko
Data: 05.08.2021
Zadanie: naiwny bayes2 gotowa biblioteka (Skeptic vs paranormal subreddits)

Wyniki z geval:
Likelihood      0.0000
Accuracy        0.7367
F1.0            0.4367
Precision       0.8997
Recall          0.2883
'''
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

def open_tsv(tsv):
    '''
    Funkcja do zamiany plików tsv jako listy linii tekstu.

    Na wejście potrzebuje ścieżkę do pliku .tsv

    np. X = open_tsv("train/expected.tsv")
    '''
    with open(tsv) as f:
        return f.readlines()

def Create_model(X_tsv, Y_tsv):
    '''
    Funkcja przeznaczona do tworzenia modelu uczenia maszynowego. 
    
    Na wejście trzeba podać zbiór X_train oraz Y_train w formie plików tsv.

    np. model = Create_model("train/in.tsv", "train/expected.tsv")
    '''

    X = open_tsv(X_tsv)
    Y = open_tsv(Y_tsv)

    Y = LabelEncoder().fit_transform(Y)
    pipeline = make_pipeline(TfidfVectorizer(),MultinomialNB())

    return pipeline.fit(X, Y)


def predict(model, X_tsv, file_name):
    '''
    Funkcja przeznaczona do predykcji wyników na podstawie modelu oraz zbiory X. trzecim argumentem w funkcji jest nazwa pliku z predykcjami, do zapisania na dysku.

    np. predict(model, "dev-0/in.tsv", "dev-0/out.tsv")
    '''
    X = open_tsv(X_tsv)

    prediction = model.predict(X)
    np.savetxt(file_name, prediction, fmt='%d')


def main():

    model = Create_model("train/in.tsv", "train/expected.tsv")

    predict(model, "dev-0/in.tsv", "dev-0/out.tsv")
    predict(model, "test-A/in.tsv", "test-A/out.tsv")


if __name__ == '__main__':
    main()