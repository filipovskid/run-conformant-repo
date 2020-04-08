from DRBosonProducer import ClientProducer
import collections
import history
import messages
import json

class DRBoson:
    def __init__(self, producer=ClientProducer()):
        self.producer = producer
        self.history = history.History(self.producer)

    def log(self, log, step=None, commit=True):
        if not isinstance(log, collections.Mapping):
            raise ValueError("drboson: log must be a dictionary")

        for key in log.keys():
            if not isinstance(key, str):
                raise KeyError('drboson: key values must be strings')

        self.history.add(log, step=step, commit=commit)

    @staticmethod
    def __prepare_message(message_type, payload):
        message = messages.make_communication_message(id='', type=message_type, payload=payload)

        return json.dumps(message)

    def save(self):
        pass

    def started(self):
        message = DRBoson.__prepare_message(message_type='status', payload='started')
        self.producer.produce(message)

    def completed(self):
        message = DRBoson.__prepare_message(message_type='status', payload='completed')
        self.producer.produce(message)
