import pickle as pk
import pandas as pd
import numpy as np

if __name__ == "__main__":
    f = open("phan_loai.pkl", "rb")
    text_clf = pk.load(f)
    df = pd.read_csv("test.csv")
    X_test = df["problem"]
    y_test = df["label"]
    kq = text_clf.predict(X_test)
    print(kq)
    print(np.array(y_test))