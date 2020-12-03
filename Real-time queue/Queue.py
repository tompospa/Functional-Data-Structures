from Queue0 import QueueZero, enqueue_zero, dequeue_zero
from Queue1 import QueueOne, enqueue_one, dequeue_one
from Queue2 import QueueTwo, enqueue_two, dequeue_two

# todo prazdna queue

def enqueue(q,value):
    # misto typu podle promene tridy
    if type(q) is QueueZero:
        return enqueue_zero(q,value)
    if type(q) is QueueOne:
        return enqueue_one(q,value)
    if type(q) is QueueTwo:
        return enqueue_two(q,value)        

def dequeue(q):
    if type(q) is QueueZero:
        return dequeue_zero(q)
    if type(q) is QueueOne:
        return dequeue_one(q)
    if type(q) is QueueTwo:
        return dequeue_two(q)      