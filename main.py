from __future__ import unicode_literals
import youtube_dl
from general import *
from queue import Queue
from crl_spider import Spider
from crl_domain import *

#Takes in url

playlist_url= input("What is the playlist url?")

#parses the url

print("Parsing url")
if playlist_url.find("list=") != -1:
    print("Finding url division")
    url_division=playlist_url.find("list=")
    playlist_url= playlist_url[url_division:]
    if playlist_url.find("&"):
        url_division = playlist_url.find("&")
        playlist_url = playlist_url[:url_division]
    else:
        print("Invalid_url")
else:
    print("Invalid url")

#This part of the code checks for new items to dowwload

print("Finding new links")

PROJECT_NAME = playlist_url
HOMEPAGE = 'https://www.youtube.com/playlist?'+playlist_url
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 1
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# This part of the code creates the downloaded and to_download data files

create_data_files(playlist_url, playlist_url, "to_download")
create_data_files(playlist_url, playlist_url, "downloaded")

#This part of the code compares the downloaded and queue files to find songs to download

to_download = file_to_set(playlist_url+"/queue.txt").difference(file_to_set(playlist_url+"/downloaded.txt"))
to_download = list(to_download)
to_download = [i for i in to_download if playlist_url in i]
to_download = set(to_download)

# This part of the code saves the to_download file

set_to_file(to_download, playlist_url+"/to_download.txt")

# This part of the sets the download options:

download_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s.',
    'nocheckcertificate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# This part of the code downloads songs

print("Downloading songs")

with youtube_dl.YoutubeDL(download_options) as dl:
    with open(playlist_url+"/to_download.txt", 'r') as f:
        for song_url in f:
            dl.download([song_url])
            append_to_file(playlist_url+"/downloaded.txt", '\n'+song_url)
