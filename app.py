import streamlit as st
from flask import Flask, redirect, request, render_template_string
import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI

app = Flask(__name__)

@app.before_request
def before_request():
    url = request.url
    # Redirect http to https
    if request.headers.get('X-Forwarded-Proto') == 'http':
        print("redirect from http to https")
        url = url.replace('http://', 'https://', 1)
    # Redirect www to non-www
    if request.host.startswith('www.'):
        print("Redirecting from www to non-www")
        url = url.replace('www.', '', 1)
    # If either redirect is needed, perform it with a 301 status code
    if request.url != url:
        return redirect(url, code=301)

@app.errorhandler(404)
def page_not_found(e):
    # Redirect to root page
    return redirect('/', code=301)

def main():
    load_dotenv()
    st.title('My Streamlit App')
    st.write('testing nice 888888')
    llm = ChatOpenAI(model='gpt-3.5-turbo-0125')
    myinput = st.text_input("prompt")
    response = llm.invoke(input=myinput)
    st.write(response)
    
    
    # Your Streamlit app code here

if __name__ == '__main__':
    main()
