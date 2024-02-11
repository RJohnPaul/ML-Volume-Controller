# Hand Gesture Volume Control App

This Python script utilizes computer vision and gesture recognition techniques to control system volume based on hand gestures detected by a webcam.

## Dependencies
- [OpenCV (`cv2`)](#opencv)
- [PyAutoGUI (`pyautogui`)](#pyautogui)
- [Mediapipe (`mediapipe`)](#mediapipe)
- [Tkinter (`tk`)](#tkinter)

## Usage
1. Clone this repository to your local machine.
2. Ensure you have all dependencies installed (`opencv-python`, `pyautogui`, `mediapipe`, `tkinter`).
3. Run the `hand_gesture_recognition.py` script using Python.

```bash
python main.py
```

4. A GUI window will open with options to start and stop the recognition process.
5. When the recognition is active, hold your hand in front of the webcam.
6. Pointing your index finger up will increase the system volume, while pointing it down will decrease the volume.
7. Close the GUI window or press 'q' to stop the recognition process.

## How It Works
- The script captures video frames from the webcam using [OpenCV (`cv2`)](#opencv).
- It uses the [Mediapipe (`mediapipe`)](#mediapipe) library to detect hand landmarks in each frame.
- Based on the relative positions of the index finger and thumb landmarks, it determines whether the hand gesture is pointing up or down.
- If the gesture is pointing up, it simulates a press of the 'volume up' key using [PyAutoGUI (`pyautogui`)](#pyautogui).
- If the gesture is pointing down, it simulates a press of the 'volume down' key using [PyAutoGUI (`pyautogui`)](#pyautogui).

## Note
- Make sure your webcam is properly configured and positioned to capture your hand gestures accurately.
- Adjust the `min_detection_confidence` and `min_tracking_confidence` parameters in the `HandGestureApp` class initialization to fine-tune gesture recognition sensitivity.

---
