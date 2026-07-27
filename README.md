# 🍽️ Snapfood Sentiment Analysis

A Machine Learning and NLP project for sentiment analysis on Persian Snapfood reviews.

This project compares traditional NLP feature extraction methods (**TF-IDF** and **Word2Vec**) with multiple machine learning classifiers to identify whether a review expresses a **positive (HAPPY)** or **negative (SAD)** sentiment.

---

## 📌 Features

- Persian text preprocessing
- Tokenization
- TF-IDF feature extraction
- Word2Vec embeddings
- Multiple ML models comparison
- Streamlit web application
- Model persistence with Joblib

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Gensim
- Streamlit
- Joblib

---

## 📂 Project Structure

```
snapfood-sentiment-analysis/

├── app/
│   └── app.py
│
├── data/
│   ├── train.csv
│   ├── validation.csv
│   ├── test.csv
│
├── model/
│   ├── linear_svc.pkl
│   └── word2vec.model
│
├── notebooks/
│   └── notebook.ipynb
│
├── src/
│   ├── preprocessing.py
│   └── tokenization.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Machine Learning Pipeline

```
Raw Text
      │
      ▼
Preprocessing
      │
      ▼
Tokenization
      │
      ├──────────────┐
      ▼              ▼
   TF-IDF        Word2Vec
      │              │
      ▼              ▼
 Logistic      Logistic
 LinearSVC     LinearSVC
 NaiveBayes    MLP
      │
      ▼
Evaluation
```

---

## 📊 Models

### TF-IDF

- Logistic Regression
- Linear SVC
- Multinomial Naive Bayes

### Word2Vec

- Logistic Regression
- Linear SVC
- MLPClassifier

---

## 📈 Results

### TF-IDF

| Model | Accuracy |
|--------|---------:|
| Logistic Regression | 0.76 |
| Linear SVC | 0.75 |
| Multinomial Naive Bayes | 0.77 |

### Word2Vec

| Model | Accuracy |
|--------|---------:|
| Logistic Regression | 0.80 |
| **Linear SVC** | **0.81** |
| MLPClassifier | 0.78 |

🏆 Best Model:

**Word2Vec + LinearSVC**

Accuracy: **81%**

---

## 🚀 Run Locally

Clone the repository

```bash
git clone https://github.com/miladevh/snapfood-sentiment-analysis.git

cd snapfood-sentiment-analysis
```

Create virtual environment

```bash
python -m venv env
```

Linux / macOS

```bash
source env/bin/activate
```

Windows

```bash
env\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app/app.py
```

---

## 💻 Demo

Enter a Persian review.

The application predicts whether the sentiment is:

- 😊 HAPPY
- 😞 SAD

---

## 📚 Future Improvements

- Fine-tune ParsBERT
- Sentence Transformers
- RAG-based chatbot
- FastAPI REST API
- Docker deployment

---

## 👨‍💻 Author

Milad

GitHub:

https://github.com/miladevh
