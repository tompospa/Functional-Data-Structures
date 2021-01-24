from Stack import Stack, stack_to_array
from Element import Element
from RealTimeDeque import Deque_0, Deque_1
from Deque import push_left, push_right, pop_left, pop_right

class MyTests():
    
    def __init__(self):
        pass
    
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


        
