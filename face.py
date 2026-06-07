import sys
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_face_mesh = mp.solutions.face_mesh

# Windows fix #1: Use DirectShow backend for better camera compatibility
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Windows fix #9: Camera warm-up — discard first few frames
for _ in range(3):
    cap.read()

if not cap.isOpened():
    # Try MSMF backend as fallback
    cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
    if not cap.isOpened():
        print("Error: Could not open camera. Try changing the index (0-9).")
        sys.exit(1)  # Windows fix #2: sys.exit releases resources properly

try:
    with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=False,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as face_mesh:

        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Failed to grab frame. Exiting...")
                break

            # Windows fix #3: Convert color BEFORE setting writeable=False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = face_mesh.process(image)

            # Convert back to BGR for OpenCV rendering
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.multi_face_landmarks:
                custom_spec = mp_drawing.DrawingSpec(
                    color=(230, 216, 173), thickness=1, circle_radius=1
                )
                for face_landmarks in results.multi_face_landmarks:
                    mp_drawing.draw_landmarks(
                        image=image,
                        landmark_list=face_landmarks,
                        connections=mp_face_mesh.FACEMESH_TESSELATION,
                        landmark_drawing_spec=custom_spec,
                        connection_drawing_spec=custom_spec
                    )

            # Flip horizontally (mirror view) and display
            cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))

            # Windows fix #8: waitKey(10) reduces CPU load vs waitKey(5)
            key = cv2.waitKey(10) & 0xFF

            # Windows fix #7: Handle ESC, Q, and window close button
            if key == 27 or key == ord('q'):
                break
            if cv2.getWindowProperty('MediaPipe Face Mesh', cv2.WND_PROP_VISIBLE) < 1:
                break  # User clicked X on window

finally:
    # Windows fix #5 & #6: Always release in finally block
    cap.release()
    cv2.destroyAllWindows()
    print("Camera released. Goodbye!")
    