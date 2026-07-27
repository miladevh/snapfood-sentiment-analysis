import streamlit as st
from pathlib import Path
import numpy as np
import joblib
from gensim.models import Word2Vec


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "linear_svc.pkl"
W2V_PATH = BASE_DIR / "model" / "word2vec.model"


svc = joblib.load(MODEL_PATH)
w2v = Word2Vec.load(str(W2V_PATH))





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
