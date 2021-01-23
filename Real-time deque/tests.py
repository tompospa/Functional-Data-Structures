from Stack import Stack
from Element import Element

class MyTests():
    
    def __init__(self):
        pass
    
    def stack_test(self):

        first = Element(3, None)

        second = Element(4, None)

        stack = Stack(first, second)
        print("stack: {}".format(stack))

        print("prvni na stacku je {}".format(stack.get()))

        print("dalsi prvek na stacku je {}".format(stack.next()))


        first = None

        second = Element(4, None)

        stack = Stack(first, second)
        print("stack: {}".format(stack))

        print("prvni na stacku je {}".format(stack.get()))

        print("dalsi prvek na stacku je {}".format(stack.next()))
