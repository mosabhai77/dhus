import streamlit as st
import requests
from bs4 import BeautifulSoup

def fetch_news_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all text from the webpage
        # Adjust the selector as needed based on the actual structure of the page
        news_content = soup.get_text(separator=' ', strip=True)
        return news_content
    except requests.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

def main():
    st.title('Messari News Text Fetcher')

    url = 'https://messari.io/news'
    st.write(f'Fetching text from: {url}')

    news_text = fetch_news_text(url)
    
    if news_text:
        st.subheader('News Text')
        st.text_area('Extracted Text', news_text, height=600)
    else:
        st.write('No text extracted.')

if __name__ == '__main__':
    main()
