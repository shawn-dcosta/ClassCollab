import csv
import os
import pickle
import time
from datetime import datetime

import cv2
from sklearn.neighbors import KNeighborsClassifier


def test():
    video = cv2.VideoCapture(0)
    facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    with open('data/names.pkl', 'rb') as w:
        LABELS = pickle.load(w)
    with open('data/faces_data.pkl', 'rb') as f:
        FACES = pickle.load(f)

    print('Shape of Faces matrix --> ', FACES.shape)

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(FACES, LABELS)

    COL_NAMES = ['NAME', 'TIME']

    while True:
        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            crop_img = frame[y:y + h, x:x + w, :]
            resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
            output = knn.predict(resized_img)
            ts = time.time()
            date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
            timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")
            exist = os.path.isfile("Attendance/Attendance_" + date + ".csv")
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 2)
            cv2.rectangle(frame, (x, y - 40), (x + w, y), (50, 50, 255), -1)
            cv2.putText(frame, str(output[0]), (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)
            attendance = [str(output[0]), str(timestamp)]
        cv2.imshow("Frame", frame)
        k = cv2.waitKey(1)
        if k == ord('o'):
            if exist:
                with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(attendance)
                csvfile.close()
            else:
                with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(COL_NAMES)
                    writer.writerow(attendance)
                csvfile.close()
        if k == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()


# test()

# import csv
# import os
# import pickle
# import time
# from datetime import datetime
#
# import cv2
# from sklearn.neighbors import KNeighborsClassifier
#
# video = cv2.VideoCapture(0)
# facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
#
# with open('data/names.pkl', 'rb') as w:
#     LABELS = pickle.load(w)
# with open('data/faces_data.pkl', 'rb') as f:
#     FACES = pickle.load(f)
#
# print('Shape of Faces matrix --> ', FACES.shape)
#
# knn = KNeighborsClassifier(n_neighbors=5)
# knn.fit(FACES, LABELS)
#
# COL_NAMES = ['NAME', 'TIME']
#
# while True:
#     ret, frame = video.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = facedetect.detectMultiScale(gray, 1.3, 5)
#     exist = False  # Define exist outside the loop
#     for (x, y, w, h) in faces:
#         crop_img = frame[y:y + h, x:x + w, :]
#         resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
#         output = knn.predict(resized_img)
#         ts = time.time()
#         date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
#         timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")
#         exist = os.path.isfile("Attendance/Attendance_" + date + ".csv")
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 2)
#         cv2.rectangle(frame, (x, y - 40), (x + w, y), (50, 50, 255), -1)
#         cv2.putText(frame, str(output[0]), (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)
#         attendance = [str(output[0]), str(timestamp)]
#         # Write attendance inside the loop
#         if exist:
#             with open("Attendance/Attendance_" + date + ".csv", "a") as csvfile:
#                 writer = csv.writer(csvfile)
#                 writer.writerow(attendance)
#         else:
#             with open("Attendance/Attendance_" + date + ".csv", "a") as csvfile:
#                 writer = csv.writer(csvfile)
#                 writer.writerow(COL_NAMES)
#                 writer.writerow(attendance)
#     cv2.imshow("Frame", frame)
#     k = cv2.waitKey(1)
#     if k == ord('q'):
#         break
#
# video.release()
# cv2.destroyAllWindows()