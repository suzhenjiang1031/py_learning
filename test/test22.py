import cv2
from fer import FER

cap = cv2.VideoCapture(0)
emotion_detector = FER()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = emotion_detector.detect_emotions(frame)
    for face in result:
        (x, y, w, h) = face["box"]
        emotions = face["emotions"]
        dominant_emotion = max(emotions, key=emotions.get)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, dominant_emotion, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow('Face Emotion Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
