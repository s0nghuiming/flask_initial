from flask import Flask, request


app = Flask(__name__)

url_for('static', filename='style.css')
