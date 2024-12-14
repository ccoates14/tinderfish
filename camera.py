import cv2

class Camera:

    def __init__(self, camera):
        self.camera = camera

    def take_picture(self, pic_num):
        MAX_ATTEMPTS = 10

        if not self.camera.isOpened():
            raise "camera not connected"
        
        count = 0

        while count < MAX_ATTEMPTS:
            ret, frame = self.camera.read()

            if ret:
                image_name = "capture_img" + str(pic_num) + ".jpeg"
                cv2.imwrite(image_name, frame)
                print('saved pic ' + image_name)
                break
            else:
                print('error capture image')
                print('retrying...')
            count += 1