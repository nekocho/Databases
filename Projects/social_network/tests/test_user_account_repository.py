from lib.user_account import *
from lib.user_account_repository import *

def test_get_all_user_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)

    result = repository.all()
    assert result == [
        UserAccount(1, 'bobby@ymail.com', 'bobasaurus'),
        UserAccount(2, 'cassie@boxmail.com', 'cassiethesloth'),
        UserAccount(3, 'lizzierocks@rmail.com', 'lizzierocks')
    ]

def test_find_user_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)  

    result = repository.find(1)

    assert result == UserAccount(1, 'bobby@ymail.com', 'bobasaurus')

def test_create_user_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection) 

    repository.create(UserAccount(4, 'andy@ymail.com', 'andyyyy'))

    result = repository.all()
    assert result == [
        UserAccount(1, 'bobby@ymail.com', 'bobasaurus'),
        UserAccount(2, 'cassie@boxmail.com', 'cassiethesloth'),
        UserAccount(3, 'lizzierocks@rmail.com', 'lizzierocks'),
        UserAccount(4, 'andy@ymail.com', 'andyyyy')
    ]

def test_delete_user_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)

    repository.delete(2)

    result = repository.all()

    assert result == [
        UserAccount(1, 'bobby@ymail.com', 'bobasaurus'),
        UserAccount(3, 'lizzierocks@rmail.com', 'lizzierocks')
    ]

def test_update_user_account(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)

    user = repository.find(1)
    user.email_address = 'bobby@gmail.com'
    repository.update(user)

    result = repository.all()
    assert result == [
        UserAccount(1, 'bobby@gmail.com', 'bobasaurus'),
        UserAccount(2, 'cassie@boxmail.com', 'cassiethesloth'),
        UserAccount(3, 'lizzierocks@rmail.com', 'lizzierocks'),
    ]