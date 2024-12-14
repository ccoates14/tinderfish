import cv2
import time
from camera import Camera
from fish_position_image_analyze import FishPositionImageAnalyze
from screen_interactor import ScreenInteractor
import time

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

def swipe_left_or_right(direction):
    mouse_start_x = 3200
    mouse_start_y = 500
    screen_interactor = ScreenInteractor(mouse_start_x, mouse_start_y)
    if direction == "left":
        screen_interactor.swipe_left()
    else:
        screen_interactor.swipe_right()

video_feed = wait_for_camera_access(0)
# call back after .25 seconds
pic_num = 0
left_side_count = 0
MAX_PICS = 40

SECONDS_IN_HOUR = 3600

SAMPLE_SIZE = SECONDS_IN_HOUR * 4
count = 0

while count * 4 < SAMPLE_SIZE:
    camera = Camera(video_feed)
    camera.take_picture(pic_num)

    pic_num += 1

    if pic_num > MAX_PICS:
        for i in range(MAX_PICS):
            fish_position_image_analyze = FishPositionImageAnalyze("capture_img" + str(pic_num) + ".jpg")
            if fish_position_image_analyze.is_goldfish_left_side():
                left_side_count += 1
        
        if left_side_count > MAX_PICS / 2:
            swipe_left_or_right("left")
            print("swipe left")
        else:
            swipe_left_or_right("right")
            print("swipe right")
        
        pic_num = 0
        left_side_count = 0

    time.sleep(0.25)
    count += 1


video_feed.release()
