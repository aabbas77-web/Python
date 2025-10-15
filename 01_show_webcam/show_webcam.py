import cv2

def main():
    # Open default camera (0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Error: Could not open webcam.")
        return

    print("✅ Press 'q' to quit the webcam window.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Failed to grab frame.")
            break

        # Grayscale view
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Show the captured frame
        cv2.imshow("Webcam", frame)

        # Quit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
