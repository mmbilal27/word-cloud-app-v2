import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import io
import base64

# Set the title and page icon
st.set_page_config(page_title="my word cloud app", page_icon="✅")

# Function to generate a word cloud
def generate_word_cloud(text, stopwords):
    wordcloud = WordCloud(stopwords=stopwords, background_color='white', width=800, height=400).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

# Function to generate word frequency table
def generate_word_frequency_table(text):
    words = text.split()
    word_freq = Counter(words)
    df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])
    df = df.sort_values(by='Frequency', ascending=False)
    st.write(df)

# Main Streamlit app
def main():
    st.title("my word cloud app")
    
    # Upload a file
    uploaded_file = st.file_uploader("Upload a document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
    
    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        st.subheader("Uploaded Document")
        st.write(file_contents)
        
        # Checkbox for removing stop words
        remove_stopwords = st.checkbox("Remove Stop Words")
        
        # Generate word cloud
        if remove_stopwords:
            stopwords = set(st.text_area("Enter additional stop words (comma-separated)", "").split(','))
            generate_word_cloud(file_contents, stopwords)
        else:
            generate_word_cloud(file_contents, set())

        # Generate word frequency table
        st.subheader("Word Frequency Table (Top 10)")
        generate_word_frequency_table(file_contents)

    # Social media links
    st.sidebar.title("Connect with Me")
    st.sidebar.markdown("[LinkedIn](YOUR_LINKEDIN_URL)")
    st.sidebar.markdown("[GitHub](YOUR_GITHUB_URL)")
    st.sidebar.markdown("[Twitter](YOUR_TWITTER_URL)")

if __name__ == "__main__":
    main()
