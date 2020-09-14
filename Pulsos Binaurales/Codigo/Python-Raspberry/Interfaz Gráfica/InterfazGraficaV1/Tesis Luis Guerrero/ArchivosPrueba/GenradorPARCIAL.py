# -*- coding: utf-8 -*-

import numpy as np
import scipy.io.wavfile as wavfile
import time, sys
import pygame
from pygame import mixer



""" 

Adaptacion del codigo realizado por Jose Pablo Muñoz, para la Raspberry Pi
Luis Guerrero 2020
""" 

#------------------------------------------------------------------------------
"""
Esta función genera pulsos binaurales al ingresar los siguientes parámetros:
basefreq: Frecuencia central de los pulsos
samplerate: Frecuencia de muestreo del archivo .WAV, por lo general se utliza 44100 muestras/segundo
binfreq: Frecuencia de los pulsos binaurales, esta frecuencia es la resta de las frecuencias 
que irán en cada canal. Esta frecuencia se le suma a la frecuencia de basefreq para crear la
segunda frecuenica. 
duration: Duración que tendrá el archivo en segundos.
samplecounter: Se utiliza para identificar el archivo de audio creado, puede ser cualquier número. 

Ej:
binauralgenerator(200,44100,20,10,0)
"""
def binauralgenerator (basefreq,samplerate,binfreq,duration,samplecounter):
    datos=[]
    sr = int(samplerate)
    basefreq = float(basefreq)
    per1 = 1/basefreq
    N1 = sr*per1
    N1 = round(N1)
    N1 = int(N1)
    x1 = np.arange(N1)
    y1 = 4/np.pi*np.sin(2*np.pi*x1/N1)
    numper1 = (duration*sr)/(N1) 
    numper1 = round(numper1)
    numper1 = int(numper1)
    y1 = np.tile(y1,numper1)
    y1 = y1/max(y1)
    y1 = y1.tolist()
    
    binfreq = float(binfreq)
    frectono = basefreq+binfreq
    per2 = 1/frectono
    N2 = per2*sr
    N2 = round(N2)
    N2 = int(N2)
    x2 = np.arange(N2)
    y2 = 4/np.pi*np.sin(2*np.pi*x2/N2)
    numper2 = (duration*sr)/(N2)  
    numper2 = round(numper2)
    numper2 = int(numper2)
    y2 = np.tile(y2,numper2)
    y2 = y2/max(y2)
    y2 = y2.tolist()    
        
    a = len(y1)-len(y2)
    if (a>0):
        for jnp.array(y2): 
    elif (a<0):
        for j in range(abs(a)):
            y2.pop()
        y2 = np.array(y2)
        y1 = np.array(y1) 
    
    for i in range (len(y1)): 
        filas = []
        filas.append(y1[i])
        filas.append(y2[i])
        datos.append(filas)
    y = np.array(datos) 
    y = np.float32(y) 
    samplecounter=str(samplecounter)
    filename = "Binaural"+samplecounter+".wav"
    wavfile.write(filename,sr,y)
    return filename, y in range(a):
            y1.pop()
        y1 = np.array(y1)
        y2 = np.array(y2) 
    elif (a<0):
        for j in range(abs(a)):
            y2.pop()
        y2 = np.array(y2)
        y1 = np.array(y1) 
    
    for i in range (len(y1)): 
        filas = []
        filas.append(y1[i])
        filas.append(y2[i])
        datos.append(filas)
    y = np.array(datos) 
    y = np.float32(y) 
    samplecounter=str(samplecounter)
    filename = "Binaural"+samplecounter+".wav"
    wavfile.write(filename,sr,y)
    return filename, y


"/home/pi/Desktop/Tesis Luis Guerrero/Binaural0.wav"
#------------------------------------------------------------------------------
def playbinaural(filename):
    pygame.init()
    sonido  = pygame.mixer.Sound(filename)
    sonido.play()
    
    
    

#------------------------------------------------------------------------------

------------------------------------------------------------------------   
