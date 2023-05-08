import argparse

from camera import Camera
from datetime import datetime


def run_camera(env='dev'):
    camera = Camera(env=env)
    # filename = camera.make_pic(f'image-{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}')
    filename = camera.make_pic()
    print(filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', type=str, help='Environment (dev, prod)')
    args = parser.parse_args()
    print('args = ', args)
    run_camera(args.env)
