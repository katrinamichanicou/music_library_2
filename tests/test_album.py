from lib.album import Album

"""
Album constructs with an id, name and genre
"""
def test_album_constructs():
    album = Album(1, "Test Title", 2022, 1)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 2022
    assert album.artist_id == 1

"""
We can format albums to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Test Title", 2022, 1)
    assert str(album) == "Album(1, Test Title, 2022, 1)"

"""
We can compare two identical albums
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Test Title", 2022, 1)
    album2 = Album(1, "Test Title", 2022, 1)
    assert album1 == album2

"""
We can assess an album for validity
"""
def test_album_validity():
    assert Album(1, "", "", "").is_valid() == False
    assert Album(1, "Title", "", "").is_valid() == False
    assert Album(1, "", 2001, "").is_valid() == False
    assert Album(1, "", "", 1).is_valid() == False
    assert Album(1, "", 2001, 1).is_valid() == False
    assert Album(1, "Title", "", 1).is_valid() == False
    assert Album(1, "Title", 2001, "").is_valid() == False
    assert Album(1, None, None, None).is_valid() == False
    assert Album(1, "Title", None, None).is_valid() == False
    assert Album(1, None, 2001, None).is_valid() == False
    assert Album(1, None, None, 1).is_valid() == False
    assert Album(None, None, 2001, 1).is_valid() == False
    assert Album(None, "Title", None, 1).is_valid() == False
    assert Album(None, "Title", 2001, None).is_valid() == False
    assert Album(1, "Title", 2001, 1).is_valid() == True
    assert Album(None, "Title", 2001, 1).is_valid() == True

"""
We can generate errors for an invalid album
"""
def test_album_errors():
    assert Album(1, "", "", "").generate_errors() == "Title can't be blank, Release Year can't be blank, Artist id can't be blank"
    assert Album(1, "Title", "", "").generate_errors() == "Release Year can't be blank, Artist id can't be blank"
    assert Album(1, "", 2001, "").generate_errors() == "Title can't be blank, Artist id can't be blank"
    assert Album(1, "", "", 1).generate_errors() == "Title can't be blank, Release Year can't be blank"
    assert Album(1, "", 2001, 1).generate_errors() == "Title can't be blank"
    assert Album(1, "Title", "", 1).generate_errors() == "Release Year can't be blank"
    assert Album(1, "Title", 2001, "").generate_errors() == "Artist id can't be blank"
    assert Album(1, None, None, None).generate_errors() == "Title can't be blank, Release Year can't be blank, Artist id can't be blank"
    assert Album(1, "Title", None, None).generate_errors() == "Release Year can't be blank, Artist id can't be blank"
    assert Album(1, None, 2001, None).generate_errors() == "Title can't be blank, Artist id can't be blank"
    assert Album(1, None, None, 1).generate_errors() == "Title can't be blank, Release Year can't be blank"
    assert Album(None, None, 2001, 1).generate_errors() == "Title can't be blank"
    assert Album(None, "Title", None, 1).generate_errors() == "Release Year can't be blank"
    assert Album(None, "Title", 2001, None).generate_errors() == "Artist id can't be blank"
    assert Album(1, "Title", 2001, 1).generate_errors() == None
    assert Album(None, "Title", 2001, 1).generate_errors() == None