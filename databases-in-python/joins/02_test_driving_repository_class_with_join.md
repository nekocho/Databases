# Test-driving a Repository method with a JOIN

Learn to test-drive "Model" and "Repository" classes to SELECT related records
from the database.

## Demonstration

[This is a bit easier to follow on the
video.](https://youtu.be/PK0fCfHNMR4&t=0s)

## Intro

You've previously learned how to test-drive a method `find` that retrieves a
single record, and return a model object.

To select an artist and all the corresponding albums, we could write the
following code:

```python
# Create our repositories
artist_repository = ArtistRepository(connection)
album_repository = AlbumRepository(connection)

# Get the artist
artist = artist_repository.find(1)

# Get all the albums
albums = album_repository.all()

# And then filter the albums array depending on id of the artist
albums_by_artist = []
for album in albums:
    if album.artist_id == artist.id:
        albums_by_artist.append(album)
```

However this is inefficient because of the N+1 problem mentioned in the previous
section. 

You've learned how to use `JOIN` to select data from two tables in a single
query, to solve this problem. In this section, you'll learn how to build a
method `find_with_****`, that returns a single record, alongside its related
rows in the other table.

For example, we could fetch a single artist, and get its related albums this
way:

```python
repository = ArtistRepository(connection)

# Perfoms a SELECT with a JOIN and returns an Artist object.
# This object also has an attribute .albums, which is an array
# of Album objects.
artist = repository.find_with_albums(1)

artist.id # The ID of the artist: 1

artist.albums # This an array of Album objects
```

We'll need to add the attribute `albums` to the `Artist` class. By default, this
would be an empty array.

```python
# file: lib/artist.py

class Artist():
    def __init__(self, id, name, genre, albums = []):
        self.id = id
        self.name = name
        self.genre = genre
        self.albums = albums
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"
```

Then we'll test-drive, defining the expected behaviour as a test.

```python
# file: tests/test_artist_repository.py
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from lib.album import Album

def test_find_with_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artist = repository.find_with_albums(1)
    assert artist == Artist(1, "Pixies", "Rock", [
        Album(1, "Doolittle", 1989, 1),
        Album(2, "Surfer Rosa", 1988, 1),
        Album(5, "Bossanova", 1990, 1),
    ])

# Note, you'll need to have the `__eq__` method on `Album` for this to work.
```

And then the method implementation:

```python
# file: lib/artist_repository.py
from lib.artist import Artist
from lib.album import Album

class ArtistRepository():
    # ...

    # Find a single artist, along with their albums
    def find_with_albums(self, artist_id):
        rows = self._connection.execute(
            "SELECT artists.id as artist_id, artists.name, artists.genre, albums.id AS album_id, albums.title, albums.release_year " \
            "FROM artists JOIN albums ON artists.id = albums.artist_id " \
            "WHERE artists.id = %s", [artist_id])
        albums = []
        for row in rows:
            album = Album(row["album_id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)

        # Each row has the same id, name, and genre, so we just use the first
        return Artist(rows[0]["artist_id"], rows[0]["name"], rows[0]["genre"], albums)
    
    # ...
```

## Exercise

Use the database `student_directory_2` from the previous section.

If you didn't design and create the tables previously, load the
`student_directory_2.sql` file in manually.

1. Test-drive and implement the three classes for the `students` and `cohorts`
   table.   
  You should end up with three classes:
    * `Student`
    * `Cohort`
    * `CohortRepository` — test-drive the method `find_with_students`.

2. Write a small program in `app.py` using the class `CohortRepository` to print
   out the data of one cohort with its students to the terminal.

<!-- OMITTED -->

## Challenge

Use the database `blog` you created [in this earlier
challenge.](../challenges/06_designing_schema_two_tables.md#challenge)

1. Test-drive and implement the three classes for the `posts` and `comments`
   tables.

2. Write a small program in `app.py` using the class `PostRepository` to print
   out the data of one post with its comments to the terminal.


[Next Challenge](03_using_joins_with_many_to_many.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=joins%2F02_test_driving_repository_class_with_join.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=joins%2F02_test_driving_repository_class_with_join.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=joins%2F02_test_driving_repository_class_with_join.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=joins%2F02_test_driving_repository_class_with_join.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fdatabases-in-python&prefill_File=joins%2F02_test_driving_repository_class_with_join.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
