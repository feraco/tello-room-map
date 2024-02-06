from djitellopy import Tello
import cv2
import time

def capture_image(tello, img_count):
    """Capture an image from the drone's camera and save it to disk."""
    frame_read = tello.get_frame_read()
    cv2.imwrite(f"room_scan_{img_count}.jpg", frame_read.frame)
    print(f"Image room_scan_{img_count}.jpg captured.")
    time.sleep(1)  # Pause for a second to ensure image is saved

def main():
    tello = Tello()

    try:
        tello.connect()
        tello.streamon()  # Start video streaming
        tello.takeoff()

        # Define a simple flight path with image captures
        img_count = 1  # Initialize image counter
        capture_points = [  # Points where the drone will capture an image
            {"move": "up", "value": 100},
            {"move": "forward", "value": 100},
            {"move": "down", "value": 100},
            {"move": "backward", "value": 100}
        ]

        for point in capture_points:
            if point["move"] == "up":
                tello.move_up(point["value"])
            elif point["move"] == "forward":
                tello.move_forward(point["value"])
            elif point["move"] == "down":
                tello.move_down(point["value"])
            elif point["move"] == "backward":
                tello.move_back(point["value"])

            capture_image(tello, img_count)
            img_count += 1

            # Rotate to change the perspective for the next capture
            tello.rotate_clockwise(90)

        tello.land()
    finally:
        tello.streamoff()
        tello.end()

if __name__ == "__main__":
    main()
