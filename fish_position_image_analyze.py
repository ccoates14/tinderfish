import cv2
import numpy as np

class FishPositionImageAnalyze:
    def __init__(self, image_name):
        self.image_name = image_name

    def is_goldfish_left_side(self):
        image = cv2.imread(self.image_name)
        image_width = image.shape[1]

        fish_position = self.locate_goldfish_by_color(self.image_name)
        x = fish_position[0]

        if x < image_width / 2:
            return True
        
        return False

    def locate_goldfish_by_color(self, image_path):
        # Load the image
        img = cv2.imread(image_path)

        # Convert to HSV color space
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Define the color range for orange
        lower_orange = np.array([10, 100, 100])
        upper_orange = np.array([30, 255, 255])

        # Create a mask for the orange color range
        mask = cv2.inRange(hsv, lower_orange, upper_orange)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find the largest contour (assuming it's the goldfish)
        largest_contour = max(contours, key=cv2.contourArea, default=None)

        if largest_contour is not None:
            x, y, w, h = cv2.boundingRect(largest_contour)
            return (x, y, w, h)
        else:
            return None


