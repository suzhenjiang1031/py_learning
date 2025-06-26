import cv2
from deepface import DeepFace

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    print("按 Q 键退出")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            # 分析人脸表情
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            dominant_emotion = result[0]['dominant_emotion']

            # 在图像上显示情绪
            cv2.putText(frame, f"Emotion: {dominant_emotion}", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        except Exception as e:
            print("检测失败：", e)

        # 显示窗口
        cv2.imshow("实时表情识别", frame)

        # 按 Q 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
