
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
        queue_arr.append(head)
        if head.next is None:
            break
        head = head.next

    while True:
        if tail is None:
            break
        queue_arr.append(tail)
        if tail.next is None:
            break
        tail = tail.next    

    while True:
        if n_head is None:
            break
        queue_arr.append(n_head)
        if n_head.next is None:
            break
        n_head = n_head.next    

    while True:
        if n_tail is None:
            break
        queue_arr.append(n_tail)
        if n_tail.next is None:
            break
        n_tail = n_tail.next                

    return queue_arr    

def q_2_to_array(q):
    queue_arr = []
    head = q.head_origin
    n_head = q.n_head
    n_tail = reverse(q.n_tail)
    pom = 0
    
    while True:
        if head is None:
            break
        queue_arr.append(head.value)
        pom +=1
        if head.next is None:
            break
        head = head.next

    pom = pom - q.delta_for_copy
    while True:
        if pom > 0:
            pom -= 1
            continue
        if n_head is None:
            break
        queue_arr.append(n_head.value)
        if n_head.next is None:
            break
        n_head = n_head.next        
       
    
    while True:
        if n_tail is None:
            break
        queue_arr.append(n_tail)
        if n_tail.next is None:
            break
        n_tail = n_tail.next      

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
