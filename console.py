import pdb
from models.artist import Artist
import repositories.artist_repository as artist_repository


pdb.set_trace()

artist_1 = Artist("The Foals")
artist_repository.save(artist_1)

artist_2 = Artist("Rufus du sol")
artist_repository.save(artist_2)

# -- INSERT INTO albums ('What went down', 'Indie Rock')
# -- INSERT INTO albums ('Bloom', 'Dance')
