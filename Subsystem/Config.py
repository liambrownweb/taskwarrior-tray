'''
Created on Feb 11, 2013

@author: lbrown
'''
import os.path
import Defaults

class ConfigReader(object):
    '''
    classdocs
    '''

    def __init__(self, params = None):
        '''
        Constructor
        '''
    
class Config(object):
    
    _db_name = None
    _home_dir = None
    _config_file = ".gtdhubrc"
    _reader = None
    
    def __init__(self, params = None):
        _reader = ConfigReader(self._config_file)
        return
    
    def getDBName(self):
        if self._db_name is None:
            self._db_name = Defaults.db_name()
        return self._db_name
            
    def getHomeDir(self):
        if self._home_dir is None:
            self._home_dir = Defaults.data_dir()
        return self._home_dir
    
    def saveConfig(self):
        return