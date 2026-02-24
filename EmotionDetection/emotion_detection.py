import requests
import json  # For parsing JSON if needed

def emotion_detector(text_to_analyze):
    """
    Detect emotions in a given text using Watson NLP EmotionPredict.

    Parameters:
        text_to_analyze (str): The text to analyze.

    Returns:
        dict: A dictionary with emotions and dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    # Send POST request
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    # Convert response to dictionary
    result = response.json()  # Already a dict
    emotions = result.get("document", {}).get("emotion", {})

    # Extract required emotions
    anger = emotions.get("anger", 0)
    disgust = emotions.get("disgust", 0)
    fear = emotions.get("fear", 0)
    joy = emotions.get("joy", 0)
    sadness = emotions.get("sadness", 0)

    # Find dominant emotion
    dominant_emotion = max(
        {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness},
        key=lambda k: {"anger": anger, "disgust": disgust, "fear": fear, "joy": joy, "sadness": sadness}[k]
    )

    # Return formatted dictionary
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }