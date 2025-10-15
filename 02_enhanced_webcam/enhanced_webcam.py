import cv2
import time
import os

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Error: Could not open webcam.")
        return

    print("✅ Controls:")
    print("   q → Quit")
    print("   g → Toggle grayscale")
    print("   s → Save snapshot")

    # Create output folder for snapshots
    os.makedirs("snapshots", exist_ok=True)

    # Variables for FPS calculation
    prev_time = 0
    show_gray = False

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Failed to grab frame.")
            break

        # FPS calculation
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if prev_time else 0
        prev_time = curr_time

        # Grayscale toggle
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) if show_gray else frame

        # Show FPS on the frame
        text = f"FPS: {fps:.2f}"
        cv2.putText(display_frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0) if not show_gray else 255, 2)

        cv2.imshow("Enhanced Webcam", display_frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            print("👋 Exiting...")
            break
        elif key == ord('g'):
            show_gray = not show_gray
            print(f"🎨 Grayscale {'ON' if show_gray else 'OFF'}")
        elif key == ord('s'):
            filename = f"snapshots/snapshot_{int(time.time())}.jpg"
            cv2.imwrite(filename, frame)
            print(f"💾 Saved snapshot: {filename}")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
