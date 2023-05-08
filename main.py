import argparse

from camera import Camera
from datetime import datetime


def run_camera(env='dev', n=10):
    camera = Camera(env=env)

    for i in range(n):
        filepath = camera.make_pic()
        print('created - ', filepath)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', type=str, help='Environment (dev, prod)')
    parser.add_argument('--n', type=int, help='Number of images')
    args = parser.parse_args()
    print('args = ', args)

    run_camera(args.env, args.n)
