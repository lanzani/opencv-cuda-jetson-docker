import time

import cv2
import mediapipe as mp


video_path = "/dev/video0"

# Initialize MediaPipe Pose and Drawing utilities
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Open the video file
cap = cv2.VideoCapture(video_path)
time.sleep(2)

frame_number = 0
csv_data = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Pose
    result = pose.process(frame_rgb)

    # Draw the pose landmarks on the frame
    if result.pose_landmarks:
        mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # for idx, landmark in enumerate(result.pose_landmarks.landmark):
        #
        #     print(f"{mp_pose.PoseLandmark(idx).name}: (x: {landmark.x}, y: {landmark.y}, z: {landmark.z})")

        right_eye = result.pose_landmarks.landmark[2]
        left_eye = result.pose_landmarks.landmark[5]

        # print(f"{mp_pose.PoseLandmark(2).name}: (x: {right_eye.x}, y: {right_eye.y}, z: {right_eye.z})")
        # print(f"{mp_pose.PoseLandmark(5).name}: (x: {left_eye.x}, y: {left_eye.y}, z: {left_eye.z})")

        if right_eye.x < left_eye.x:
            cv2.putText(frame, 'BACK', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, 'FRONT', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2, cv2.LINE_AA)

        # right_eye = mp_pose.PoseLandmark(2)
        # left_eye = mp_pose.PoseLandmark(5)
        # print(mp_pose.PoseLandmark(2).landmark)
        # print(mp_pose.PoseLandmark(5).name)

    # Display the frame
    cv2.imshow('MediaPipe Pose', frame)

    # Exit if 'q' keypyt
    cv2.waitKey(1)
