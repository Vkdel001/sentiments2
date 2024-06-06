from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Initialize the sentiment analysis pipeline
classifier = pipeline("sentiment-analysis")

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        user_input = request.form["text"]
        if user_input:
            result = classifier(user_input)[0]
            sentiment = result["label"]
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
