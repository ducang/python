import pyglet
import time
import datetime
from pyglet.media import Source, Player, load

alarm = int(input("alarm:"))
now = datetime.datetime.now().minute

while True:
  if now == alarm:

    mp3file="music.mp3"
    player = Player()
    source = load(mp3file)
    player.queue(source)        
    player.play()

    while True:
      interact = (input("Play, pause or stop:"))
      if interact == "play":
        player.play()
      elif interact == "pause":
        player.pause()
      elif interact == "stop":
        player.pause()
        break
    break
  else:
    now= datetime.datetime.now().minute

    
