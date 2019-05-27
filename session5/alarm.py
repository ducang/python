import pyglet
import time
import datetime
now= str(datetime.datetime.today().time())
alarm = "19:59:00.000000"
while (now>=alarm):
  music=pyglet.resource.media("music.mp3")
  music.play()
  pyglet.app.run()  
    

        

    
