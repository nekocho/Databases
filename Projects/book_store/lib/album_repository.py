from lib.album import *

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM albums')
        artists = []
        for row in rows:
            item = Album(row["title"], row["release_year"], row["artist_id"])
            artists.append(item)
        return artists

    def find(self, title):
        rows = self._connection.execute('SELECT * FROM albums WHERE title = %s', [title])
        row = rows[0]
        return Album(row["title"], row["release_year"], row["artist_id"])
    
    def create(self, album):
        self._connection.execute("INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)", 
                    [album.title, album.release_year, album.artist_id])
        return None
    
    def delete(self, title):
        self._connection.execute("DELETE FROM albums WHERE title = %s", [title])
        return None

