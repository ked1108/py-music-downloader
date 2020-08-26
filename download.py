import spotify_tags as st
import requests
import os
import pafy
import json

def getResults(song, artist):
    r = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&q='+song+'+'+artist+'+official+audio&type=video&key=AIzaSyDtJ0SPTFqIKAidiZxCgjWYfzqkAj_e8Co')
    with open('result.json', 'wb+') as f:
        f.write(r.content)


def parseResults():
    with open('result.json') as f:
        data = json.load(f)
        watchID = data['items'][0]['id']['videoId']
    return watchID


def download(watchID, song, artist):
    audio = pafy.new(watchID)
    best = audio.getbestaudio(preftype='m4a')
    title = os.getenv("USERPROFILE") + r"\Music\\" + audio.title + '.m4a'
    best.download(os.getenv("USERPROFILE") + r"\Music", quiet=True)
    st.search(title, artist, song)
