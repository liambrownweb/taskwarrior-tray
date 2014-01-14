'''
Created on Feb 12, 2013

@author: Liam Brown
'''

class IllegalArgumentException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value) 

class NoViewException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value) 