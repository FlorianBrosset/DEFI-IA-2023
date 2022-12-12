#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 16:32:19 2022

@author: brosset
"""

#Gradio
import pandas as pd
import numpy as np
import gradio as gr
import tensorflow_decision_forests as tfdf

#importer le modèle

#importer les données hotels
hotels = pd.read_csv('features_hotels.csv', index_col=['hotel_id', 'city'])


#crée un dataframe contenant seulement les inputs
def DfFromInput(city,date,language,mobile,avatar_id,hotel_id,stock):
    d = {'city':[city] ,'date':[date] , 'language':[language] ,'mobile':[mobile] ,'avatar_id':[avatar_id] ,
         'hotel_id':[hotel_id],'stock':[stock]}
    df=pd.DataFrame(data=d)
    return df


#join du dataframe avec les données "hotels"
def AddData(city,date,language,mobile,avatar_id,hotel_id,stock):
    df = DfFromInput(city,date,language,mobile,avatar_id,hotel_id,stock)
    hotels = pd.read_csv('features_hotels.csv', index_col=['hotel_id', 'city'])
    df = df.join(hotels, on=['hotel_id', 'city'])
    return df


#transformation des données pour tfdf et prédiction du prix
def Price(city,date,language,mobile,avatar_id,hotel_id,stock):
    df =AddData(city,date,language,mobile,avatar_id,hotel_id,stock)
    df =tfdf.keras.pd_dataframe_to_tf_dataset(df)
    price =model.predict(df,verbose =0)
    price=price[0,0]
    return price


app = gr.Interface(fn = Price,
                    inputs= [
                        gr.Radio(["amsterdam","copenhagen","madrid","paris","rome",
                                          "sofia","valletta","vienna","vilnius"]),
                        gr.Slider(0,44,step =1,value =0),
                        gr.Radio(["austrian","belgian","bulgarian","croatian","cypriot",
                                       "czech","danish","dutch","estonian","finnish","french",
                                       "german","greek","hungarian","irish","italian","latvian",
                                       "lithuanian","luxembourgish","maltese","polish","portuguese",
                                       "romanian","slovakian","slovene","spanish","swedish"]),
                        gr.Slider(0,1,step=1,value=0),
                        gr.Number(value=111612),
                        gr.Number(),
                        gr.Number()
                        
                    ],
                    
                    outputs="number")

app.launch()