import streamlit as st
from flask import Flask, redirect, request
import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
import time

app = Flask(__name__)

load_dotenv()
llm = ChatOpenAI(model='gpt-3.5-turbo-0125')
st.title('My Streamlit App')
st.write('testing nice 888888')

# @app.before_request
# def before_request():
#     url = request.url
#     # Redirect http to https
#     if request.headers.get('X-Forwarded-Proto') == 'http':
#         print("Redirecting from http to https")
#         url = url.replace('http://', 'https://', 1)
#     # Redirect www to non-www
#     if request.host.startswith('www.'):
#         print("Redirecting from www to non-www")
#         url = url.replace('www.', '', 1)
#     # If either redirect is needed, perform it with a 301 status code
#     if request.url != url:
#         return redirect(url, code=301)

# @app.errorhandler(404)
# def page_not_found(e):
#     # Redirect to root page
#     return redirect('/', code=301)

def stream_data(response):
    for word in response.content.split(" "):
        yield word + " "
        time.sleep(0.02)

def main():
    myinput = st.text_input("prompt")
    if myinput:
        response = llm.invoke(input=myinput)
        st.write_stream(stream_data(response=response))

if __name__ == '__main__':
    # Run the Flask app
    app.run()
    # Run the Streamlit app
    main()
