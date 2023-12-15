from lib.user_account import *

def test_construct_user_account():
    user_account = UserAccount(1, 'bob@bob.com', 'bobtastic')
    assert user_account.id == 1
    assert user_account.email_address == 'bob@bob.com'
    assert user_account.username == 'bobtastic'

def test_equalise_user_account():
    user_account1 = UserAccount(1, 'bob@bob.com', 'bobtastic')
    user_account2 = UserAccount(1, 'bob@bob.com', 'bobtastic')
    assert user_account1 == user_account2

def test_formatting():
    user_account = UserAccount(1, 'bob@bob.com', 'bobtastic')
    assert str(user_account) == "UserAccount(1, bob@bob.com, bobtastic)"