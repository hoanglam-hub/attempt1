import cv2
from configs import frame_width, frame_height


class Camera:
    def __init__(self, cam_id=0):
        self.cap = cv2.VideoCapture(cam_id)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    def read(self):
        return self.cap.read()

    def release(self):
        self.cap.release()