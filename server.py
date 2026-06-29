from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def emotion_api():
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if "error" in result:
        return "Invalid text! Please try again!"

    dominant_emotion = result.get("dominant_emotion")

    # ✅ Required error handling
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return jsonify({
        "anger": result["anger"],
        "disgust": result["disgust"],
        "fear": result["fear"],
        "joy": result["joy"],
        "sadness": result["sadness"],
        "dominant_emotion": dominant_emotion
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
