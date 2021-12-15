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
############### title ###############)

############### sidebar ###############
image = Image.open('blackoil.png')
st.sidebar.image(image)

st.sidebar.title("Pilihan")
left_col, mid_col, right_col = st.columns(3)

list_statistik = ['Mentah', 'Negara', 'Tahun', 'Negara Terbesar', 'Negara Terkecil', 'Negara Kosong', 'Data Negara']
pilihan = st.sidebar.selectbox("Pilih Statistik", list_statistik)
list_pilihan = {'Mentah':'1', 
                'Negara':'2',
                'Tahun':'3',
                'Negara Terbesar':'4', 
                'Negara Terkecil':'5',
                'Negara Kosong':'6',
                'Data Negara':'7',
                }

filepath = list_pilihan[pilihan]
angka=filepath
st.markdown(angka)

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

df2=df1.loc[df1['kode_negara']=='Australia']
plt.show()

#Negara
st.markdown('Negara')
negara_unik = list(df1['kode_negara'].unique())
print(f"Negara unik: {negara_unik}")
tulis_negara = []
for i, negara in enumerate(negara_unik):
  tulis_negara.append(f"{str(i+1)}. {negara}\n")
tulis_negara = ' '.join(map(str, tulis_negara))
tulis_negara
