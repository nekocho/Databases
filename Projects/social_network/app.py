from lib.database_connection import DatabaseConnection
from lib.user_account_repository import *
from lib.post_repository import *



# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")

# Retrieve all artists
user_repository = UserAccountRepository(connection)
post_repository = PostRepository(connection)
user = user_repository.all()
post = post_repository.all()

# List them out
for user in user:
    print(user)

for post in post:
    print(post)
