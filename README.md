# Face Recognition with OpenCV and face_recognition

This Python project uses OpenCV and the `face_recognition` library to perform real-time face recognition using your webcam. It detects faces, compares them against known faces, 
and labels recognized people live on the video feed.

---

## Features

- Real-time face detection and recognition from webcam.
- Load multiple known faces with custom labels.
- Draws bounding boxes and names around recognized faces.
- Unknown faces are labeled as "Unknown".
- Efficient frame processing for better performance.

---

## How to Use

### Prerequisites

- Python 3.7 or higher
- Webcam connected to your computer

### Install dependencies

Run the following command to install required libraries:

```bash
pip install face_recognition opencv-python numpy
Add Known Faces
Add images of known people in your local machine.

Update the load_face() function calls in main.py with the correct image paths and names.

Example:

python
Copy
Edit
load_face("/path/to/your/image.jpg", "Person Name")
Run the Project
Execute the main script:

bash
Copy
Edit
python main.py
A window will open showing the webcam feed.

Detected faces will have boxes and names displayed.

Press q to quit the program.

How It Works
The script loads known faces and their encodings.

It captures video from the webcam.

Every other frame is processed for face detection and recognition for better performance.

Matches are found by comparing current faces with known face encodings.

Recognized faces are labeled with their names; unknown faces are labeled as "Unknown".

Files
main.py — The main face recognition script.

.gitignore — Git ignore file.

README.md — This file.

Author
Gayathri Menon

