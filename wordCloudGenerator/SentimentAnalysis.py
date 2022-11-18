import streamlit as st
import textblob
from textblob import TextBlob

st.title('Sentiment Analysis using Text Blob')
st.header('Enter you text to test')

testimonial = TextBlob("The food was great!")
print(testimonial.sentiment)

