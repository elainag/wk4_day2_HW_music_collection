from db.run_sql import run_sql
from models.artist import Artist


def select():
    artists = []
    sql = " SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row["artist_name"], row["id"])
        artists.append(artist)
    return artists


def select(id):
    artist = []
    sql = " SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = Artist(result["artist_name"], result["id"])
    return artist


def save(artist):
    sql = "INSERT INTO artists (artist_name) VALUES (%s) RETURNING *"
    values = [artist.artist_name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    artist.id = id
    return artist


def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)
