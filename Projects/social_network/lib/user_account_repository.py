from lib.user_account import *

class UserAccountRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM user_accounts ORDER BY id ASC')
        useraccount = []
        for row in rows:
            item = UserAccount(row['id'], row['email_address'], row['username'])
            useraccount.append(item)
        return useraccount
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * FROM user_accounts WHERE id = %s', [id])
        row = rows[0]
        return UserAccount(row['id'], row['email_address'], row['username'])
    
    def create(self, useraccount):
        self._connection.execute(
            'INSERT INTO user_accounts(id, email_address, username) VALUES(%s, %s, %s)', [useraccount.id, useraccount.email_address, useraccount.username]
        )
        return None
    
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM user_accounts WHERE id = %s', [id]
        )
        return None
    
    def update(self, useraccount):
        self._connection.execute(
            'UPDATE user_accounts SET email_address = %s, username = %s WHERE id = %s', [useraccount.email_address, useraccount.username, useraccount.id]
            )
        return None