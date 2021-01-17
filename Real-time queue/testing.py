

from Element import Element
from Queue import enqueue, dequeue, get_empty_queue
from SimpleQueue import SimpleQueue
from RealTimeQueue import QueueZero, enqueue_zero, dequeue_zero, QueueOne, enqueue_one, dequeue_one, QueueTwo, enqueue_two, dequeue_two
import random
from queue_to_array import *
import copy


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

def do_operations_on_queue(operations, q, values_o):
    
    values = copy.deepcopy(values_o)
    n_q = q
    for x in operations:
        if x:
            n_q = enqueue(n_q, values[0])
            values.pop(0)
        else:
            v, n_q = dequeue(n_q)
    return n_q

def check_realtimeQ(real_time_queue, simple_queue, number_of_operation_for_testing):
    
    number_of_operations = number_of_operation_for_testing
    operations = []
    values = []

    #vytvoření pole operací a pole prvků pro přídání
    for _ in range(number_of_operations):
        choice = random.choice([True, False])
        operations.append(choice)
        if choice:
            values.append(random.randint(0,50))    

    #samotné testování
    for x in operations:
        if x:
            real_time_queue = enqueue(real_time_queue, values[0])
            simple_queue = enqueue(simple_queue, values[0])
            values.pop(0)
        else:
            v1, real_time_queue = dequeue(real_time_queue)
            v2, simple_queue = dequeue(simple_queue)
            if v1 != v2:
                return False

    return True

 

if __name__ == '__main__':

    print(check_realtimeQ( get_empty_queue() , SimpleQueue(), 10000) ) #vstupy jsou prázdné fronty jedna Realtimequeue a druhí Simplequeue a poslední argument je počet operací, které budou nad frontou provedeny


    #testování queue přes rovnost každáho prvku
    '''
    b = QueueZero(None, None, 0)

    operations, values = make_random_operations_array(10,100)

    b = do_operations_on_queue(operations, b, values)

    s = SimpleQueue()

    s = do_operations_on_queue(operations, s, values)
    
    if b.state == 0:
        print(q_0_to_array(b))
    if b.state == 1:
        print(q_1_to_array(b))

    if b.state == 2:
        print(q_2_to_array(b))

    print(s.qlist)
    '''

    




