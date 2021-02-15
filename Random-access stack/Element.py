class Element(object):
    
    def __init__(self, value, index, next, jump):
        self.value = value
        self.index = index
        self.next = next
        self.jump = jump



    def __str__(self):
        return '{} '.format(self.value)
