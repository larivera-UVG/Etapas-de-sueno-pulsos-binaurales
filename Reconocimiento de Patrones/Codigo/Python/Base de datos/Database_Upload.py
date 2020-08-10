# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:17:11 2020

@author: kokal
"""
import mysql.connector
import shutil
import os

class DataBase:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            db='uvg_eeg'
        )
        self.cursor = self.connection.cursor()
        print("Conexion Exitosa")

    def close(self):
        self.connection.close()

    def add_data(self):
        sql = "INSERT INTO movement_eeg(Mov_ID,Mov_F1,Mov_F2,Mov_F3,Mov_F4,Mov_F5,Mov_Chnl_1_Fil,Mov_Descrip) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        Data = (ID,F1,F2,F3,F4,F5,Data_Filt,Descript)
        self.cursor.execute(sql, Data)
        self.connection.commit()

database=DataBase()
database.close()
Opt = 0; #Ingresar 0 para guardar data y 1 para 'Descargarla'

if Opt == 0:#Modo de carga de datos
    Dir_Act =os.getcwd()    #Direcotrio actual del proyecto
    Dir_Origin = 'C:\\Users\kokal\OneDrive\Documents\Primer Semetre 2020\Diseno e innovacion\Datos Pyshio\Python\Cerrando ojo izquierdo 5 rep'
    DB_Dir = 'C:\\Users\kokal\OneDrive\Documents\Sleep_DataBase\ ' #Directorio Local en donde se almacenaran los datos

    # Nombre de los archivos a subir
    Feature1 = 'Feature_1.csv'
    Feature2 = 'Feature_2.csv'
    Feature3 = 'Feature_3.csv'
    Feature4 = 'Feature_4.csv'
    Feature5 = 'Feature_5.csv'
    files = os.listdir(Dir_Origin)


    # asignando variables para realizar la carga de datos
    ID = '000001'

    Data_Filt = '123,456,789'
    Descript = 'Esta es una prueba de ingreso'
    for file in files:
        if os.path.isfile(file):
            shutil.copy2(file, DB_Dir+ID)
            
    F1 = DB_Dir + Feature1
    print(F1)
    F2 = 1
    F3 = 1
    F4 = 1
    F5 = 1
    # database.add_data()
else:
    if Opt == 1:
        #Modo de descarga de datos
        print('Null')