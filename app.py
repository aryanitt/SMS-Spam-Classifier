import streamlit as st
import pickle

# Load vectorizer
with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Load model
with open('spam_detect_model.pkl', 'rb') as file:
    spam_detect_model = pickle.load(file)

st.title("📩 Spam Message Detector")
st.write("Enter a message and the model will predict whether it is spam or not.")

# Text Input
user_input = st.text_area("Type your message here:")

# Predict Button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message!")
    else:
        # Transform input message
        message_vector = vectorizer.transform([user_input])

        # Prediction
        y_pred = spam_detect_model.predict(message_vector)

        # Output
        if y_pred[0] == 0:
            st.error("🚨 This message is **SPAM**!")
        else:
            st.success("✔ This message is **NOT SPAM**!")
