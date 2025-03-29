import cv2
import mediapipe as mp
import pandas as pd
import time

# Setup Mediapipe
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Create a list to hold all landmark data per frame
landmark_records = []

# Setup timer
recording_seconds = 10  # <–– set how long to record
start_time = time.time()

# Open webcam
cap = cv2.VideoCapture(0)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Timer check
        elapsed_time = time.time() - start_time
        if elapsed_time > recording_seconds:
            print("Recording ended.")
            break

        # Flip and convert image
        frame = cv2.flip(frame, 1)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Detect pose
        results = pose.process(image)

        # Convert back to BGR for display
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Draw landmarks
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
            )

            # Extract landmark coordinates
            landmarks = results.pose_landmarks.landmark
            frame_data = {"timestamp": elapsed_time}
            for idx, lm in enumerate(landmarks):
                frame_data[f"x_{idx}"] = lm.x
                frame_data[f"y_{idx}"] = lm.y
                frame_data[f"z_{idx}"] = lm.z
                frame_data[f"visibility_{idx}"] = lm.visibility
            landmark_records.append(frame_data)

        # Show frame
        cv2.imshow("Pose Estimation Recording", image)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()

# Save to CSV
df = pd.DataFrame(landmark_records)
df.to_csv("pose_landmarks.csv", index=False)
print("Landmark data saved to pose_landmarks.csv")
# Display the first few rows of the DataFrame
print(df.head())
# Display the shape of the DataFrame
print(f"Data shape: {df.shape}")
# Display the columns of the DataFrame
print(f"Columns: {df.columns.tolist()}")
