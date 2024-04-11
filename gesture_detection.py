# -*- coding: utf-8 -*-
"""gesture_detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16i4zVVidovKNHw1s-cyrXt7wWAbk7LcZ
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install mediapipe

import cv2
import mediapipe as mp

def get_user_input():
  """Prompts the user for gesture representation path and test video path."""

  gesture_path = input("Enter the path to your gesture representation (image or video): ")
  test_video_path = input("Enter the path to your test video: ")
  return gesture_path, test_video_path

def detect_hand_gesture(frame):
  """Detects hands in a frame using MediaPipe's hand detection model.

  Args:
      frame (np.ndarray): The input frame in BGR format.

  Returns:
      bool: True if a hand is detected, False otherwise.
  """

  mp_hands = mp.solutions.hands.Hands(
      max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
  mp_draw = mp.solutions.drawing_utils

  # Convert frame to RGB for MediaPipe processing
  rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

  # Detect hands in the frame
  results = mp_hands.process(rgb_frame)

  # Check if hands are detected
  return results.multi_hand_landmarks is not None

def main():
  """Main function to handle user input, video processing, and gesture detection."""

  gesture_path, test_video_path = get_user_input()

  # Open video capture
  cap = cv2.VideoCapture(test_video_path)
  if not cap.isOpened():
    print("Error opening video!")
    return

  while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Break if frame not captured or video ends
    if not ret:
      break

    # Detect hand gesture
    hand_detected = detect_hand_gesture(frame)

    # Overlay "DETECTED" text if hand is detected
    if hand_detected:
      font = cv2.FONT_HERSHEY_SIMPLEX
      text_size, _ = cv2.getTextSize("DETECTED", font, 3, 2)
      text_x = (frame.shape[1] - text_size[0]) // 2
      text_y = text_size[1] + 10
      cv2.putText(frame, "DETECTED", (text_x, text_y), font, 3, (0, 255, 0), 2)

    # Display frame with (optional) gesture detection results
    from google.colab.patches import cv2_imshow
    cv2_imshow(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # Release capture
  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  main()