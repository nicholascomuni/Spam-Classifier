import pandas as pd
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle as pkl

dtf = pd.read_csv("spam_data.csv")

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(dtf['message'].values)
targets = dtf['class'].values

classifier = MultinomialNB()
classifier.fit(counts, targets)

with open("predictor.pkl","wb") as file:
    pkl.dump((vectorizer,classifier),file)
