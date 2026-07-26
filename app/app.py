import streamlit as st
import joblib
import numpy as np

from gensim.models import Word2Vec


svc = joblib.load('../model/linear_svc.pkl')

w2v = Word2Vec.load("../model/word2vec.model")


def sentence_to_vec(tokens, model):

    vectors = [model.wv[w] for w in tokens if w in model.wv]

    if len(vectors) == 0:
        return np.zeros(model.wv.vector_size)

    return np.mean(vectors, axis=0)


st.title("😊 Happy / Sad Classifier")

text = st.text_area("Enter your sentence")


if st.button("Predict"):

    tokens = text.lower().split()

    emb = sentence_to_vec(tokens, w2v)

    pred = svc.predict([emb])[0]

    if pred == 0:
        st.success("😊 HAPPY")
    else:
        st.error("😢 SAD")
