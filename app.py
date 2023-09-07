import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from io import BytesIO
import base64

# Set page title and icon
st.set_page_config(
    page_title="my word cloud app",
    page_icon="✅"
)

# Title of the app
st.title("my word cloud app")

# Upload a file
uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    file_contents = uploaded_file.read()

    # Checkbox for removing stop words
    remove_stopwords = st.checkbox("Remove Stop Words")

    if remove_stopwords:
        # User-defined stop words
        custom_stopwords = st.text_area("Enter additional stop words (comma-separated)", "")
        custom_stopwords = set(custom_stopwords.split(','))
    else:
        custom_stopwords = set()

    # Generate word cloud
    wordcloud = WordCloud(
        stopwords=custom_stopwords,
        background_color='white',
        width=800,
        height=400
    ).generate(file_contents)

    # Display word cloud
    st.subheader("Word Cloud")
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

    # Generate word frequency table
    st.subheader("Word Frequency Table (Top 10)")
    words = file_contents.split()
    word_freq = Counter(words)
    df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])
    df = df.sort_values(by='Frequency', ascending=False).head(10)
    st.write(df)

# Social media links
st.sidebar.title("Connect with Me")
st.sidebar.markdown("[LinkedIn](YOUR_LINKEDIN_URL)")
st.sidebar.markdown("[GitHub](YOUR_GITHUB_URL)")
st.sidebar.markdown("[Twitter](YOUR_TWITTER_URL)")


        
