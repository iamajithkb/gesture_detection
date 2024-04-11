import cv2
import mediapipe as mp
from google.colab.patches import cv2_imshow

def get_user_input():
  """Prompts the user for gesture representation path, test video path, and frame interval."""

  gesture_path = input("Enter the path to your gesture representation (image or video): ")
  test_video_path = input("Enter the path to your test video: ")
  frame_interval = int(input("Enter the frame processing interval (process every nth frame): "))
  return gesture_path, test_video_path, frame_interval

def detect_hand_gesture(frame):
  """Detects hands in a frame using MediaPipe's hand detection model.

  Args:
      frame (np.ndarray): The input frame in BGR format.

  Returns:
      bool: True if a hand is detected, False otherwise.
  """

  mp_hands = mp.solutions.hands.Hands(
      max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
  mp_draw = mp.solutions.drawing_utils

  # Convert frame to RGB for MediaPipe processing
  rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

  # Detect hands in the frame
  results = mp_hands.process(rgb_frame)

  # Check if hands are detected
  return results.multi_hand_landmarks is not None

def main():
  """Main function to handle user input, video processing, and gesture detection."""

  gesture_path, test_video_path, frame_interval = get_user_input()

  # Open video capture
  cap = cv2.VideoCapture(test_video_path)
  if not cap.isOpened():
    print("Error opening video!")
    return

  # Frame count for tracking processed frames
  frame_count = 0

  while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Break if frame not captured or video ends
    if not ret:
      break

    # Process frame only if frame_count is a multiple of the interval
    if frame_count % frame_interval == 0:
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
    cv2_imshow(frame)  # Assuming you have cv2_imshow from google.colab.patches imported

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

    frame_count += 1  # Increment frame count

  # Release capture
  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  main()
