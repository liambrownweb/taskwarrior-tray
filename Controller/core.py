'''
Created on Feb 11, 2013

@author: lima
'''

from Subsystem import Exceptions, Defaults, Config
import subprocess
import os

class DataHub(object):
    '''
    The "hub" for the GTD PIM spider system.
    '''
    _views = None
    _model = None
    _config = None

    def __init__(self, params = None):
        '''
        Constructor
        '''
        self._config = Config.Config()
        self._views = []

    def addView(self, view_object):
        '''
        connects a view object to the controller

        If the view_object is already connected to the controller, the function does nothing.
        '''
        if not view_object in self._views:
            self._views.append(view_object)
            view_object.addController(self)

    def removeView(self, view_object):
        '''
        '''
        if view_object in self._views:
            self._views.remove(view_object)
        else:
            raise Subsystem.Exceptions.NoViewException("This view was not connected to the controller.")

    def store(self, data):
        '''
        Creates an item from the data sent and stores it in the model.

        Expects the input param, data, to be a dictionary containing fields 'type' and 'content'.
        Creates an object whose classname matches 'type' (assuming 'type' is a valid DB object type in the model)
        and passes it to the model's store() method.
        '''
        item = data['type']()
        '''self._model.store(item)'''
        return subprocess.check_output(["task", "add", data['contents']])

    def retrieve(self, data):
        object = Notes.Note(data)
