
def make_communication_message(id, type, payload):
    types = ['log', 'file', 'status']

    if type not in types:
        raise TypeError('drboson: Invalid message type')

    return {
        'id': id,
        'type': type,
        'payload': payload
    }
