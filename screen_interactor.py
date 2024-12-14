

import pyautogui

class ScreenInteractor:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y

    def print_screen_dimensions(self):
        """Prints the current screen width and height."""
        screen_width, screen_height = pyautogui.size()
        print(f"Screen Width: {screen_width}, Screen Height: {screen_height}")

    def click(self):
        """Simulates a mouse click at the starting position."""
        pyautogui.moveTo(self.start_x, self.start_y)
        pyautogui.click()

    def swipe_left(self, distance=150):
        """Simulates a left swipe from the starting position."""
        pyautogui.moveTo(self.start_x, self.start_y)
        pyautogui.dragTo(self.start_x - distance, self.start_y, duration=.5, button='left')

    def swipe_right(self, distance=150):
        """Simulates a right swipe from the starting position."""
        pyautogui.moveTo(self.start_x - 200, self.start_y)
        pyautogui.dragTo(self.start_x + distance, self.start_y, duration=0.5, button='left')