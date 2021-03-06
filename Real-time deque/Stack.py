class Stack(object):

    def __init__(self,first,second):
        self.first = first#extra
        self.second = second

    def __str__(self):
        return "first: {} second: {}".format(self.first,self.second)


    def get(self):
        if self.first is None:
            return self.second
        return self.first

        
    def next(self):
        if self.first is None:
            if self.second is None:
                print("stack je prazdny next nedava smysl")
                return None
            return Stack(None, self.second.next)
        if self.first.next is None:
            return Stack(None, self.second)
        return Stack(self.first.next, self.second)

def stack_to_array(stack):

    arr = []
    
    while stack.get() is not None:
        arr.append(stack.get().value)
        stack = stack.next()
        
    return arr

