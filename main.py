import face_recognition
import cv2
import numpy as np

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not video_capture.isOpened():
    print("Error: Cannot access the webcam.")
    exit()

# Load known faces and encodings
print("[INFO] Loading known faces...")

known_face_encodings = []
known_face_names = []

def load_face(image_path, name):
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    if encodings:
        known_face_encodings.append(encodings[0])
        known_face_names.append(name)
        print(f"[INFO] Loaded: {name}")
    else:
        print(f"[WARNING] No face found in image: {name}")

# Add your known faces here
load_face("/Users/gayathri/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Downloads/gayathri.jpg", "HI GAYATHRI! ")
load_face("/Users/gayathri/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Downloads/person2.jpg", "ZENDAYA")
load_face("/Users/gayathri/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Downloads/suma1.jpg", "HI SUMA! ")
load_face("/Users/gayathri/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Downloads/suni.jpg", "HI SUNIL!")
load_face("/Users/gayathri/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Downloads/dad.jpg", "HI DAD !")
load_face("/Users/gayathri/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Downloads/siva.jpg", "HI SIVA!")


print("[INFO] Face encodings loaded.")

# Variables for processing frames
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Main loop
while True:
    ret, frame = video_capture.read()

    if not ret:
        print("Failed to grab frame from webcam.")
        continue

    # Process every other frame for performance
    if process_this_frame:
        # Resize frame to 1/4 size for faster processing (optional)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect faces
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            name = "Unknown"
            if known_face_encodings:
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since frame was resized to 1/4
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw box and label
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Show the result
    cv2.imshow('Video', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
video_capture.release()
cv2.destroyAllWindows()
