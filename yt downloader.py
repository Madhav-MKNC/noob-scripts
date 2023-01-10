# this program is used for downloading the youtube playlists in mp3 format

from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

playlist = Playlist("https://www.youtube.com/playlist?list=PLyRX3udhFgijHDmSzYY396e3I5FlvT9Kn")

playlist.video_urls
for url in playlist:
    print(url)
    
for vid in playlist.videos:
    print(vid)

for url in playlist:
   YouTube(url).streams.filter(only_audio=True).first().download()