📩 SMS Spam Classifier – Streamlit Web App

A Machine Learning–powered web application that detects whether an SMS message is Spam or Not Spam using Natural Language Processing techniques.
Live Demo ➝ https://sms-spam-classifier-c4bp7eeqzxevu8kuedxvkv.streamlit.app/

🚀 Overview

This project uses NLP preprocessing and a Multinomial Naive Bayes model to analyze text messages and classify them as:

✔️ Not Spam (Ham)

🚨 Spam

The model is trained on the famous SMS Spam Collection Dataset containing 5,572 labeled messages.
A simple and interactive Streamlit UI allows users to test any message instantly.

✨ Features

🧠 ML-based spam classification

⚡ Real-time predictions

🎨 Clean and user-friendly Streamlit interface

📦 Pickle-based model & vectorizer for easy deployment

🔍 Handles various types of spam (ads, scams, promotions, phishing)

🛠️ Technologies Used

Python

Pandas

NumPy

NLTK

Scikit-Learn

Streamlit

📂 Project Structure
📁 SMS-Spam-Classifier
│── app.py
│── vectorizer.pkl
│── spam_detect_model.pkl
│── requirements.txt
│── README.md

🧠 Model Workflow

Text cleaning (regex, lowercasing, stopword removal, stemming)

Convert text to numerical vectors using CountVectorizer

Train model using Multinomial Naive Bayes

Save vectorizer & model as .pkl files

Load files in app.py and predict user input

▶️ Run Locally
1. Install dependencies
pip install -r requirements.txt

2. Run the Streamlit app
streamlit run app.py

🌐 Live Deployment

The app is deployed using Streamlit Cloud and can be accessed here:

👉 https://sms-spam-classifier-c4bp7eeqzxevu8kuedxvkv.streamlit.app/

📌 Dataset

This model is trained on the SMS Spam Collection Dataset, containing real-world SMS messages labeled as "ham" (not spam) or "spam".

📜 License

This project is open-source and free to use for learning and research.

💡 Author

Aryan Gupta
Machine Learning & NLP Enthusiast
