'''
Created on Feb 10, 2013

@author: Liam Brown
'''
import sqlite3, os

class table(object):
    _name = None
    _field_defs = None
    
    def __init__(self, name, fields):
        self._name = name
        self._fields = fields
    
class entry():
    _name=None

class DB(object):
    _db_name = None
    def create(self, query):
        raise Exception.NotImplementedException()
    
    def initialize(self):
        import DBStructure
        for current_table in DBStructure.Default:
            self.create(current_table)

class SQLite(DB):
    
    def __init__(self, database_path, new_database):
        self._db_name = database_path
        if (new_database):
            self.initialize()
        
    def create(self, table, delete_first = False):
        table_name = table._table_name
        field_list = ["id integer primary key autoincrement"]
        for current in table._field_defs:
            field_list.append(current + " " + table._field_defs[current])
        if (delete_first):
            drop_query = "DROP TABLE `" + table_name + "`"
            self.query(drop_query)
        field_spec = ", ".join(field_list)
        create_query = "CREATE TABLE " + table_name + "(" + field_spec + ")"
        self.query(create_query)
        
    def query(self, query):
        with sqlite3.connect(self._db_name) as connection:
            cur = connection.cursor()
            return cur.execute(query)
        
    def retrieve(self, table, search_criteria = None):
        retrieve_query = "SELECT * FROM `" + table +"`"
        if not search_criteria is None:
            retrieve_query += " WHERE " + search_criteria
        cursor = self.query(retrieve_query)
        return cursor.fetchall()
    
    def store(self, new_object):
        table = new_object._table
        table_name = table._table_name
        field_names_list = []
        field_values_list = []
        for current in new_object._fields:
            field_names_list.append("`" + current + "`")
            field_values_list.append("'" + str(new_object._fields[current]) + "'")
        field_names = ", ".join(field_names_list)
        field_values = ", ".join(field_values_list)
        store_query = "INSERT INTO " + table_name + "(" + field_names + ") VALUES (" + field_values + ")" 
        self.query(store_query)

def openDB(data=[]):
    model = None
    new_database = not os.path.exists(data['dbfilename']) and not os.path.isfile(data['dbfilename'])
    if (data['type']=='sqlite'):
        model = SQLite(data['dbfilename'], new_database)
    return model