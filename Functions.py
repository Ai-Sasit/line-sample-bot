from youtube_search import YoutubeSearch
from pydub import AudioSegment
from pygame import mixer as Mi
from os import remove, rename
from spotdl import Spotdl
import glob as G
import pafy

Mi.init(48000)
Link_Queue = list()
Name_Queue = list()

def MusicPlayDirect(search):
    global Cplay
    if Mi.music.get_busy() == 0:
        print("ไม่มีเพลงเล่น")
        if ("$music_temp.mp3" in G.glob("*.mp3")):
            try: Mi.music.unload()
            except: pass
            finally: remove("$music_temp.mp3")
    else:
        print("มีเพลงเล่นอยู่")
        if ("$music_temp.mp3" in G.glob("*.mp3")):
            raise Exception
    results = YoutubeSearch(search, max_results=1).to_dict()
    result = pafy.new("www.youtube.com" + dict(results[0])["url_suffix"])
    m4a = result.m4astreams[0]
    m4a.download()
    name = G.glob("*.m4a")[0]
    Mp3 = AudioSegment.from_file(name, format="m4a")
    Mp3.export("$music_temp.mp3", format="mp3" , bitrate='256')
    remove(name)
    Mi.music.load("$music_temp.mp3")
    Mi.music.play()
    return result.title

def MusicQueue(search):
    results = YoutubeSearch(search, max_results=1).to_dict()
    url = "www.youtube.com" + dict(results[0])["url_suffix"]
    result = pafy.new(url)
    Link_Queue.append(url)
    Name_Queue.append(result.title)
    return result.title

def PlayQueue():
    if ("$music_temp.mp3" in G.glob("*.mp3")):
        Mi.music.unload()
        remove("$music_temp.mp3")
    Name_Queue.pop(0)
    link = Link_Queue.pop(0)
    result = pafy.new(link)
    m4a = result.m4astreams[0]
    m4a.download()
    name = G.glob("*.m4a")[0]
    Mp3 = AudioSegment.from_file(name, format="m4a")
    Mp3.export("$music_temp.mp3", format="mp3" , bitrate='256')
    remove(name)
    Mi.music.load("$music_temp.mp3")
    Mi.music.play()