import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Open the camera
cap = cv2.VideoCapture(0)

# Fingertip indices (thumb is treated differently)
finger_tips = [4, 8, 12, 16, 20]

while True:
    success, frame = cap.read()
    if not success:
        break

    # Flip the image horizontally (because webcam shows mirrored image)
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    fingers_up = 0

    # Convert the image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lm_list = []

            for id, lm in enumerate(hand_landmarks.landmark):
                lm_x, lm_y = int(lm.x * w), int(lm.y * h)
                lm_list.append((lm_x, lm_y))

            # Count the raised fingers
            if lm_list:
                # Thumb (moves horizontally)
                if lm_list[finger_tips[0]][0] > lm_list[finger_tips[0] - 1][0]:
                    fingers_up += 1

                # Other fingers (move vertically)
                for tip_id in finger_tips[1:]:
                    if lm_list[tip_id][1] < lm_list[tip_id - 2][1]:
                        fingers_up += 1

            # Draw the hand landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the number of raised fingers on the screen
    cv2.putText(frame, f'Fingers: {fingers_up}', (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1.8, (0, 255, 0), 3)

    cv2.imshow("Hand Tracking", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
