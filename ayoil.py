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
df = pd.read_csv("produksi_minyak_mentah.csv")
df
