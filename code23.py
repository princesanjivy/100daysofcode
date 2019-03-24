# @princesanjivy
# download youtube videos using
# pip install pytube

from pytube import YouTube
ytlink = input("video link: ")

yt = YouTube(ytlink).streams
yt.first().download()
print("video saved!")

# will be saved in current directory