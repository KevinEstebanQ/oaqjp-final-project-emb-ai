"""
unit Testing logic for emtotion detection app
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    class meant to test various outputs of the emotion
    test application on the Emotion Detection package

    """
    def test_emotion_detection(self):
        """
        test 5 strings emotion guesses and assert their outputs
        """
        test_cases = {
            "I am glad this happened" : "joy",
            "I am really mad about this" : "anger",
            "I feel disgusted just hearing about this"  : "disgust",
            "I am so sad about this" : "sadness",
            "I am really afraid that this will happen" : "fear"
        }
        for k,v in test_cases.items():
            guessed_emotion = emotion_detector(k)
            self.assertEqual(guessed_emotion["dominant_emotion"], v, "assert  incorrect")

if __name__  == "__main__":
    unittest.main()
