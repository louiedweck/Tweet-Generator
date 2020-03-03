from flask import Flask, render_template
from generate_sentence import generate_sentence
import os
from generate_sentence import sample
from histogram import get_num_tokens
from generate_sentence import generate_sentence


app = Flask(__name__)


@app.route('/')
def render_page():
    sentence = generate_sentence()
    return render_template('index.html', sentence=sentence)


if __name__ == '__main__':
    app.run(debug=True)
