# Exercise Feedback AI

A computer vision system that uses pose estimation and biomechanical rules to analyze human exercise performance 

## Project Goal
Build an pose estimation powered feedback tool that detects common mistakes in exercises (e.g. butt wink, knee valgus) and gives automatic suggestions.

## Tech Stack
- Python
- [Mediapipe](https://google.github.io/mediapipe/) or OpenPose
- NumPy, OpenCV, Matplotlib
- Rule-based Biomechanical Analysis

## Components
- **Pose Extraction:** Detect 2D joint coordinates from video
- **Rule Engine:** Apply biomechanical rules to detect movement deviations
- **Feedback System:** Visual and text-based suggestions
- **Visualization:** Annotated video frames and summary graphics

## 📸 Example Output (coming soon)

![sample](media/sample_feedback.gif)

## Folder Structure
See project layout in the repo structure.

## Roadmap
- [ ] Set up pose estimation pipeline
- [ ] Define rules for squat analysis
- [ ] Generate sample output with visual feedback
- [ ] Add feedback logic for other exercises (optional)
