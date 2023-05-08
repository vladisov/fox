import os
from datetime import datetime


def _get_hour_prefix():
    return datetime.now().strftime("%Y-%m-%d-%H")


def _stub_create_file(filename, fun):
    print(f'{fun}: {filename}')
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        file.write('test')
