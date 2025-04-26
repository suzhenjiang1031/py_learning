while True:
    ret, frame = cap.read()
    if not ret:
        break

    result = detector.detect_emotions(frame)

    for face in result:
        (x, y, w, h) = face["box"]
        emotions = face["emotions"]
        top_emotion = max(emotions, key=emotions.get)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, top_emotion, (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    cv2.imshow('Facial Emotion Recognition', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
