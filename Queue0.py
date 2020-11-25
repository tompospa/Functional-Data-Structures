
from Element import *
from Queue1 import QueueOne, enqueue_one, dequeue_one


class QueueZero(object):

    def __init__(self, head, tail, lendiff):
        self.head = head
        self.tail = tail
        self.lendiff = lendiff #  = |head| - |tail|


def enqueue_zero(q, value):
    if q.lendiff == 0:
        return enqueue_one(QueueOne(q.head, q.head, q.tail, None, None, None, 0, 0), value)

    n_tail = Element(value, q.tail)
    q.lendiff -= 1
    return QueueZero(q.head, n_tail, q.lendiff)


def dequeue_zero(q):
    if q.lendiff == 0:
        return dequeue_one(QueueOne(q.head, q.head, q.tail, None, None, None, 0, 0))

    q.lendiff -= 1
    n_queue = QueueZero(q.head.next, q.tail, q.lendiff)
    return q.head.value, n_queue
