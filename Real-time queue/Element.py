
class Element(object):
    
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return '{} '.format(self.value)
