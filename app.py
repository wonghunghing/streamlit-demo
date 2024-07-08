import streamlit as st
from flask import Flask, redirect, request
import os

app = Flask(__name__)

@app.before_request
def before_request():
    if request.headers.get('X-Forwarded-Proto') == 'http':
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

def main():
    st.title('My Streamlit App')
    st.write('testing nice')
    # Your Streamlit app code here

if __name__ == '__main__':
    main()
