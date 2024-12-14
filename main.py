import cv2
import time
from camera import Camera
from fish_position_image_analyze import FishPositionImageAnalyze
from screen_interactor import ScreenInteractor

# take a sample pic

def wait_for_camera_access(camera_index):
    print("Waiting for camera authorization...")
    while True:
        cap = cv2.VideoCapture(camera_index)
        if cap.isOpened():
            print("Camera access granted!")
            return cap
        else:
            print("Camera not accessible. Please grant access.")

        cap.release()
        time.sleep(2)  # Wait for 2 seconds before retrying


# video_feed = wait_for_camera_access(0)
# camera = Camera(video_feed)

# pic_num = 0
# camera.take_picture(pic_num)

# video_feed.release()

# fish_position_image_analyze = FishPositionImageAnalyze("fishright.jpg")

# fish_position_image_analyze.determine_goldfish_position()

mouse_start_x = 3200
mouse_start_y = 500
screen_interactor = ScreenInteractor(mouse_start_x, mouse_start_y)

screen_interactor.print_screen_dimensions()
screen_interactor.swipe_right()