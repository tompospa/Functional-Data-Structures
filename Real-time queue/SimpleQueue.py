from Element import Element

class SimpleQueue(object):

    def __init__(self):
        self.qlist = []

def s_enqueue(q, value):
    q.qlist.append(value)
    return q

def s_dequeue(q):
    value = q.qlist[0]
    return value, q.qlist.pop(0)

"""
q = Queue()
enqueue(q, 3)
enqueue(q, 35)
enqueue(q, 9)
enqueue(q, 12)
enqueue(q, 6)
enqueue(q, 7)
enqueue(q, 11)
print(q.qlist)
dequeue(q)
print(q.qlist)
"""