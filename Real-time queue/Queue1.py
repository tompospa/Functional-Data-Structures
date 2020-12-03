

from Element import *
from Queue2 import QueueTwo

class QueueOne(object):

    def __init__(self, head_origin, head, tail, head_reversed, n_head, n_tail, lendiff, delta_for_copy):
        self.head_origin = head_origin
        self.head = head
        self.tail = tail
        self.head_reversed = head_reversed
        self.n_head = n_head
        self.n_tail = n_tail
        self.lendiff = lendiff
        self.delta_for_copy = delta_for_copy
        self.state = 1



def enqueue_one(q, value):
    n_tail = Element(value, q.n_tail)
    lendiff = q.lendiff-1
    
    
    head = q.head
    tail = q.tail
    head_reversed = q.head_reversed
    n_head = q.n_head
    delta_for_copy = q.delta_for_copy
    
    #copy
    for _ in range(2):
        if head is not None:
            head_reversed = Element(head.value, head_reversed)
            head = head.next
            #copy from head to head_reversed *2 -> #copy+2 
            delta_for_copy +=1
        if tail is not None:
            n_head = Element(tail.value, n_head)
            tail = tail.next
            #copy from tail to n_head *2 -> lendiff+2
            lendiff +=1
        if head is None and tail is None:
            return QueueTwo(q.head_origin, head_reversed, n_head, n_tail, lendiff, delta_for_copy)
            
    
    return QueueOne(q.head_origin, head, tail, head_reversed, n_head, n_tail, lendiff, delta_for_copy)
    #new_n_tail = Element(value, q.tail) -> lendiff-1
    #podminka till tail none
    #copy from tail to n_head *2 -> lendiff+2
    #podminka till head none
    #copy from head to head_reversed *2 -> #copy+2 
    # return new Queue1
    


def dequeue_one(q):

    head_origin = q.head_origin.next
    delta_for_copy = q.delta_for_copy-1
    
    
    head = q.head
    tail = q.tail
    head_reversed = q.head_reversed
    n_head = q.n_head
    lendiff = q.lendiff

    for _ in range(2):
        if head is not None:
            head_reversed = Element(head.value, head_reversed)
            head = head.next            
            #copy from head to head_reversed *2 -> #copy+2 
            delta_for_copy +=1
        if tail is not None:
            n_head = Element(tail.value, n_head)
            tail = tail.next            
            #copy from tail to n_head *2 -> lendiff+2
            lendiff +=1
        if head is None and tail is None:
            return q.head_origin.value, QueueTwo(head_origin, head_reversed, n_head, q.n_tail, lendiff, delta_for_copy)

    return q.head_origin.value, QueueOne(head_origin, head, tail, head_reversed, n_head, q.n_tail, lendiff, delta_for_copy)
    #new_head_origin = head_origin.next #copy-1
    
    #podminka till tail none
    #copy from tail to n_head *2 -> lendiff+2
    #podminka till head none
    #copy from head to head_reversed *2 -> #copy+2 
    # return new Queue1


