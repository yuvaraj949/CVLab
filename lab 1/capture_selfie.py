import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow('Webcam — press s to save, q to quit')

while True:
    ok, frame = cap.read()
    if not ok:
        print('Camera not accessible. Check permissions.')
        break
    cv2.imshow('Webcam — press s to save, q to quit', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('s'):
        cv2.imwrite('my_selfie.jpg', frame)
        print("Saved my_selfie.jpg")
        break
    elif k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()