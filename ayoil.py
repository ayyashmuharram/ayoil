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

# Create a page dropdown 
page = st.selectbox("Choose your page", ["Page 1", "Page 2", "Page 3"]) 
if page == "Page 1":
    # Display details of page 1
elif page == "Page 2":
    # Display details of page 2
elif page == "Page 3":
    # Display details of page 3
