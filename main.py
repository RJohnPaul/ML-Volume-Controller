import cv2
import pyautogui
import mediapipe as mp
import tkinter as tk

class HandGestureApp:
    def __init__(self, master):
        self.master = master
        master.title("Hand Gesture Recognition")

        self.label = tk.Label(master, text="Hand Gesture Recognition", font=("Helvetica", 16, "bold"), fg="blue")
        self.label.pack(pady=10)

        self.start_button = tk.Button(master, text="Start", command=self.start_recognition, font=("Helvetica", 12), bg="green", fg="white")
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_recognition, font=("Helvetica", 12), bg="red", fg="white")
        self.stop_button.pack(pady=5)

        self.cap = cv2.VideoCapture(0)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                                          min_detection_confidence=0.5, min_tracking_confidence=0.5)
        self.mp_drawing = mp.solutions.drawing_utils
        self.recognition_active = False

    def start_recognition(self):
        self.recognition_active = True
        self.recognize_gestures()

    def stop_recognition(self):
        self.recognition_active = False

    def recognize_gestures(self):
        while self.recognition_active:
            ret, frame = self.cap.read()
            if not ret:
                break

            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(image_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                    index_finger_y = hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                    thumb_y = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y

                    if index_finger_y < thumb_y:
                        hand_gesture = 'pointing up'
                    elif index_finger_y > thumb_y:
                        hand_gesture = 'pointing down'
                    else:
                        hand_gesture = 'other'

                    if hand_gesture == 'pointing up':
                        pyautogui.press('volumeup')
                    elif hand_gesture == 'pointing down':
                        pyautogui.press('volumedown')

            cv2.imshow('Hand Gesture', frame)

            if cv2.waitKey(1) & 0xFF == ord('q') or not self.recognition_active:
                break

        self.cap.release()
        cv2.destroyAllWindows()

root = tk.Tk()
app = HandGestureApp(root)
root.mainloop()
