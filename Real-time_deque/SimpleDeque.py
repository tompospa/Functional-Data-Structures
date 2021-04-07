
class SimpleDeque(object):

    def __init__(self):
        self.list = []
        self.state = 4

def push_left_simple(value, dq):
    dq.list.insert(0,value)
    return dq

def push_right_simple(value, dq):
    dq.list.append(value)
    return dq

def pop_left_simple(dq):
    if not dq.list:
        return None, dq
    value = dq.list.pop(0)
    return value, dq

def pop_right_simple(dq):
    if not dq.list:
        return None, dq
    value = dq.list.pop()
    return value, dq