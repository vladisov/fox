from picamera import PiCamera
from time import sleep

class Camera:
    def __init__(self):
        self.camera = PiCamera()

    def record(self, filename='video', duration=5):
        self.camera.start_recording(f'{filename}.h264')
        sleep(duration)
        self.camera.stop_recording()
