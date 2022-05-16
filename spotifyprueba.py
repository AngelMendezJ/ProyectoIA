from hmac import trans_36
from unittest import result
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
import pprint
import webbrowser
import pyautogui
import time

client_id = "5ef6339bf8424873900df12dc10e3b62"
client_secret = "7321cb422d0549488410ed879b7bd040"
author = 'Odyssey'
song = "Resonance"

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
result = sp.search(author)

for i in range(0, len(result["tracks"]["items"])):
    name_song = result["tracks"]["items"][i]["name"]
    if song == name_song:
        webbrowser.open(result["tracks"]["items"][i]["uri"])