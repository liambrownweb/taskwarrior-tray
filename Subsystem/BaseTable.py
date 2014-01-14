'''
Created on Feb 12, 2013

@author: Liam Brown
'''
from Subsystem import Exceptions
from datetime import datetime

class BaseObject(object):
    '''
    Generic base object for an individual item in the database.
    '''
    _table = None
    _fields = None

    def __init__(self, date = None):
        '''
        Constructor
        '''
        if self._fields['date'] is None:
            self._fields['date'] = datetime.now()
        else:
            self._fields['date'] = date
    
    def getField(self, field_name = None):
        '''
        Gets a (database) field and returns it
        
        Assuming field_name is specified and it is among the database fields for this
        object, this will grab the field and return its value. Otherwise, it raises
        an illegal argument exception.
        '''
        if field_name is None or not field_name in self._fields.keys():
            raise Exceptions.IllegalArgumentException
        return self._fields[field_name]
    
    def setField(self, field_name = None, value = None):
        '''
        Sets a (database) field and returns it.
        
        Assuming field_name is specified and is among the database fields for this
        object, this will set the field value to whatever is specified by value.
        If value is not specified, the field is not changed.
        returns self, so this method can be chained.
        '''
        if field_name is None or not field_name in self._fields.keys():
            raise Exceptions.IllegalArgumentException
        if value is None:
            return
        self._fields[field_name] = value
        return self

class BaseTable(object):
    _field_defs = None
    _init_data = None
    _table_name = None
    _collection = None