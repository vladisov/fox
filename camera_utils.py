import os
from datetime import datetime
from time import sleep


def _get_hour_prefix():
    return datetime.now().strftime("%Y-%m-%d-%H")


def _stub_create_file(filename, fun):
    sleep(1)
    print(f'{fun}: {filename}')
    with open(filename, 'w') as file:
        file.write('test')
