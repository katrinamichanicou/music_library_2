from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
GET /albums
Returns a list of albums as an HTML page
"""
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library_2.sql")
    page.goto(f"http://{test_web_address}/albums")
    h1_tag = page.locator("h1")
    li_tag = page.locator("li")
    expect(h1_tag).to_have_text("Albums")
    expect(li_tag).to_have_text([
        '\nTitle: Doolittle\nReleased: 1989\n', 
        '\nTitle: Surfer Rosa\nReleased: 1988\n', 
        '\nTitle: Waterloo\nReleased: 1974\n', 
        '\nTitle: Super Trouper\nReleased: 1980\n', 
        '\nTitle: Bossanova\nReleased: 1990\n', 
        '\nTitle: Lover\nReleased: 2019\n', 
        '\nTitle: Folklore\nReleased: 2020\n', 
        '\nTitle: I Put a Spell on You\nReleased: 1965\n', 
        '\nTitle: Baltimore\nReleased: 1978\n', 
        '\nTitle: Here Comes the Sun\nReleased: 1971\n', 
        '\nTitle: Fodder on My Wings\nReleased: 1982\n', 
        '\nTitle: Ring Ring\nReleased: 1973\n' 
        ])

"""
GET /albums/id
with parameter of id = 3
Returns the Title, Release year and artist for that id
"""
def test_get_one_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library_2.sql")
    page.goto(f"http://{test_web_address}/albums/3")
    title_tag = page.locator(".t-title")
    release_year_tag = page.locator(".t-release-year")
    artist_tag = page.locator(".t-artist")
    expect(title_tag).to_have_text("Waterloo")
    expect(release_year_tag).to_have_text("\nReleased: 1974\n")
    expect(artist_tag).to_have_text("\nArtist: ABBA\n")

"""
GET /artists
with a parameter of id = 1
Returns the name and genre for the artist with id 1
"""
def test_get_one_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library_2.sql")
    page.goto(f"http://{test_web_address}/artists/1")
    h1_tag = page.locator("h1")
    h3_tag = page.locator("h3")
    expect(h1_tag).to_have_text("Artist: Pixies")
    expect(h3_tag).to_have_text("Genre: Rock")

"""
GET /artists
Returns a list of artists
"""
def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library_2.sql")
    page.goto(f"http://{test_web_address}/artists")
    h1_tag = page.locator("h1")
    div_tag = page.locator("div")
    expect(h1_tag).to_have_text("Artists")
    expect(div_tag).to_have_text([
        '\n1. Pixies\n',
        '\n2. ABBA\n',
        '\n3. Taylor Swift\n',
        '\n4. Nina Simone\n'
    ])

"""
When we create a new album
We see it in the albums index
"""
def test_create_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library_2.sql")
    page.goto(f"http://{test_web_address}/albums")

    # This time we click the link with the text 'Add a new album'
    page.click("text=Add a new album")

    # Then we fill out the field with the name attribute 'title'
    page.fill("input[name='title']", "Wild is the Wind")

    # And the field with the name attribute 'release_year'
    page.fill("input[name='release_year']", "1966")

    # And the field with the name attribute 'artist_id'
    page.fill("input[name='artist_id']", "4")

    # Finally we click the button with the text 'Create Album'
    page.click("text=Create Album")

    # Just as before, the virtual browser acts just like a normal browser and
    # goes to the next page without us having to tell it to.

    title_element = page.locator(".t-title")
    expect(title_element).to_have_text("Wild is the Wind")

    release_year_element = page.locator(".t-release-year")
    expect(release_year_element).to_have_text("Released: 1966")

    artist_element = page.locator(".t-artist")
    expect(artist_element).to_have_text("Artist: Nina Simone")

"""
If we create a new album without a title, release year or artist id
We see an error message
"""
def test_create_album_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library_2.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.click("text=Create Album")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Title can't be blank, Release Year can't be blank, Artist id can't be blank")

"""
When we create a new artist
We see it in the artists index
"""
def test_create_artist(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library_2.sql")
    page.goto(f"http://{test_web_address}/artists")

    page.click("text=Add a new artist")
    page.fill("input[name='name']", "Beyonce")
    page.fill("input[name='genre']", "Pop")
    page.click("text=Create Artist")

    artist_element = page.locator(".t-artist")
    expect(artist_element).to_have_text("Artist: Beyonce")

    genre_element = page.locator(".t-genre")
    expect(genre_element).to_have_text("Genre: Pop")

"""
If we create a new artist without a name or genre
We see an error message
"""
def test_create_artist_error(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library_2.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text=Add a new artist")
    page.click("text=Create Artist")
    errors = page.locator(".t-errors")
    expect(errors).to_have_text("There were errors with your submission: Name can't be blank, Genre can't be blank")

"""
When we delete an album
We no longer see it in the albums index
"""
def test_delete_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library_2.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Title: Ring Ring")
    page.click("text=Delete Album")
    list_items = page.locator("li")
    expect(list_items).to_have_text([
        '\nTitle: Doolittle\nReleased: 1989\n', 
        '\nTitle: Surfer Rosa\nReleased: 1988\n', 
        '\nTitle: Waterloo\nReleased: 1974\n', 
        '\nTitle: Super Trouper\nReleased: 1980\n', 
        '\nTitle: Bossanova\nReleased: 1990\n', 
        '\nTitle: Lover\nReleased: 2019\n', 
        '\nTitle: Folklore\nReleased: 2020\n', 
        '\nTitle: I Put a Spell on You\nReleased: 1965\n', 
        '\nTitle: Baltimore\nReleased: 1978\n', 
        '\nTitle: Here Comes the Sun\nReleased: 1971\n', 
        '\nTitle: Fodder on My Wings\nReleased: 1982\n', 
        ])
