import cv2
from fer import FER

# 初始化摄像头和情绪识别器
cap = cv2.VideoCapture(0)
emotion_detector = FER()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 检测表情
    result = emotion_detector.detect_emotions(frame)
    for face in result:
        (x, y, w, h) = face["box"]
        emotions = face["emotions"]
        # 取最大情绪值
        dominant_emotion = max(emotions, key=emotions.get)

        # 在图像上绘制矩形和情绪文本
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, dominant_emotion, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # 显示窗口
    cv2.imshow('Face Emotion Detector', frame)

    # 按 q 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
