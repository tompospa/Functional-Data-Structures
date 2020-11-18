import random


class Element(object):

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return '{} '.format(self.value)


class Queue(object):

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __str__(self):
        h = self.head
        t = reverse(self.tail)
        # t = self.tail
        queue_str = 'head: '
        while True:
            queue_str = '{} {}'.format(queue_str, h)
            if h.next is None:
                break
            h = h.next
        queue_str = '{} tail: '.format(queue_str)
        while True:
            queue_str = '{} {}'.format(queue_str, t)
            if t.next is None:
                break
            t = t.next

        return queue_str


def enqueue(q, value):
    n_tail = Element(value, q.tail)
    return Queue(q.head, n_tail)


def dequeue(q):
    if queue_is_empty(q):
        pass  # dodelat chyba nelze odebrat, fronta je prazdna
    if head_is_empty(q):
        n_head = reverse(q.tail)
        n_queue = Queue(n_head.next, None)
        return n_head.value, n_queue

    else:
        n_queue = Queue(q.head.next, q.tail)
        return q.head.value, n_queue


def reverse_2(tail, reversed_tail):
    if tail is not None:
        x = Element(tail.value, reversed_tail)
        return reverse_2(tail.next, x)
    else:
        return reversed_tail
    pass


def reverse(tail):
    return reverse_2(tail, None)


def queue_is_empty(q):
    if q.head is None and q.tail is None:
        return True
    else:
        return False


def head_is_empty(q):
    if q.head is None:
        return True
    else:
        return False


def make_random_queue():
    head_size = random.randint(5, 15)
    tail_size = random.randint(5, 15)
    head = Element(random.randint(0, 50), None)
    tail = Element(random.randint(0, 50), None)
    head_2 = head
    tail_2 = tail

    for x in range(head_size):
        head_2.next = Element(random.randint(0, 50), None)
        head_2 = head_2.next
    for x in range(tail_size):
        tail_2.next = Element(random.randint(0, 50), None)
        tail_2 = tail_2.next

    return Queue(head, tail)


def print_queue(q):
    h = q.head
    t = reverse(q.tail)
    queue_str = 'head: '
    while True:
        queue_str = '{} {}'.format(queue_str, h)
        if h.next is None:
            break
        h = h.next
    queue_str = '{} tail: '.format(queue_str)
    while True:
        queue_str = '{} {}'.format(queue_str, t)
        if t.next is None:
            break
        t = t.next

    return queue_str


if __name__ == '__main__':
    q = make_random_queue()
    print(print_queue(q))
    print(q)

    value, q_2 = dequeue(q)
    print('removed Element has value {}'.format(value))
    print(q_2)

    value, q_3 = dequeue(q_2)
    print('removed Element has value {}'.format(value))
    print(q_3)

    q_4 = enqueue(q_3, 99)
    print(q_4)
