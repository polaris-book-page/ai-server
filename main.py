import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

@app.route("/")
def test():
    return "hello world!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
