import re
import sys
import datetime
from database import Database

class Model:
    ### CLASSE PAI DOS MODELOS DE TABELA ###
    db = Database()
    id = 0

    def __init__(self) -> None:
        print('model constructor')


    def create(self, data):
        # VALIDATE INPUT DATA
        self.__validatingData(data=data)
        # ADD THE TIMESTAMP DO DATA TO INSERT
        dataToInsert = self.__addTimeStamp(data)

        try:

            cursor = self.db.getCursor()
            cursor.execute(f'INSERT INTO {self.__getTable()} ({self.__getAttr()}) VALUES ({self.__getPlaceholderAttr()})', dataToInsert)
            self.__setId(cursor.lastrowid)
            self.db.store()

        except Exception as err:

            print(f'exception found: {err}')
            sys.exit()


    def all(self, attr='*'):

        cursor = self.db.getCursor()
        cursor.execute(f"SELECT {attr} FROM {self.__getTable()}")
        return cursor.fetchall()


    def findByName(self, name):

        cursor = self.db.getCursor()
        cursor.execute(f'SELECT id FROM {self.__getTable()} WHERE nome = "{name}"')

        id = self.__trim(cursor.fetchone())

        if id:
            return id
        else:
            return False


    def find(self, id):
        cursor = self.db.getCursor()
        cursor.execute(f'SELECT nome from {self.__getTable()} WHERE id = "{id}"')

        nome = cursor.fetchone()
        return self.__cleanData(nome)

    # GETTER

    def getId(self):
        return self.id

    # GETTER

    # PRIVATE METHODS #

    def __getTable(self):
        return self.table

    def __getAttr(self):
        attr =  ','.join(str(item) for item in self.attr)
        #timestamp add
        return attr + ',created_at,updated_at'

    def __getPlaceholderAttr(self):
        placeholder_attr = ', '.join(['%s' for item in self.attr])
        #adding timestamp
        return placeholder_attr + ",%s, %s"

    def __validatingData(self, data):

        if len(data) == 0:
            print("Data cannot be empty")
            sys.exit()

        elif len(data) < len(self.attr):
            print("Data has not all attrbutes")
            sys.exit()

    def __addTimeStamp(self,data):
        now = datetime.datetime.now()
        return data + (now, now)

    def __setId(self, id):
        self.id = id

    def __trim(self, data):
        return re.sub("[^0-9]","", f"{data}")

    def __cleanData(self, data):
        return data[0]
    # PRIVATE METHODS #