from drboson.drboson import DRBoson
import flask
import random
import time


def run(drboson=DRBoson()):
    for i in range(10):
        time.sleep(2)
        drboson.log({'step': 1, 'random': random.random()}, step=i, commit=False)
        drboson.log({'additional': random.random()}, step=i)
