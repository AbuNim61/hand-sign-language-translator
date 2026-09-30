# untuk menankap dataset
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np 
import math
import time 

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgSize = 300

folder = "Data/makan"  
counter = 0
delay_after_capture = 0.5  

while True:
    success, img = cap.read()
    if not success:
        print("Gagal mengakses kamera.")
        break

    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y-offset:y+h+offset, x-offset:x+w+offset]

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize

        cv2.imshow("imageCrop", imgCrop)
        cv2.imshow("imageWhite", imgWhite)

    cv2.imshow("image", img)
    key = cv2.waitKey(1)
    if key == ord("s"):
        counter += 1
        filename = f'{folder}/Image_{time.time()}.jpg'
        cv2.imwrite(filename, imgWhite)
        print(f"Disimpan: {filename} ({counter})")
        time.sleep(delay_after_capture)  # delay untuk mencegah gambar duplikat
    elif key == ord("q"):
        print("Keluar dari program...")
        break

cap.release()
cv2.destroyAllWindows()
