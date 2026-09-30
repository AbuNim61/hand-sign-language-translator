# test 2
import cv2
import numpy as np
import math
import tensorflow as tf
from cvzone.HandTrackingModule import HandDetector
from gtts import gTTS
import io
import pygame


pygame.mixer.init()


model = tf.keras.models.load_model("Model/model_sibi.h5")
labels = ["aku", "makan", "sedang"]  


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)


offset = 20
imgSize = 224  

last_label = ""

def play_text(text):
    tts = gTTS(text=text, lang='id')
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    pygame.mixer.music.load(audio_buffer, "mp3")
    pygame.mixer.music.play()

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y-offset:y + h+offset, x-offset:x + w+offset]

        try:
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

            # Preprocessing untuk model
            imgInput = cv2.resize(imgWhite, (224, 224))
            imgInput = imgInput.astype('float32') / 255.0
            imgInput = np.expand_dims(imgInput, axis=0)

            # Prediksi
            prediction = model.predict(imgInput)
            index = np.argmax(prediction)
            label = labels[index]
            print("Detected:", label)

            cv2.putText(imgOutput, label, (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 0, 255), 2)
            cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (255, 0, 255), 4)

            if label != last_label and not pygame.mixer.music.get_busy():
                play_text(label)
                last_label = label

        except Exception as e:
            print("Error:", e)

    cv2.imshow("Image", imgOutput)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
