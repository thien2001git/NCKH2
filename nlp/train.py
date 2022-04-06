
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import pickle
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


if __name__ == "__main__":
    df = pd.read_csv("train.csv")
    X_train = df["problem"]
    y_train = df["label"]
    # label_encoder = LabelEncoder()
    # label_encoder.fit(y_train)
    # print(list(label_encoder.classes_), '\n')
    # y_train = label_encoder.transform(y_train)
    # y_test = label_encoder.transform(y_test)

    # Huân luyện
    start_time = time.time()
    text_clf = Pipeline([('vect', CountVectorizer(ngram_range=(1,1),
                                                max_df=0.8,
                                                max_features=None)), 
                        ('tfidf', TfidfTransformer()), 
                        ('clf', MultinomialNB())
                        ])
    # huấn luyện
    text_clf = text_clf.fit(X_train, y_train)
    train_time = time.time() - start_time
    print('Done training Naive Bayes in', train_time, 'seconds.')
    
    # lưu lại dùng sau
    pickle.dump(text_clf, open("phan_loai.pkl", 'wb'))

    # kq = text_clf.predict(X_test)
    # print(kq)
    # print(y_test)