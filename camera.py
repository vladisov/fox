import os
from time import sleep

from camera_utils import _stub_create_file, _get_hour_prefix


class Camera:
    def __init__(self, resolution=(2592, 1944), framerate=15, rotation=0, env='dev'):
        self.env = env
        self.prefix = 'data'
        if env == 'dev':
            return

        from picamera import PiCamera
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.camera.rotation = rotation

    def record_video(self, filename='video', duration=5):
        filename = self._build_filepath(filename, 'h264')

        if self.env == 'dev':
            _stub_create_file(filename, 'record_video')
            return

        self.camera.start_recording(filename)
        sleep(duration)
        self.camera.stop_recording()
        return filename

    def make_pic(self, filename='image', duration=5):
        filename = self._build_filepath(filename, 'jpg')

        if self.env == 'dev':
            _stub_create_file(filename, 'make_pic')
            return

        sleep(duration)
        self.camera.capture(filename)
        return filename

    def _build_filepath(self, filename, extension):
        filename = f'{self.prefix}/{_get_hour_prefix()}/{filename}.{extension}'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        return filename
