from mutagen.mp4 import MP4, MP4Cover
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json

cid = 'CID'
secret_id = 'SECRET ID'

client_credentials_manager = SpotifyClientCredentials(client_id = cid, client_secret = secret_id)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def search(file, artist, song):
    results = sp.search(q='artist:{0} track:{1}'.format(artist, song), limit = 1, type="track")
    print("retrieved results!")
    get_details(file, results)


def get_details(file, result):
    details = result["tracks"]["items"][0]
    album = details["album"]["name"]
    title = details["name"]
    images = details["album"]["images"][0]
    image_url = images["url"]

    for a in details["artists"]:
        artist = a["name"]
        break

    image = requests.get(image_url)

    with open("image.png", "wb+") as f:
        f.write(image.content)
    print("got the details!")
    embed(file, title, artist, album)

def embed(file, title, artist, album):
    meta = MP4(file)
    meta['\xa9nam'] = title
    meta['\xa9ART'] = artist
    meta['\xa9alb'] = album
    with open("image.png", "rb+") as f:
        meta['covr'] = [MP4Cover(f.read(), imageformat=MP4Cover.FORMAT_PNG)]
    meta.save()
    print("Done!")
