from picamera import PiCamera
from time import sleep


class Camera:
    def __init__(self):
        self.camera = PiCamera()

    def record_video(self, filename='video', duration=5):
        self.camera.start_recording(f'{filename}.h264')
        sleep(duration)
        self.camera.stop_recording()

    def make_pic(self, filename='image'):
        sleep(5)
        filename = f'{filename}.jpg'
        self.camera.capture(filename)
        return filename
