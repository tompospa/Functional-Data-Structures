from RealTimeQueue import QueueZero, enqueue_zero, dequeue_zero, QueueOne, enqueue_one, dequeue_one, QueueTwo, enqueue_two, dequeue_two
from SimpleQueue import SimpleQueue,s_dequeue, s_enqueue
import copy

# todo prazdna queue

def enqueue(q,value):
    
    #q_c = copy.deepcopy(q)

    if q.state == 0:
        return enqueue_zero(q,value)
    if q.state == 1:
        return enqueue_one(q,value)
    if q.state == 2:
        return enqueue_two(q,value)   
    # pro testovani pridana varianta i pro SimpleQueue
    if q.state == 3:
        return s_enqueue(q, value)     

def dequeue(q):

    #q_c = copy.deepcopy(q)

    if q.state == 0:
        return dequeue_zero(q)
    if q.state == 1:
        return dequeue_one(q)
    if q.state == 2:
        return dequeue_two(q)    
    # pro testovani pridana varianta i pro SimpleQueue
    if q.state == 3:
        return s_dequeue(q)           