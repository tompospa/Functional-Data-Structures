
from Element import *

def q_0_print(q):
    queue_arr = []
    head = q.head
    tail = reverse(q.tail)

    while True:
        queue_arr.append(head)
        if head.next is None:
            break
        head = head.next

    while True:
        queue_arr.append(tail)
        if tail.next is None:
            break
        tail = tail.next    

    return queue_arr


def q_1_print(q):
    queue_arr = []
    head = q.head_origin
    tail = reverse(q.tail)
    n_head = q.n_head
    n_tail = reverse(q.n_tail)

    while True:
        queue_arr.append(head)
        if head.next is None:
            break
        head = head.next

    while True:
        queue_arr.append(tail)
        if tail.next is None:
            break
        tail = tail.next    

    while True:
        queue_arr.append(n_head)
        if n_head.next is None:
            break
        n_head = n_head.next    

    while True:
        queue_arr.append(n_tail)
        if n_tail.next is None:
            break
        n_tail = n_tail.next                

    return queue_arr    

def q_2_print(q):
    queue_arr = []
    head = q.head_origin
    n_head = q.n_head
    n_tail = reverse(q.n_tail)
    #slozitejsi prvni je head_origin pocitat kolik jsem prosel
    #odecist od toho q.#copy a ten pocet preskocit pri pridavani z n_head
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
