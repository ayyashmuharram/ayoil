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

st.sidebar.subheader("Pengaturan konfigurasi tampilan")
list_bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
bulan = st.sidebar.selectbox("Pilih bulan", list_bulan)
list_url = {'Januari': 'https://data.jakarta.go.id/dataset/50b36c4b-0aed-42a5-82e4-c3510475716a/resource/1a3bcf20-1ed0-42c9-baca-71cdabbe7fdc/download/Data-Penumpang-Bus-Transjakarta-Januari-2019.csv',
            'Februari': 'https://data.jakarta.go.id/dataset/50b36c4b-0aed-42a5-82e4-c3510475716a/resource/849e203a-ca5d-47d6-9024-1e753ca405ad/download/Data-Penumpang-Bus-Transjakarta-Februari-2019.csv', 
            'Maret': 'https://data.jakarta.go.id/dataset/50b36c4b-0aed-42a5-82e4-c3510475716a/resource/c7cea037-4306-4d3c-aabd-382798bf88ff/download/Data-Penumpang-Bus-Transjakarta-Maret-2019.csv', 
            'April': 'https://data.jakarta.go.id/dataset/50b36c4b-0aed-42a5-82e4-c3510475716a/resource/204a8676-afe3-4355-91cf-21ac866605eb/download/Data-Penumpang-Bus-Transjakarta-April-2019.csv', 
            'Mei': 'https://data.jakarta.go.id/dataset/50b36c4b-0aed-42a5-82e4-c3510475716a/resource/178a44a4-ad21-41c0-860b-67b5e1dd0175/download/Data-Penumpang-Bus-Transjakarta-Mei-2019.csv', 
            'Juni': 'https://data.jakarta.go.id/dataset/50b36c4b-0aed-42a5-82e4-c3510475716a/resource/fc49004a-2eaf-43c2-ab7d-b316ca0a6e38/download/Data-Penumpang-Bus-Transjakarta-Juni-2019.csv', 
            'Juli': 'https://data.jakarta.go.id/dataset/50b36c4b-0aed-42a5-82e4-c3510475716a/resource/ee7a387c-f0e5-4564-a17f-5e50e1137441/download/Data-Penumpang-Bus-Transjakarta-Juli-2019.csv', 
            'Agustus': 'https://data.jakarta.go.id/dataset/50b36c4b-0aed-42a5-82e4-c3510475716a/resource/d950bb97-7a49-42ff-9d22-438374404b82/download/Data-Penumpang-Bus-Transjakarta-Agustus-2019.csv', 
            'September': 'https://data.jakarta.go.id/dataset/50b36c4b-0aed-42a5-82e4-c3510475716a/resource/04e2b099-2d2c-47d5-bddd-3b0d092fbdae/download/Data-Penumpang-Bus-Transjakarta-September-2019.csv', 
            'Oktober': 'https://data.jakarta.go.id/dataset/50b36c4b-0aed-42a5-82e4-c3510475716a/resource/b37e5a6f-9b98-443b-bb5f-bdba288cf7e3/download/Data-Penumpang-Bus-Transjakarta-Oktober-2019.csv', 
            'November': 'https://data.jakarta.go.id/dataset/50b36c4b-0aed-42a5-82e4-c3510475716a/resource/14520801-0674-4334-89bc-a1f1a94257b7/download/Data-Penumpang-Bus-Transjakarta-November-2019.csv', 
            'Desember': 'https://data.jakarta.go.id/dataset/50b36c4b-0aed-42a5-82e4-c3510475716a/resource/4c3be51b-6ae9-44cc-9b42-616b4c982614/download/Data-Penumpang-Bus-Transjakarta-Desember-2019.csv'
           }

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

negara_unik = list(df1['kode_negara'].unique())
print(f"Negara unik: {negara_unik}")

tulis_negara = []
for i, negara in enumerate(negara_unik):
    tulis_negara.append(f"{str(i+1)}. {negara}\n")
tulis_negara = ' '.join(map(str, tulis_negara))
tulis_negara
