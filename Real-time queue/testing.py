

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


    operations, values = make_random_operations_array(5,10)
    print("----------------------")
    b = QueueZero(None, None, 0)
    
    b = enqueue(b , 8)
    print(type(b))
    #print(q_2_to_array(b))
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

    b = enqueue(b , 4)
    print(type(b))
    
    print(b)       
    print(q_0_to_array(b))


    pom, b = dequeue(b)
    print(type(b))
    
    print(b)    
    print(q_0_to_array(b))
    
    pom, b = dequeue(b)
    print(type(b))
    
    print(b)  
    print(q_1_to_array(b)) 

    pom, b = dequeue(b)
    print(type(b))
    
    print(b)      

    pom, b = dequeue(b)
    print(type(b))
    
    print(b)    


    pom, b = dequeue(b)
    print(type(b))
    
    print(b)        


    pom, b = dequeue(b)
    print(type(b))
    
    print(b)    

    

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

    




