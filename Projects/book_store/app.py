from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
# for artist in artists:
#     print(artist)


artists = artist_repository.find(1)
print(artists)

