"""
Emotion Detection Server

Using a Flask server, this file detects the emotion from user input string.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Main function to render template of index.html in templates folder.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detection():
    """
    Function retrieves user input. 
    Sends rejection message for blank input and prints emotion detection otherwise.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid Text! Please try again!"

    return (
            "For the given statement, the system response is"+
            f" 'anger': {response['anger']},"+
            f" 'disgust': {response['disgust']}, 'fear': {response['fear']},"+ 
            f" 'joy': {response['joy']}, and 'sadness': {response['sadness']}."+
            f" The dominant emotion is {response['dominant_emotion']}."
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
