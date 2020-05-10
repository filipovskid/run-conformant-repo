
def make_communication_message(id, type, payload):
    types = ['log', 'file', 'status']
    status_allowed_payload = ['pending', 'preparing', 'running', 'failed', 'completed']

    if type.lower() not in types:
        raise TypeError('drboson: Invalid message type')

    if type.lower() == 'status' and payload.lower() not in status_allowed_payload:
        raise ValueError('drboson: Invalid status')

    return {
        'id': id,
        'type': type,
        'payload': payload
    }
