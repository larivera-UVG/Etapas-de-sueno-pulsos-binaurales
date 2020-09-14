import tkinter as tk
from PIL import ImageTk,Image
import pygame
from pygame import mixer
from tkinter import filedialog
import numpy as np
import scipy.io.wavfile as wavfile
from pydub import AudioSegment
import pygame.time



class Main(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        
        
        container.pack(side = "top", fill = "both" , expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (MainMenu,AudioPage,SubMenu,GeneratingPage):
            
            frame = F(container,self)
            
            self.frames[F] = frame
            
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame(GeneratingPage)
        
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
        

        
        


        
class MainMenu(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        global render,boton, botonoffmain,botonbrightnessmain
        self.configure(bg= "#13254a")
        
        load = Image.open('boton-05.png')
        render = ImageTk.PhotoImage(load)
        image = tk.Label(self, image = render)
        image.pack()
        image.place(x = 318, y = 200)
        
        
        
        boton = tk.PhotoImage(file = 'boton-01v290px.png')
        b = tk.Button( self , image = boton, borderwidth = 0,
                       command = lambda:controller.show_frame(SubMenu))
        b.pack()
        b.place(x = 915, y = 600)
        
        
        botonoffmain =  tk.PhotoImage(file = 'boton-0330px2.png')
        b2 = tk.Button(self, image = botonoffmain , borderwidth = 0)#falta comando para el boton de apagado
        b2.pack()
        b2.place(x = 1800, y = 10)
        
        botonbrightnessmain = tk.PhotoImage(file = 'boton v2-0430px.png')
        b3 = tk.Button(self, image = botonbrightnessmain , borderwidth = 0)#falta comando para el boton de brightness
        b3.pack()
        b3.place(x = 1750, y = 10)
        
class SubMenu(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        global labelreproduccion, labelgeneracion, btnbackward, btnoff2, btnbrightness2
        self.configure(bg= "#13254a")
        
        labelgeneracion = tk.PhotoImage(file = 'botones-08.png')
        bsub = tk.Button( self , image = labelgeneracion, borderwidth = 0,
                       command = lambda:controller.show_frame(GeneratingPage))
        bsub.pack()
        bsub.place(x = 598, y = 300)
        
        labelreproduccion = tk.PhotoImage(file = 'botones-09.png')
        bsub2 = tk.Button( self , image = labelreproduccion, borderwidth = 0,
                       command = lambda:controller.show_frame(AudioPage))
        bsub2.pack()
        bsub2.place(x = 521, y = 500)
        
        btnoff2 =  tk.PhotoImage(file = 'boton-0330px2.png')
        b4 = tk.Button(self, image = btnoff2 , borderwidth = 0)#falta comando para el boton de apagado
        b4.pack()
        b4.place(x = 1800, y = 10)
        
        btnbrightness2 = tk.PhotoImage(file = 'boton v2-0430px.png')
        b5 = tk.Button(self, image = btnbrightness2 , borderwidth = 0)#falta comando para el boton de brightness
        b5.pack()
        b5.place(x = 1750, y = 10)
        
        btnbackward = tk.PhotoImage(file = 'botones-0650px.png')
        b6 = tk.Button(self, image = btnbackward , borderwidth = 0,
                       command = lambda:controller.show_frame(MainMenu))#falta comando para el boton de brightness
        b6.pack()
        b6.place(x = 20, y = 950)
    
        
class GeneratingPage(tk.Frame):
    
    
        
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        global btnoff4, btnbrightness4, btnbackward3, labelgeneracion2, entradafrecuenciacentral, entradafrecuenciapulsobinaural
        self.configure(bg= "#13254a")
        self.samplerate = 44100
        self.duration = 10
        self.samplecounter = 0
        
        
        btnoff4 =  tk.PhotoImage(file = 'boton-0330px2.png')
        b10 = tk.Button(self, image = btnoff2 , borderwidth = 0)#falta comando para el boton de apagado
        b10.pack()
        b10.place(x = 1800, y = 10)
        
        btnbrightness4 = tk.PhotoImage(file = 'boton v2-0430px.png')
        b11 = tk.Button(self, image = btnbrightness2 , borderwidth = 0)#falta comando para el boton de brightness
        b11.pack()
        b11.place(x = 1750, y = 10)
        
        btnbackward3 = tk.PhotoImage(file = 'botones-0650px.png')
        b12 = tk.Button(self, image = btnbackward , borderwidth = 0,
                       command = lambda:controller.show_frame(SubMenu))#falta comando para el boton de brightness
        b12.pack()
        b12.place(x = 20, y = 950)
        
        entradafrecuenciacentral = tk.Text(self,width = 4,height = 1, font = ("Courier",40), bg = "#ffffff", fg = "#13254a")
        entradafrecuenciacentral.pack()
        entradafrecuenciacentral.place(x = 900, y = 250)
        
        labelfrecuenciacentral = tk.Label(self, text = "Frecuencia central de pulsos (Hz):", font = ("Courier",40), bg = "#13254a", fg = "#ffffff" )
        labelfrecuenciacentral.pack()
        labelfrecuenciacentral.place(x = 400, y = 175)
        
        entradafrecuenciapulsobinaural = tk.Text(self,width = 4,height = 1, font = ("Courier",40), bg = "#ffffff", fg = "#13254a")
        entradafrecuenciapulsobinaural.pack()
        entradafrecuenciapulsobinaural.place(x = 900, y = 475)
        
        labelpulsobinaural = tk.Label(self, text = "Frecuencia pulsos binaurales (Hz):", font = ("Courier",40), bg = "#13254a", fg = "#ffffff" )
        labelpulsobinaural.pack()
        labelpulsobinaural.place(x = 400, y = 375)
        
        labelgeneracion2 = tk.PhotoImage(file = 'botones-08.png')
        bsub4 = tk.Button( self , image = labelgeneracion2, borderwidth = 0,
                       command = lambda:self.binauralgenerator())
        bsub4.pack()
        bsub4.place(x = 598, y = 600)
        
    def binauralgenerator (self):
        basefreq = int(entradafrecuenciacentral.get("1.0", 'end-1c'))
        binfreq = int(entradafrecuenciapulsobinaural.get("1.0", 'end-1c'))
        datos=[]
        sr = int(self.samplerate)
        basefreq = float(basefreq)
        per1 = 1/basefreq
        N1 = sr*per1
        N1 = round(N1)
        N1 = int(N1)
        x1 = np.arange(N1)
        y1 = 4/np.pi*np.sin(2*np.pi*x1/N1)
        numper1 = (self.duration*sr)/(N1) 
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
        numper2 = (self.duration*sr)/(N2)  
        numper2 = round(numper2)
        numper2 = int(numper2)
        y2 = np.tile(y2,numper2)
        y2 = y2/max(y2)
        y2 = y2.tolist()    
                
        a = len(y1)-len(y2)
        if (a>0):
            for j in range(a):
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
        stringbase = str(basefreq)
        stringbin = str(binfreq)
        filename = "/home/pi/Desktop/Tesis Luis Guerrero/User1_wavfiles/BinauralFrecuenciaCentral"+stringbase+"FrecuenciaBinaural"+stringbin+".wav"
        wavfile.write(filename,sr,y)
        
        song = AudioSegment.from_wav("/home/pi/Desktop/Tesis Luis Guerrero/User1_wavfiles/BinauralFrecuenciaCentral"+stringbase+"FrecuenciaBinaural"+stringbin+".wav")
        song.export("/home/pi/Desktop/Tesis Luis Guerrero/User1_oggfiles/BinauralFrecuenciaCentral"+stringbase+"FrecuenciaBinaural"+stringbin+".ogg", format="ogg")
    
                
        
       
        
class AudioPage(tk.Frame):
    
    
        
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        global botonplay,botonstop,botonpause, btnoff3, btnbrightness3, btnbackward2, botontime, botonaudio,entradatiempohoras,entradatiempominutos, varhoras, varminutos
        pygame.init()
        pygame.mixer.music.load('500Hz.ogg')
        self.configure(bg= "#13254a")
        self.botoncliqueado = 0
        self.vartiempo = 0
        self.vartime = 1
        
##        self.entradatiempominutos = None
        
        botonplay = tk.PhotoImage(file = 'boton-01v50px.png')
        bplay = tk.Button(self, image = botonplay, borderwidth = 0, command = lambda:self.play())
        bplay.pack()
        bplay.place(x = 935, y = 450)
        
        
        botonstop = tk.PhotoImage(file = 'botones-0750px.png')
        bstop = tk.Button(self, image = botonstop, borderwidth = 0, command = lambda:self.stop())
        bstop.pack()
        bstop.place(x = 870, y = 450)
        
        botonpause = tk.PhotoImage(file = 'boton-0250px.png')
        bpause = tk.Button(self, image = botonpause, borderwidth = 0, command = lambda:self.pause())
        bpause.pack()
        bpause.place(x = 1000, y = 450)
        
        botontime = tk.PhotoImage(file = 'botones-10.png')
        btime = tk.Button(self, image = botontime, borderwidth = 0, command = lambda:self.temproduccion())
        btime.pack()
        btime.place(x = 490, y = 250)
        
        botonaudio = tk.PhotoImage(file = 'botones-11.png')
        baudio = tk.Button(self, image = botonaudio, borderwidth = 0, command = lambda:self.chooseaudio())
        baudio.pack()
        baudio.place(x = 654, y = 600)
        
        btnoff3 =  tk.PhotoImage(file = 'boton-0330px2.png')
        b7 = tk.Button(self, image = btnoff3 , borderwidth = 0)#falta comando para el boton de apagado
        b7.pack()
        b7.place(x = 1800, y = 10)
        
        btnbrightness3 = tk.PhotoImage(file = 'boton v2-0430px.png')
        b8 = tk.Button(self, image = btnbrightness3 , borderwidth = 0)#falta comando para el boton de brightness
        b8.pack()
        b8.place(x = 1750, y = 10)
        
        btnbackward2 = tk.PhotoImage(file = 'botones-0650px.png')
        b9 = tk.Button(self, image = btnbackward2 , borderwidth = 0,
                       command = lambda:controller.show_frame(SubMenu))#falta comando para el boton de brightness
        b9.pack()
        b9.place(x = 20, y = 950)
        
        entradatiempohoras = tk.Text(self,width = 2,height = 1, font = ("Courier",40), bg = "#ffffff", fg = "#13254a")
        entradatiempohoras.pack()
        entradatiempohoras.place(x = 850, y = 175)
        
        labelhoras = tk.Label(self, text = "Horas:", font = ("Courier",40), bg = "#13254a", fg = "#ffffff" )
        labelhoras.pack()
        labelhoras.place(x = 650, y = 175)
        
        labelminutos = tk.Label(self, text = "Minutos:", font = ("Courier",40), bg = "#13254a", fg = "#ffffff" )
        labelminutos.pack()
        labelminutos.place(x = 950, y = 175)
        
        entradatiempominutos = tk.Text(self,width = 2,height = 1, font = ("Courier",40), bg = "#ffffff", fg = "#13254a")
        entradatiempominutos.pack()
        entradatiempominutos.place(x = 1225, y = 175)
        
    def play(self):
        if self.botoncliqueado < 1:
             pygame.mixer.music.play(self.vartime)
        if self.botoncliqueado >= 1:
             pygame.mixer.music.unpause()
        self.botoncliqueado += 1
        
    def pause(self):
        pygame.mixer.music.pause()
        
    def stop(self):
        pygame.mixer.music.stop()
        self.botoncliqueado = 0
        print(self.botoncliqueado)
        
    def chooseaudio(self):
        self.filename = tk.filedialog.askopenfilename(initialdir = "/home/pi/Desktop/Tesis Luis Guerrero/User1_oggfiles", title = "Seleccione un audio", filetypes =(("ogg files","*.ogg"),("all files","*.*")))
        pygame.mixer.music.load(self.filename)
        
    def temproduccion(self):
        
        varhoras = int(entradatiempohoras.get("1.0", 'end-1c'))
        varminutos = int(entradatiempominutos.get("1.0", 'end-1c'))
        self.vartime = ((varhoras*360) + (varminutos*6))
       
        

app = Main()

app.geometry('1920x1080')
      
        
    

app.mainloop()
    