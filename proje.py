import cv2
import mediapipe as mp
import time
import serial

ser = serial.Serial('COM3', 9600)
time.sleep(1)
webcam = cv2.VideoCapture(0)

el = mp.solutions.hands
el_cizim = mp.solutions.drawing_utils

with el.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5) as eller:
    while True:
        _, frame = webcam.read()
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = eller.process(rgb)
        yuk, gen, _ = frame.shape

        if result.multi_hand_landmarks:
            for cizim in result.multi_hand_landmarks:
                el_cizim.draw_landmarks(frame, cizim, el.HAND_CONNECTIONS)
                koordinat1 = cizim.landmark[8]
                x = int(koordinat1.x * gen)
                y = int(koordinat1.y * yuk)
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

                if 30 <= x <= 160 and 30 <= y <= 120:
                    cv2.rectangle(frame, (30, 30), (160, 120), (0, 0, 255), -1)
                    ser.write(b'1')
                else:
                    ser.write(b'0')

                if 430 <= x <= 560 and 30 <= y <= 120:
                    cv2.rectangle(frame, (430, 30), (560, 120), (0, 255, 0), -1)
                    ser.write(b'2')
                else:
                    ser.write(b'3')

                if 230 <= x <= 360 and 30 <= y <= 120:
                    cv2.rectangle(frame, (230, 30), (360, 120), (0, 255, 255), -1)  # Sarı renkli kutu
                    ser.write(b'4')
                else:
                    ser.write(b'5')

        cv2.rectangle(frame, (30, 30), (160, 120), (0, 0, 255), 3)
        cv2.rectangle(frame, (430, 30), (560, 120), (0, 255, 0), 3)
        cv2.rectangle(frame, (230, 30), (360, 120), (0, 255, 255), 3)  # Sarı renkli kutu
        cv2.putText(frame, "Kirmizi Isik", (30, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        cv2.putText(frame, "Yesil Isik", (430, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
        cv2.putText(frame, "Sari Isik", (230, 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)  # Sarı renkli kutu

        cv2.imshow("pen", frame)
        if cv2.waitKey(5) & 0xFF == ord("q"):
            break

webcam.release()
cv2.destroyAllWindows()
