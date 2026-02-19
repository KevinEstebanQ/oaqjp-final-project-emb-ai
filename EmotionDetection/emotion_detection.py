""" emotion detection module """
import json
import requests

def emotion_detector(text_to_analyse):
    """
    Docstring for emotion_detector
    
    :param text_to_analyse: call the watson ai NLP and generate a sentiment analysis

    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/" \
            "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url=url, json=input_json, headers=header, timeout=5)
    json_obj = json.loads(response.text)
    emotion_predictions = json_obj["emotionPredictions"][0]["emotion"]
    new_emotions_dict = {**emotion_predictions, "dominant_emotion": ""}
    emotions_min_value = 0

    for k,v in emotion_predictions.items():
        if v > emotions_min_value:
            emotions_min_value = v
            new_emotions_dict["dominant_emotion"] = k
    return new_emotions_dict
