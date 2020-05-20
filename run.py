from drboson.drboson import DRBoson
import flask
import random
import time
import pathlib


def run(drboson=DRBoson(), dataset_location=None):
    for i in range(10):
        time.sleep(2)
        drboson.log({'step': 1, 'random': random.random()}, step=i, commit=False)
        drboson.log({'additional': random.random()}, step=i)

    some_file = pathlib.Path('something.txt')
    with open(some_file, 'a') as file:
        file.write(f'{dataset_location}')

        make an error

        for i in range(20):
            file.write(f'This is some random number in a file: {i}\n')

    drboson.save(some_file)
