from typing import Type

class Connection:
    def connect(self):
        print('Connect database')
    
    def disconnect(self):
        print('Disconnect database')

def MysqlRepo(Connection):
    def __init__(self):
        super().__init__()
    
    def select(self):
        self.connect()
        print('SELECT * FROM table')

class UseCase:
    def search(self, db_repo: Type[MysqlRepo]):
        db_repo.select()