from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""

def test_get_all_albums(db_connection):
    db_connection.seed("seeds/music_library_2.sql")
    repository = AlbumRepository(db_connection)

    albums = repository.all()

    assert albums == [
        Album(1,"Doolittle", 1989, 1),
        Album(2,"Surfer Rosa", 1988, 1),
        Album(3,"Waterloo", 1974, 2),
        Album(4,"Super Trouper", 1980, 2),
        Album(5,"Bossanova", 1990, 1),
        Album(6,"Lover", 2019, 3),
        Album(7,"Folklore", 2020, 3),
        Album(8,"I Put a Spell on You", 1965, 4),
        Album(9,"Baltimore", 1978, 4),
        Album(10,"Here Comes the Sun", 1971, 4),
        Album(11,"Fodder on My Wings", 1982, 4),
        Album(12,"Ring Ring", 1973, 2),
    ]

"""
When we call AlbumRepository#find, with an id
We get a single Album object with that id, reflecting the seed data.
"""
def test_get_single_album(db_connection):
    db_connection.seed("seeds/music_library_2.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(7)
    assert album == Album(7, "Folklore", 2020, 3)

"""
When we call AlbumRepository#create
We add a new Account object to the table
"""
def test_create_album_adds_to_table(db_connection):
    db_connection.seed("seeds/music_library_2.sql")
    repository = AlbumRepository(db_connection)
    new_album = Album(None, "Fun Fun Songs", 2022, 3)
    repository.create(new_album)
    assert repository.all() == [
        Album(1,"Doolittle", 1989, 1),
        Album(2,"Surfer Rosa", 1988, 1),
        Album(3,"Waterloo", 1974, 2),
        Album(4,"Super Trouper", 1980, 2),
        Album(5,"Bossanova", 1990, 1),
        Album(6,"Lover", 2019, 3),
        Album(7,"Folklore", 2020, 3),
        Album(8,"I Put a Spell on You", 1965, 4),
        Album(9,"Baltimore", 1978, 4),
        Album(10,"Here Comes the Sun", 1971, 4),
        Album(11,"Fodder on My Wings", 1982, 4),
        Album(12,"Ring Ring", 1973, 2),
        Album(13,"Fun Fun Songs", 2022, 3),
    ]

def test_deleted_album_removes_from_table(db_connection):
    db_connection.seed("seeds/music_library_2.sql")
    repository = AlbumRepository(db_connection)
    new_album = Album(None, "Fun Fun Songs", 2022, 3)
    repository.create(new_album)
    repository.delete(13)
    assert repository.all() == [
        Album(1,"Doolittle", 1989, 1),
        Album(2,"Surfer Rosa", 1988, 1),
        Album(3,"Waterloo", 1974, 2),
        Album(4,"Super Trouper", 1980, 2),
        Album(5,"Bossanova", 1990, 1),
        Album(6,"Lover", 2019, 3),
        Album(7,"Folklore", 2020, 3),
        Album(8,"I Put a Spell on You", 1965, 4),
        Album(9,"Baltimore", 1978, 4),
        Album(10,"Here Comes the Sun", 1971, 4),
        Album(11,"Fodder on My Wings", 1982, 4),
        Album(12,"Ring Ring", 1973, 2),
    ]


