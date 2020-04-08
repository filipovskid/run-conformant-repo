import sys
sys.path.append('./drboson')
from drboson.drboson import DRBoson
from drboson.DRBosonProducer import RemoteProducer
import socket
import run
import os


def main():

    bootstrap_servers = os.environ.get('BOOTSTRAP_SERVERS')
    producer_topic = os.environ.get('PRODUCER_TOPIC')
    run_id = os.environ.get("RUN_ID")
    project_id = os.environ.get("PROJECT_ID")

    conf = {
        'bootstrap.servers': bootstrap_servers,
        'client.id': socket.gethostname(),
        'retries': 10,
        'retry.backoff.ms': 1000,
        'queue.buffering.max.ms': 100
    }

    producer = RemoteProducer(conf, topic=producer_topic)
    drboson = DRBoson(producer)
    drboson.started()

    try:
        run.run(drboson)
    finally:
        drboson.completed()

    # run.run()


if __name__ == '__main__':
    main()
