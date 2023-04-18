"""Python serial number generator."""
from random import randint

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """



    def __init__(self, start=0):
        """ Make a new serial generator starting at start """
        self.start = self.next = start
    
    def __repr__(self):
        """ Show Representation """
        return f'<SerialGenerator Start = {self.start} next = {self.next}>'
    
    def generate(self):
        """ Return next serial """
        self.next += 1 
        return self.next -1
    
    def reset(self):
        """ Reset number to original start """

        self.next = self.start

    

    



