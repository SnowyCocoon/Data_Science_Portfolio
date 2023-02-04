import pandas as pd
from collections import defaultdict
from utils import read_csv
from train import train_model, predict_data


def main():
    data = read_csv("train/in.tsv.xz")
    train_words = read_csv("train/expected.tsv")

    train_data = data[[6, 7]]
    train_data = pd.concat([train_data, train_words], axis=1)
    train_data["607"] = train_data[6] + train_data[0] + train_data[7]

    model = defaultdict(lambda: defaultdict(lambda: 0))
    alpha = 0.00002
    vocab = set()

    train_model(train_data, model,vocab,alpha)

    predict_data("dev-0/in.tsv.xz", "dev-0/out.tsv", model)
    predict_data("test-A/in.tsv.xz", "test-A/out.tsv", model)


if __name__ == "__main__":
    main()
