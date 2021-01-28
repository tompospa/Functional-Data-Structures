from Stack import Stack, stack_to_array
from Element import Element
from RealTimeDeque import Deque_0, Deque_1
from Deque import push_left, push_right, pop_left, pop_right
import random
import copy

class MyTests():
    
    def __init__(self):
        pass
    
    def check_realtimeDQ(self, real_time_deque, simple_deque, number_of_operation_for_testing):
        
        number_of_operations = number_of_operation_for_testing
        operations = []
        values = []

        #vytvoření pole operací a pole prvků pro přídání
        for _ in range(number_of_operations):
            choice = random.choice([1, 2, 3, 4]) # 1,2 -> push left right ......  3,4 -> pop left right
            operations.append(choice)
            if choice == 1 or choice == 2:
                values.append(random.randint(0,50))    

        #samotné testování
        for x in operations:
            if x == 1:#push left
                real_time_deque = push_left(values[0], real_time_deque)
                simple_deque = push_left(values[0], simple_deque)
                values.pop(0)
                #print(real_time_deque)
                #print(simple_deque.list)                   
            if x == 2:#push right
                real_time_deque = push_right(values[0], real_time_deque)
                simple_deque = push_right(values[0], simple_deque)
                #print(real_time_deque)
                #print(simple_deque.list)                   
                values.pop(0)        
            if x == 3:#pop left
    
                pom1 = real_time_deque
                pom2 = copy.deepcopy(simple_deque)
                v1, real_time_deque = pop_left(real_time_deque)
                v2, simple_deque = pop_left(simple_deque)
                #print(real_time_deque)
                #print(simple_deque.list)                  
                if v1 != v2:
                    #print("pred realtime: {} ".format(pom1))
                    #print("pred simple: {} ".format(pom2.list))
                    #print("rt vraci: {} simple vraci: {}".format(v1,v2))
                    #print(real_time_deque)
                    #print(simple_deque.list)                    
                    return False        
            if x == 4:#pop right
        
                pom1 = real_time_deque
                pom2 = copy.deepcopy(simple_deque)                
                v1, real_time_deque = pop_right(real_time_deque)
                v2, simple_deque = pop_right(simple_deque)
                #print(real_time_deque)
                #print(simple_deque.list)                  
                if v1 != v2:
                    #print("pred realtime: {} ".format(pom1))
                    #print("pred simple: {} ".format(pom2.list))                    
                    #print("rt {} simple {}".format(v1,v2))
                    #print(real_time_deque)
                    #print(simple_deque.list)
                    return False                     

        return True

    def stack_test(self):

        print("STACK TEST")
        print("----------------------------------------------------")        
        first = Element(3, None)

        second = Element(4, None)

        stack = Stack(first, second)
        print("stack: {}".format(stack))

        print("prvni na stacku je {}".format(stack.get()))

        print("dalsi prvek na stacku je {}".format(stack.next()))

        print(stack_to_array(stack))


        first = None

        second = Element(4, None)

        stack = Stack(first, second)
        print("stack: {}".format(stack))

        print("prvni na stacku je {}".format(stack.get()))

        print("dalsi prvek na stacku je {}".format(stack.next()))

        print(stack_to_array(stack))
        print("----------------------------------------------------")        



    def deque_1_test(self):
        print("DEQUE 1 TEST")
        print("----------------------------------------------------")
        LHS = Stack(Element(1,None), Element(2,None))

        RHS = Stack(Element(4,None), Element(3,None))

        x1 = Deque_1(LHS,RHS,2,2)

        print("{} -> {} ....... {} <- {}".format(x1.LHS.get().value, x1.LHS.next().get().value, x1.RHS.next().get().value, x1.RHS.get().value ))


        x2 = push_left(8, x1)

        print(x2)

        x2 = push_right(8, x1)

        print(x2)        

        #-----------
        v, x2 = pop_right(x1)
        print(x2)      


        v, x2 = pop_right(x2)
        print(x2)               

        v, x2 = pop_right(x2)
        print(x2)     

        v, x2 = pop_right(x2)
        print(x2)      


        v, x2 = pop_right(x2)
        print(x2)

        #-----------
        v, x2 = pop_left(x1)
        print(x2)      
        x2 = push_right(8, x2)

        v, x2 = pop_left(x2)
        print(x2)               

        v, x2 = pop_left(x2)
        print(x2)     

        v, x2 = pop_left(x2)
        print(x2)      

        v, x2 = pop_left(x2)
        print(x2)                                


        print("----------------------------------------------------")


        
