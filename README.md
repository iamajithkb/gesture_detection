# gesture_detection

This project demonstrates gesture detection using MediaPipe's hand detection model in a Google Colab environment. The code detects hands in a test video and displays a "DETECTED" message when a hand is found. You can adjust the frame processing interval to reduce computational cost for longer videos.

Requirements:

Google Colab account
A video file for testing (place it in your Google Drive)
An image or video representing the gesture you want to detect (place it in your Google Drive)

Instructions:

Mount Google Drive: Run the following code cell in Colab:

Python
from google.colab import drive
drive.mount('/content/drive')

Save the Code: Copy and paste the following code into a new Python file (e.g., gesture_detection.py) and save it in your Colab environment.
Run the Script: Execute the following code cell in Colab:

Python
from gesture_detection import main
main()
Use code with caution.
User Input: The script will prompt you for the paths to the gesture representation and test video stored in your Google Drive
Video Display: The script will process the video frames and display them with a "DETECTED" message if a hand is identified. Press 'q' to quit the video playback.
