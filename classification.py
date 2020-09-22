from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
import pickle
import joblib
from sklearn import feature_extraction, model_selection, naive_bayes, metrics, svm


import numpy as np
def same_x(x):
  return x

def classification(sms_df):
    vectorizer = joblib.load("dataset/features.joblib")

    best_svc = joblib.load("dataset/best_svc.joblib")

    # vectorization to TF-IDF
    record = vectorizer.transform(sms_df['message']).todense()


    # SVM with TF-IDF
    predict = best_svc.predict(record)

    return predict