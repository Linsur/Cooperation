# written by <Linsur>
# please streamlit run ../PyGwalker.py


import pandas as pd
import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer

st.set_page_config(page_title="Dashboard",page_icon="🌎",layout="wide",initial_sidebar_state="auto")
st.title("PyGwalker EDA")
uploaded_file = st.file_uploader("Your csv data")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()