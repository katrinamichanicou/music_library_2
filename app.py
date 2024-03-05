import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    albums = album_repository.all()
    return render_template('albums/index.html', albums=albums)

@app.route('/albums/<int:album_id>',methods=['GET'])
def get_one_album(album_id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album = album_repository.find(album_id)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(album.artist_id)
    return render_template('albums/album.html', album=album, artist=artist)

@app.route('/artists/<int:artist_id>', methods=['GET'])
def get_one_artist(artist_id):
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(artist_id)
    return render_template('artists/artist.html', artist=artist)

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    return render_template('artists/index.html', artists=artists)

@app.route('/albums/new', methods=['GET'])
def get_new_album():
    return render_template('albums/new.html')

@app.route('/albums', methods=['POST'])
def  create_album():
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    album = Album(None, title, release_year, artist_id)
    if not album.is_valid():
        return render_template('albums/new.html', album=album, errors=album.generate_errors()), 400
    album = album_repository.create(album)
    return redirect(f"/albums/{album.id}")

@app.route('/artists/new', methods=['GET'])
def get_new_artist():
    return render_template('artists/new.html')

@app.route('/artists', methods=['POST'])
def post_artists():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    artist = Artist(None, name, genre)
    if not artist.is_valid():
        return render_template('artists/new.html', artist=artist, errors=artist.generate_errors()), 400
    artist = artist_repository.create(artist)
    return redirect(f"/artists/{artist.id}")

@app.route('/albums/<int:album_id>/delete', methods=['POST'])
def delete_book(album_id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album_repository.delete(album_id)
    return redirect(url_for('get_albums'))


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
