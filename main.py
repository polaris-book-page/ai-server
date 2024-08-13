import os

from dotenv import load_dotenv
from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from recommend_books import RecommendBooks

load_dotenv()

app = Flask(__name__)
api = Api(app, version='0.0.1')

CORS(app, origins=["https://polaris-book.vercel.app/", "http://localhost:3000/"])

api.add_namespace(RecommendBooks, '/recommend_books')

@app.route("/")
def test():
    return "hello world!"


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
