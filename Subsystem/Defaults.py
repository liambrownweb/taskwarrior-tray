'''
Created on Feb 18, 2013

@author: Liam Brown
'''

import os

def data_dir():
    home = os.getenv('HOME') or os.getenv('USERPROFILE')
    data_subpath = '.gtdhub'
    data_dir = os.path.join(home, data_subpath)
    return data_dir

def db_name():
    return "gtdhub.sqlite"

prog_root_dir = os.path.join(os.path.dirname(__file__), "..")