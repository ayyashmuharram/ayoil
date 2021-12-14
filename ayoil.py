"""
Aplikasi Streamlit untuk menggambarkan statistik produksi minyak

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import streamlit as st
from PIL import Image

############### title ###############
st.set_page_config(layout="wide")  # this needs to be the first Streamlit command called
st.title("Statistik Produksi Minyak")
############### title ###############

############### sidebar ###############
image = Image.open('blackoil.png')
st.sidebar.image(image)

st.sidebar.title("Settings")
left_col, mid_col, right_col = st.columns(3)

## User inputs on the control panel
st.sidebar.subheader("Display configuration settings")
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

n_tampil = st.sidebar.number_input("Number of rows in the table shown", min_value=1, max_value=None, value=10)
############### sidebar ###############

############### upper left column ###############
left_col.subheader("Data representation table")
