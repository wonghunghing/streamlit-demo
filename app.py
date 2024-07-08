import streamlit as st
from flask import Flask, redirect, request
import os

app = Flask(__name__)

@app.before_request
def before_request():
    url = request.url
    # Redirect http to https
    if request.headers.get('X-Forwarded-Proto') == 'http':
        print("redirect from http to https")
        url = url.replace('http://', 'https://', 1)
    # Redirect www to non-www
    if 'www.' in url:
        print("replace www to no-www")
        url = url.replace('www.', '', 1)
    # If either redirect is needed, perform it with a 301 status code
    if request.url != url:
        return redirect(url, code=301)

def main():
    st.title('My Streamlit App')
    st.write('testing nice')
    # Your Streamlit app code here

if __name__ == '__main__':
    main()
