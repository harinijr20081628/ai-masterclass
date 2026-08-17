import cv2

alg = "haarcascade_frontalface_default.xml"
haarcascade = cv2.CascadeClassifier(alg)

# video = "video_path"  # use a file path here, or 0 for default webcam
cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()  # reading frame from cam

    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = haarcascade.detectMultiScale(grayImg, 1.3, 4)  # get coordinates

    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face Detection", img)
    key = cv2.waitKey(10)

    if key == 27:  # escape key to stop
        break

cam.release()
cv2.destroyAllWindows()
