
from Element import Element
from Queue0 import QueueZero



class QueueTwo(object):

    def __init__(self, head_origin, head_reversed, n_head, n_tail, lendiff, delta_for_copy):
        self.head_origin = head_origin
        self.head_reversed = head_reversed
        self.n_head = n_head
        self.n_tail = n_tail
        self.lendiff = lendiff
        self.delta_for_copy = delta_for_copy
    

def enqueue_two(q, value):

    n_tail = Element(value, q.n_tail)
    lendiff = q.lendiff-1
    
    head_reversed = q.head_reversed
    n_head = q.n_head
    delta_for_copy = q.delta_for_copy

    
    for _ in range(2):
        if delta_for_copy == 0:
            return QueueZero(n_head,n_tail,lendiff)
        else:
            n_head = Element(head_reversed.value, n_head)
            head_reversed = head_reversed.next
            #napojit prvek z head_reversed do n_head * 2 -> lendiff+2 #copy-2
            lendiff +=1
            delta_for_copy -=1

    return QueueTwo(q.head_origin, head_reversed, n_head, n_tail, lendiff, delta_for_copy)
    #vlozit prvek do n_tail lendiff -1
    #napojit prvek z head_reversed do n_head * 2 -> lendiff+2 #copy-2
    
    


def dequeue_two(q):

    head_origin = q.head_origin.next
    delta_for_copy = q.delta_for_copy-1
    
    head_reversed = q.head_reversed
    n_head = q.n_head
    lendiff = q.lendiff

    #copy
    for _ in range(2):
        if delta_for_copy == 0:
            return q.head_origin.value, QueueZero(n_head,q.n_tail,lendiff)
        else:
            n_head = Element(head_reversed.value, n_head)
            head_reversed = head_reversed.next            
            #napojit prvek z head_reversed do n_head * 2 -> lendiff+2 #copy-2
            lendiff +=1
            delta_for_copy -=1
    
    return q.head_origin.value, QueueTwo(head_origin, head_reversed, n_head, q.n_tail, lendiff, delta_for_copy)
    # odebrat prvek s head_origin #copy -1
    #napojit prvek z head_reversed do n_head * 2 -> lendiff+2 #copy-2
    # kdyz je #copy 0 vratit queue0 s head, tail a lendiff 
    # pokud ne vratit na konci stejnou tridu s novymi param
    


