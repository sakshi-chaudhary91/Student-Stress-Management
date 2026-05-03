from deepface import DeepFace
import cv2

def detect_emotion():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if ret:
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            return result[0]['dominant_emotion']
        except:
            return "Not detected"
    return "Camera Error"
