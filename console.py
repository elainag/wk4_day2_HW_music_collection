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


all_albums = album_repository.select_all()
for album in all_albums:
    print(album.__dict__)

pdb.set_trace()
