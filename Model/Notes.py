'''
Created on Feb 12, 2013

@author: lima
'''
from Subsystem import Exceptions
from Subsystem import BaseTable
from DB import table
        
class NoteTable(BaseTable.BaseTable):
    _table_name = "notes"
    _field_defs = {"date":"datetime",
                   "content":"varchar(512)"}
    
    def __init__(self):  
        self._init_data = table(name = self._table_name, fields = self._field_defs)
        
    def addNote(self, data = None):
        if data is None:
            raise Exceptions.IllegalArgumentException("No note provided to addNote method")
        elif type(data) == Note:
            self._collection.append(data)
        else:
            note = Note(contents = data)
            self._collection.append(note)
            
    def getInitData(self):
        return self._init_data
    
class Note(BaseTable.BaseObject):
    '''
    The internal data structure for inbox notes.
    '''
    _table = NoteTable

    def __init__(self, contents = None, date = None):
        '''
        Constructor
        '''
        if contents is None:
            self._fields = dict((x, None) for x in tuple(NoteTable._field_defs.keys()))
        else:
            self._fields = contents
        super(Note,self).__init__(date)
        
    def getContents(self):
        '''
        returns the contents of the note.
        ''' 
        return self._fields
    
    
    
    def setContents(self, contents):
        '''
        sets new contents for a note.
        
        Parameters
        contents: the new contents for the note.
        '''
        if contents is None:
            raise Exceptions.IllegalArgumentException("contents parameter empty")
        self._contents = contents
