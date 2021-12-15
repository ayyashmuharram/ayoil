"""
Aplikasi Streamlit untuk menggambarkan statistik penumpang TransJakarta
Sumber data berasal dari Jakarta Open Data
Referensi API Streamlit: https://docs.streamlit.io/library/api-reference
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import streamlit as st
from PIL import Image
import json


############### title ###############
st.set_page_config(layout="wide")  # this needs to be the first Streamlit command called
st.title("Statistik Jumlah Produksi Minyak")
st.markdown("*Sumber data dari nggatau")
############### title ###############)

############### sidebar ###############
image = Image.open('blackoil.png')
st.sidebar.image(image)

# read dataset
#filepath = "data-penumpang-bus-transjakarta-desember-2019.csv"
#filepath = 'https://data.jakarta.go.id/dataset/50b36c4b-0aed-42a5-82e4-c3510475716a/resource/4c3be51b-6ae9-44cc-9b42-616b4c982614/download/Data-Penumpang-Bus-Transjakarta-Desember-2019.csv'
df1 = pd.read_csv("produksi_minyak_mentah.csv")

file_json = open("kode_negara_lengkap.json")
data = json.loads(file_json.read())

urutan=0
for i in df1.loc():
    urutan2=0
    for j in data:
        kode1=(df1.loc[urutan,"kode_negara"])
        kode2=data[urutan2]['alpha-2']
        kode3=data[urutan2]['alpha-3']
        #print("kode 1 adalah",kode1)
        #print("kode 2 adalah",kode2)
        #print("kode 3 adalah",kode3)
        if kode1==kode2 or kode1==kode3:
            df1.loc[urutan,"kode_negara"]=data[urutan2]['name']
            #print('negara berubah menjadi',df1.loc[urutan,"kode_negara"])
        #print("ini adalah urutan kode negara",urutan,"dan urutan json",urutan2)
        urutan2=urutan2+1
    urutan=urutan+1
    if urutan==5839:break

df1
