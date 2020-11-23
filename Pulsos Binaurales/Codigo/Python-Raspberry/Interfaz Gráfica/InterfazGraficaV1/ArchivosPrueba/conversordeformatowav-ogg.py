from pydub import AudioSegment

song = AudioSegment.from_wav("/home/pi/Desktop/Tesis Luis Guerrero/Binaural0.wav")
song.export("/home/pi/Desktop/Tesis Luis Guerrero/Exito.ogg", format="ogg")
