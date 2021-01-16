

from Element import Element
from Queue import enqueue, dequeue
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
    for x in operations: # predelat na for element
        if x:
            n_q = enqueue(n_q, values[0])
            values.pop(0)
        else:
            v, n_q = dequeue(n_q)
    return n_q

def compare_queues(q_1, q_2):


    pass # udelat z queues Array a porovnat Arrays    

if __name__ == '__main__':
    # udelat samostatne funce
    #e = Element(5,None)
    #print(e)

    q_simple = SimpleQueue()
    
    #print(q_simple.qlist)
    q1 = enqueue(q_simple, 7)
    q2 = enqueue(q1, 8)
    q3 = enqueue(q2, 9)
    q4 = enqueue(q3, 10)
    print(q2)
    print(q4)
    print(q2.qlist)
    print(q4.qlist)
    k,l = dequeue(q4)
    print(l.qlist)

    print(q_simple.qlist)

    operations, values = make_random_operations_array(5,10)
    print("----------------------")
    b = QueueZero(None, None, 0)
    b = enqueue(b , 8)
    print(type(b))
    print(b)
    b = enqueue(b , 7)
    print(type(b))
    print(b)    
    b = enqueue(b , 6)
    print(type(b))
    print(b)
    b = enqueue(b , 5)   
    print(type(b))
    print(b)

    print(q_0_to_array(b))

    odebrany, b = dequeue(b)
    #print(q_0_to_array(b))
    print(type(b))
    print(b)
    print(q_2_to_array(b))

    b = enqueue(b , 5)   
    print(type(b))
    print(b)
    print(q_0_to_array(b))    

    print("*************************")
    operations, values = make_random_operations_array(5,10)
    print(operations)
    print(values)

    q_simple = SimpleQueue()
    
    q = QueueZero(None, None, 0)

    do_operations_on_queue(operations, q_simple, values)   # operations and values on simple q
    
    print("simple q is {}".format(q_simple.qlist))
    do_operations_on_queue(operations, q, values) # same operations and values on my q

    print(q)
    print(type(q))
    a = None
    if q.state == 0:
        a = q_0_to_array(q)
    if q.state == 1:
        a = q_1_to_array(q)
    if q.state == 2:
        a = q_2_to_array(q)    
    print(a)        


    

    '''
    p1 = 0 
    p2 = 0
    for x in operations:
        if x:
            p1 +=1
        else:
            p2 +=1
    
    print("operace jsou: {0}".format(operations))
    print("hodnoty jsou: {0}".format(values))
    #print("pridavani "+str(p1))
    #print("odebirani "+str(p2))
    
    q_simple = do_operations_on_queue(operations, q_simple, values)

    #print(q_simple.qlist)

    b = QueueZero(None, None, 0)
    b1 = enqueue(b , 8)
    b2 = enqueue(b1 , 9)
    b3 = enqueue(b2 , 10)
    b4 = enqueue(b3 , 11)

    print(b3) 

    #q_2_to_array(b1)

    #print(q_2_to_array(b1))
    '''

    '''q = QueueZero(None, None, 0)

    operations, values = make_random_operations_array(10,100)
    
    do_operations_on_queue(operations, q_simple, values)   # operations and values on simple q
    do_operations_on_queue(operations, q, values) # same operations and values on my q

    compare_queues(q_simple, q)'''



