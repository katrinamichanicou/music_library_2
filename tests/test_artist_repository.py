from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library_2.sql") # Seed our database with some test data
    repository = ArtistRepository(db_connection) # Create a new ArtistRepository

    artists = repository.all() # Get all artists

    # Assert on the results
    assert artists == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
    ]

"""
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_library_2.sql")
    repository = ArtistRepository(db_connection)

    repository.create(Artist(None, "Wild Nothing", "Indie"))

    result = repository.all()
    assert result == [
        Artist(1, "Pixies", "Rock"),
        Artist(2, "ABBA", "Pop"),
        Artist(3, "Taylor Swift", "Pop"),
        Artist(4, "Nina Simone", "Jazz"),
        Artist(5, "Wild Nothing", "Indie"),
    ]

"""
When we call ArtistRepository#find with an artist.id
We get the Artist details
"""

def test_find_artist(db_connection):
    db_connection.seed("seeds/music_library_2.sql")
    repository = ArtistRepository(db_connection)
    assert repository.find(2) == Artist(2, "ABBA", "Pop")
    