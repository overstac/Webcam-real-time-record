import cv2

video= cv2.VideoCapture(0)
succes, frame= video.read()

height= frame.shape[0]
width= frame.shape[1]

face_cascade= cv2.CascadeClassifier("faces.xml")
output= cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"DIVX"), 15, (width, height))

count= 0
while succes:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 4)

    cv2.imshow("Recording", frame)          # shows the camera live

    key= cv2.waitKey(1)
    if key == ord("q"):                     # quit when you press "q" button
        break
    output.write(frame)
    succes, frame= video.read()
    count += 1
    print(count)

output.release()
video.release()
cv2.destroyAllWindows()
