import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import imdb
import streamlit as st

def decode_review(encoded_review):
    reverse_word_index={value: key for key,value in word_index.items()}
    return ''.join([reverse_word_index.get(i-3,'?') for i in encoded_review])


#preprocess the user input
def preprocess_text(text):
    word_index=imdb.get_word_index()
    words=text.lower().split()
    encoded_review=[word_index.get(word,2)+3 for word in words]
    padded_review=sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_review



def predict_sentiment(review):
    model=load_model('Simple_rnn_imdb.h5')
    preprocessed_input=preprocess_text(review)
    prediction=model.predict(preprocessed_input)

    sentiment="Positive" if prediction[0][0] >0.5 else 'Negitive'

    return sentiment,prediction[0][0]

#loading the IMDB data set and word index
word_index=imdb.get_word_index()



st.title("IMDB movie review sentiment analysis")
st.write("Enter a movie review to classify it as positive or negitive")
user_input=st.text_area('Movie review')

if st.button('classify'):
    preprocessed_input=preprocess_text(user_input)
    #make predictions
    sentiment,prediction=predict_sentiment(preprocessed_input)
    st.write(f'Sentiment:{sentiment}')
    st.write(f'Prediction score:{prediction}')
else:
    st.write("Please enter a movie review")
    

# # example_review="This movie was fentastic ! and acting was great and plot was thrilling"

# sentiment,score=predict_sentiment(example_review)


# print(f'Review: {example_review}')
# print(f'Sentiment: {sentiment}')
# print(f'Prediction score: {score}')