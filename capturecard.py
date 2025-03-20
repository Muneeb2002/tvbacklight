import cv2
import numpy as np

# Open the capture device (modify device index if needed)
cap = cv2.VideoCapture(0)  # Use /dev/video0, change index if required

# Set resolution if needed (optional, depends on your capture card)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        continue

    # Resize to 2x2 with RGB (preserving color)
    small_frame = cv2.resize(frame, (2, 2), interpolation=cv2.INTER_AREA)

    # Convert the 2x2 BGR array to RGB format
    small_frame_rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Print the 2x2 RGB values
    print("\n2x2 RGB Pixel Values:")
    print(np.array(small_frame_rgb, dtype=int))  # Print as integer values

    # Optional: Add a small delay to control processing speed
    cv2.waitKey(1000)  # Adjust for real-time processing

# Cleanup
cap.release()
cv2.destroyAllWindows()
