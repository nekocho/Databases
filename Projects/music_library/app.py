from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):
    artist_repository = ArtistRepository(self._connection)
    artists = artist_repository.all()

    album_repository = AlbumRepository(self._connection)
    albums = album_repository.all()

    print("Welcome to the music library manager!")

    print("What would you like to do?")
    print('1 - List all albums')
    print('2 - List all artists')
    inp = int(input("Enter your choice:"))
    if inp == 1:
        print('Here is a list of artists:')
        for artist in artists:
            print(f"{artist.id}: {artist.name} ({artist.genre})")
    if inp == 2:
        print('Here is a list of albums:')
        for album in albums:
            print(f"{album.id}: {album.title} ({album.release_year} {album.artist_id})")

if __name__ == '__main__':
    app = Application()
    app.run()