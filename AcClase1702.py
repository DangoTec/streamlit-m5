import streamlit as st
import pandas as pd

names= "dataset.csv"
names_data=pd.read_csv(names)


st.title("St and pd - Daniel Porras Actividad 17/02")

st.dataframe(names_data)
