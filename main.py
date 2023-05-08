from camera import Camera
from datetime import datetime

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    camera = Camera()
    filename = camera.make_pic(f'image-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}')
    print(filename)

