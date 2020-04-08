import collections
import numbers
import json
import messages


class History:
    def __init__(self, producer):
        self.producer = producer
        self.steps = 0
        self.log = {}

    def add(self, log, step=None, commit=True):
        if not isinstance(log, collections.Mapping):
            raise ValueError('Expected dict-like log object')

        for key, value in log.items():
            if not key:
                raise KeyError('Logging empty keys is not supported')
            if not isinstance(value, numbers.Number):
                raise ValueError('Logging is allowed for numeric metrics only')

        if step is None:
            self.update(log)
            self.__write()
        else:
            if not isinstance(step, numbers.Number):
                raise ValueError('Step must be a number')
            else:
                step = int(round(step))

                if step < self.steps:
                    raise ValueError('You are not allowed to log in past steps')
                elif step == self.steps:
                    pass
                else:
                    self.__write()
                    self.steps = step

            self.update(log)
            if commit:
                self.__write()

    def update(self, new_log):
        for key, value in new_log.items():
            key = key.strip()
            self.log[key] = value

    def __transform(self):
        logs = []

        for key, value in self.log.items():
            log = {
                key: value,
                '_step': self.steps
            }
            logs.append(log)

        return logs

    @staticmethod
    def __prepare_message(log):
        message = messages.make_communication_message(id='', type='log', payload=log)

        return json.dumps(message)

    def __write(self):
        logs = self.__transform()

        for log in logs:
            message = History.__prepare_message(log)
            self.producer.produce(message)

        self.steps += 1
