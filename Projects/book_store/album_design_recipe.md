# {{TABLE NAME}} Model and Repository Classes Design Recipe


## 1. Design and create the Table

Database seed = music_library.sql

## 2. Create Test SQL seeds

Database seed = music_library.sql

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# Model class
# (in lib/album.py)
class Album


# Repository class
# (in lib/album_repository.py)
class AlbumRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# Table name: music_library

# Model class
# (in lib/album.py)

class Album:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.release_year = 0
        self.artist_id = 0



# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> album = Album()
# >>> album.title = "Doolittle"
# >>> album.release_year = 1989
# >>> album.artist_id = 1

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: music_library

# Repository class
# (in lib/album_repository.py)

class AlbumRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, title, release_year, artist_id FROM albums;

        # Returns an array of album objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, title, release_year, artist_id FROM albums WHERE id = $1;

        # Returns a single album object.



    def create(title, release_year, artist_id)
        # Executes the SQL query:
        # INSERT INTO albums (title, release_year, artist_id) VALUES (%s, $1, $1);
        # Creates new album with respective artist ID

    def delete(title)
        # Executes the SQL query:
        # DELETE FROM albums WHERE title = %s'; 
        # Deletes the album with the title given

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all albums

repo = AlbumRepository()

albums = repo.all()

len(albums) # =>  2

albums[0].id # =>  1
albums[0].title # =>  'Doolittle'
albums[0].release_year # => 1989
albums[0].artist_id # => 1

albums[1].id # =>  2
albums[1].title # =>  'Surfer Rosa'
albums[1].release_year # =>  1988
albums[1].artist_id # => 1

# 2
# Get a single album

repo = AlbumRepository()

album = repo.find(1)

album.id # =>  1
album.title # =>  'Doolittle'
album.release_year # =>  1989
album.artist_id # => 1

# 3 
# Create a new album

repo = AlbumRepository()

album = repo.create()

album.title # =>  '1989'
album.release_year # =>  2014
album.artist_id # => 3


# 4
# Delete an album

repo = AlbumRepository()

album = repo.delete()

album.title # =>  '1989'

```


