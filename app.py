from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__) 
import logging
from logging.handlers import RotatingFileHandler
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)



# Initialize the sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

@app.route('/', methods=['GET', 'POST'])
def index():
    app.logger.info('Handling request for /')
    sentiment = None
    if request.method == 'POST':
        text = request.form['text']
        # Perform sentiment analysis here and assign the result to sentiment variable
        sentiment = classifier(text)  # Placeholder result
        app.logger.info(f'Analyzed text: {text}, Sentiment: {sentiment}')
    return render_template('index.html', sentiment=sentiment)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
