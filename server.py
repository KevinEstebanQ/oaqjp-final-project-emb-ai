"""
code for the Flask api exposing the endpoint to call the emotion detection
"""
from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/emotionDetector")
def handle_emotion_detection():
    query_user_emotion = request.args.get("textToAnalyze")    
    emotions_dict = emotion_detector(query_user_emotion)
    answer_string = ("For the given statement, the system response is"
                    f" 'anger': {emotions_dict['anger']}"
                    f", 'disgust': {emotions_dict['disgust']}, 'fear': {emotions_dict['fear']},"
                    f" 'joy': {emotions_dict['joy']} and 'sadness': {emotions_dict['sadness']}."
                    f" The dominant emotion is {emotions_dict['dominant_emotion']}.")
    return answer_string

app.run(debug=True)