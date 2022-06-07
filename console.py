import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


artist_1 = Artist("The Foals")
artist_repository.save(artist_1)

artist_2 = Artist("Rufus du sol")
artist_repository.save(artist_2)


album_1 = Album("What Went Down", "Inide Rock", artist_1)
album_repository.save(album_1)

album_2 = Album("Bloom", "Dance", artist_2)
album_repository.save(album_2)


delete_albums = album_repository.delete_all()

delete_artists = artist_repository.delete_all()


find_album = album_repository.select(7)

all_albums = album_repository.select_all()
for album in all_albums:
    print(album.__dict__)


find_artist = artist_repository.select(1)

all_artists = artist_repository.select_all()
for artist in all_artists:
    print(artist.__dict__)


find_artists_albums = album_repository.list_albums_by_artist(1)


pdb.set_trace()
