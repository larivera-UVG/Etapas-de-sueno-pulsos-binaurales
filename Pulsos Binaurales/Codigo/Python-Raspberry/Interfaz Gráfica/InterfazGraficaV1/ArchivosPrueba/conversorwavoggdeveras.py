from pydub import AudioSegment
stringbase = str(100)
##stringbin = 20

song = AudioSegment.from_wav("/home/pi/Desktop/Tesis Luis Guerrero/Binaural0"+".wav")
song.export("/home/pi/Desktop/Tesis Luis Guerrero/qUEREPUTAS"+stringbase+".ogg", format="ogg")
