# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:17:11 2020

@author: kokal
"""
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('sleepdbuvg_Key.json')
firebase_admin.initialize_app(cred)

dbs = firestore.client()

data_path = 'Data_Pro.csv'
data = pd.read_csv(data_path, header=0)
# print(data)
tst = data.to_numpy()
MAV = tst[[0]]
ZC = tst[[1]]
MMD = tst[[2]]

# print(str(MAV))
# print(MAV_Str)


data_path2 = 'Data_Raw.csv'
data2 = pd.read_csv(data_path2, header=0)
# print(data2)
PreRaw = data2.to_numpy()
Raw = PreRaw[[0]]

# print(Raw)

ID = 2020001
Descpt = "Aqui se ingresan las condiciones de las mediciones"
'''
doc_ref = dbs.collection('Upload_Test').document('SleepEEG')
doc_ref.set({
    'ID': ID,
    'MAV':str(MAV),
    'ZC':str(ZC),
    'MMD':str(MMD),
    'Raw_Data':str(Raw)


})
'''

# Get data
Doc = dbs.collection('Upload_Test').where('ID', '==', ID).stream()
for doc in Doc:
    print(('{} => {} '.format(doc.id, doc.to_dict())))
    Save_File = ('{} => {} '.format(doc.id, doc.to_dict()))

# print(Doc)
# print(type(Save_File))

SF = list(Save_File.split(" "))
    
# print(type(Save_File))
    
V1 = []
V2 = []
V3 = []
V4 = []

for vec in range(len(SF) - 1, -1, -1):
    if SF[vec] == "=>":
        del SF[vec]
    if SF[vec] == "SleepEEG":
        del SF[vec]

for vect in range(len(SF)- 1, -1, -1):
    if SF[vect] == "{'MAV':":
        Index1 = vect
    else:
        if SF[vect] == "'ID':":
            Index2 = vect
        else:
            if SF[vect] == "'MMD':":
                Index3 = vect
            else:
                if SF[vect] == "'ZC':":
                    Index4 = vect
                else:
                    if SF[vect] == "'Raw_Data':":
                        Index5 = vect

# print(Index1)
# print(Index2)
# print(Index3)
# print(Index4)
# print(Index5)

V1 = SF[Index1:Index2-1]
V2 = SF[Index2:Index3]
V3 = SF[Index3:Index4]
V4 = SF[Index4:Index5]
V5 = SF[Index5:]


# print(SF)
# print(V1)
# print(V2)
# print(V3)
# print(V4)
# print(V5)

Feature_1 = pd.DataFrame({
    V1[0]: V1[1:]
})

Feature_3 = pd.DataFrame({
    V3[0]: V3[1:]
})
Feature_4 = pd.DataFrame({
    V4[0]: V4[1:]
})
Raw_Datas = pd.DataFrame({
    V5[0]: V5[1:]
})
# print(Feature_1)
Feature_1.to_csv('Feature_1.csv')
Feature_3.to_csv('Feature_2.csv')
Feature_4.to_csv('Feature_3.csv')
Raw_Datas.to_csv('Raw_Datas.csv')
# '''
