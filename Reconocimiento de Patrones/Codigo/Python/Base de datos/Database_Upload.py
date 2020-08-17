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
        sql = '''INSERT INTO movement_eeg(Mov_ID,Mov_F1,Mov_F2,Mov_F3,Mov_F4,Mov_F5,Mov_Chnl_1_Fil,Mov_Descrip) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'''
        Data = (ID,F1,F2,F3,F4,F5,Data_Filt,Descript)
        self.cursor.execute(sql, Data)
        self.connection.commit()

    def check_data(self):
        self.cursor.execute("SELECT * FROM movement_eeg")
        myresult = self.cursor.fetchall()
        for row in myresult:
            print(row)
    def get_data(self,id):
        try:
            self.cursor.execute("SELECT * FROM movement_eeg WHERE Mov_ID = {}".format(id))
            user = self.cursor.fetchone()
            return user
        except Exception as e:
            raise


database=DataBase()
#database.close()
Opt = 1; #Ingresar 0 para guardar data y 1 para 'Descargarla'

if Opt == 0:#Modo de carga de datos
    Dir_Act =os.getcwd()    #Direcotrio actual del proyecto
    Dir_Origin = 'C:/Users/kokal/OneDrive/Documents/Primer Semetre 2020/Diseno e innovacion/Datos Pyshio/Python/Cerrando ojo izquierdo 5 rep/'
    DB_Dir = 'C:/Users/kokal/OneDrive/Documents/Sleep_DataBase/' #Directorio Local en donde se almacenaran los datos


    # Nombre de los archivos a subir
    Feature1 = 'Feature_1.csv'
    Feature2 = 'Feature_2.csv'
    Feature3 = 'Feature_3.csv'
    Feature4 = 'Feature_4.csv'
    Feature5 = 'Feature_5.csv'
    DFilt    = 'Datos_Filtrados.csv'

    ID = '000002'
    Descript = 'Esta es una prueba de ingreso'


    Save_Dir = DB_Dir+ID

    try:
        os.mkdir(Save_Dir)
    except OSError:
        print("La creación del directorio %s falló" )
    else:
        print("Se ha creado el directorio: %s " )


    files = os.listdir(Dir_Origin)
    #print(files)
    shutil.copy(Dir_Origin+Feature5, Save_Dir)
    shutil.copy(Dir_Origin + Feature4, Save_Dir)
    shutil.copy(Dir_Origin + Feature3, Save_Dir)
    shutil.copy(Dir_Origin + Feature2, Save_Dir)
    #shutil.copy(Dir_Origin + Feature1, Save_Dir)
    shutil.copy(Dir_Origin + DFilt, Save_Dir)

    F1 = Save_Dir + "/" +Feature1
    print(type(F1))
    F2 = Save_Dir + "/" +Feature2
    F3 = Save_Dir + "/" +Feature3
    F4 = Save_Dir + "/" +Feature4
    F5 = Save_Dir + "/" +Feature5
    Data_Filt = Save_Dir + "/" +DFilt

    database.add_data()
    database.close()
else:
    if Opt == 1:    # Modo de descarga de datos
        check = 1;
        if check == 0: # Revisar que datos estan disponibles
            database.check_data()
            database.close()
        else:
            if check == 1: #Extraer un dato en especifico
                search = '000002'
                D = database.get_data(search)
                print(D)
                Save_Id = D[0]
                S_Feature1 = D[1]
                S_Feature2 = D[2]
                S_Feature3 = D[3]
                S_Feature4 = D[4]
                S_Feature5 = D[5]
                S_Data_Filt = D[6]
                S_Desc = D[7]
                print(S_Desc)
                Destination = 'C:/Users/kokal/OneDrive/Escritorio/Prueba descarga/'  # Lugar en donde se guardaran los datos
                Save_Dir2 = Destination + Save_Id

                try:
                    os.mkdir(Save_Dir2)
                except OSError:
                    print("La creación del directorio %s falló")
                else:
                    print("Se ha creado el directorio: %s ")
                database.close()

                #shutil.copy(S_Feature1, Save_Dir2)
                shutil.copy(S_Feature2, Save_Dir2)
                shutil.copy(S_Feature3, Save_Dir2)
                shutil.copy(S_Feature4, Save_Dir2)
                shutil.copy(S_Feature5, Save_Dir2)
                shutil.copy(S_Data_Filt, Save_Dir2)






