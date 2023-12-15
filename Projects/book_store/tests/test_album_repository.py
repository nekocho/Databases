from lib.album_repository import *
from lib.album import *


def test_get_all_albums(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.all()

    assert album == [
        Album('Doolittle', 1989, 1),
        Album('Surfer Rosa', 1988, 1),
        Album('Waterloo', 1974, 2),
        Album('Super Trouper', 1980, 2),
        Album('Bossanova', 1990, 1),
        Album('Lover', 2019, 3),
        Album('Folklore', 2020, 3),
        Album('I Put a Spell on You', 1965, 4),
        Album('Baltimore', 1978, 4),
        Album('Here Comes the Sun', 1971, 4),
        Album('Fodder on My Wings', 1982, 4),
        Album('Ring Ring', 1973, 2),
    ]

def test_find_single_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find('Waterloo')
    assert album == Album("Waterloo", 1974, 2)

def test_create_single_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album('1989', 2014, 3))

    result = repository.all()
    assert result == [
        Album('Doolittle', 1989, 1),
        Album('Surfer Rosa', 1988, 1),
        Album('Waterloo', 1974, 2),
        Album('Super Trouper', 1980, 2),
        Album('Bossanova', 1990, 1),
        Album('Lover', 2019, 3),
        Album('Folklore', 2020, 3),
        Album('I Put a Spell on You', 1965, 4),
        Album('Baltimore', 1978, 4),
        Album('Here Comes the Sun', 1971, 4),
        Album('Fodder on My Wings', 1982, 4),
        Album('Ring Ring', 1973, 2),
        Album('1989', 2014, 3)
    ]

def test_delete_single_album(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.delete('1989')

    result = repository.all()
    assert result == [
        Album('Doolittle', 1989, 1),
        Album('Surfer Rosa', 1988, 1),
        Album('Waterloo', 1974, 2),
        Album('Super Trouper', 1980, 2),
        Album('Bossanova', 1990, 1),
        Album('Lover', 2019, 3),
        Album('Folklore', 2020, 3),
        Album('I Put a Spell on You', 1965, 4),
        Album('Baltimore', 1978, 4),
        Album('Here Comes the Sun', 1971, 4),
        Album('Fodder on My Wings', 1982, 4),
        Album('Ring Ring', 1973, 2),
    ]