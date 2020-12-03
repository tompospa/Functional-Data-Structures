

from Element import *
from Queue import dequeue, enqueue
from SimpleQueue import SimpleQueue,s_dequeue, s_enqueue
from Queue0 import QueueZero
import random

def make_random_operations_array(min, max):
    number_of_operations = random.randint(min, max)
    operations = []
    values = []

    for _ in range(number_of_operations):
        choice = random.choice([True, False])
        operations.append(choice)
        if choice:
            values.append(random.randint(0,50))


    return operations, values

def do_operations_on_queue(operations, q, values):
    
    n_q = q 
    for x in range(len(operations)): # predelat na for element
        if operations[x]:
            n_q = enqueue(n_q, values[0])
        else:
            n_q = dequeue(n_q)
    return n_q

def compare_queues(q_1, q_2):
    pass # udelat z queues Array a porovnat Arrays    

if __name__ == '__main__':
    # udelat samostatne funce
    e = Element(5,None)
    print(e)

    q_simple = SimpleQueue()
    q = QueueZero(None, None, 0)

    operations, values = make_random_operations_array(10,100)
    
    do_operations_on_queue(operations, q_simple, values)   # operations and values on simple q
    do_operations_on_queue(operations, q, values) # same operations and values on my q

    compare_queues(q_simple, q)


