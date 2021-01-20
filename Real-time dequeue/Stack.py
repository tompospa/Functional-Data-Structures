class Stack(object):

    def __init__(self,first,second):
        self.first = first#extra
        self.second = second

    def __str__(self):
        return "first: {} second: {}".format(self.first,self.second)
