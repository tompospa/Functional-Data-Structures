
from Element import Element

def q_0_to_array(q):
    queue_arr = []
    head = q.head
    tail = reverse(q.tail)

    while True:
        if head is None:
            break
        queue_arr.append(head.value)
        if head.next is None:
            break
        head = head.next

    #queue_arr.append(" | ")
    while True:
        if tail is None:
            break
        queue_arr.append(tail.value)
        if tail.next is None:
            break
        tail = tail.next    

    return queue_arr


def q_1_to_array(q):
    queue_arr = []
    head = q.head_origin
    tail = reverse(q.tail)
    n_head = q.n_head
    n_tail = reverse(q.n_tail)

    while True:
        if head is None:
            break
        queue_arr.append(head.value)
        if head.next is None:
            break
        head = head.next

    while True:
        if tail is None:
            break
        queue_arr.append(tail.value)
        if tail.next is None:
            break
        tail = tail.next    

    while True:
        if n_head is None:
            break
        queue_arr.append(n_head.value)
        if n_head.next is None:
            break
        n_head = n_head.next    

    while True:
        if n_tail is None:
            break
        queue_arr.append(n_tail.value)
        if n_tail.next is None:
            break
        n_tail = n_tail.next                

    return queue_arr    

def q_2_to_array(q):#
    queue_arr = []
    head = q.head_origin
    n_head = q.n_head
    n_tail = reverse(q.n_tail)
    
    
    for x in range(q.delta_for_copy):
        if head is None:
            break
        queue_arr.append(head.value)
        if head.next is None:
            break
        head = head.next

    
    while True:
        if n_head is None:
            break
        queue_arr.append(n_head.value)
        if n_head.next is None:
            break
        n_head = n_head.next        
       
    
    while True:
        if n_tail is None:
            break
        queue_arr.append(n_tail.value)
        if n_tail.next is None:
            break
        n_tail = n_tail.next      

    #z head_origin vzit #copy prvku pak vsechny z n_head a vsechy y reverse n_tail

    return queue_arr       


def reverse_2(tail, reversed_tail):
    if tail is not None:
        x = Element(tail.value, reversed_tail)
        return reverse_2(tail.next, x)
    else:
        return reversed_tail
    pass


def reverse(tail):
    return reverse_2(tail, None)
