from drboson.drboson import DRBoson
import flask
import random
import time
import pathlib

def write_dataset_lines(dataset_location, dest_file):
    with open(dataset_location, 'r') as f:
        for i in range(10):
            line = f.readline()
            
            if len(line) == 0:
                break

            dest_file.write(line)


def run(drboson=DRBoson(), dataset_location=None):
    for i in range(10):
        time.sleep(2)
        drboson.log({'step': 1, 'random': random.random()}, step=i, commit=False)
        drboson.log({'additional': random.random()}, step=i)

    some_file = pathlib.Path('something.txt')
    with open(some_file, 'a') as file:
        file.write(f'Dataset: {dataset_location} \n')

        for i in range(20):
            file.write(f'This is some random number in a file: {i}\n')

    drboson.save(some_file)

    dataset_print = pathlib.Path('dataset_data.txt')
    with open(dataset_print, 'a') as file: 
        file.write(f'Dataset: {dataset_location} \n')
        write_dataset_lines(dataset_location, file)

    drboson.save(dataset_print)
