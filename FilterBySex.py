import streamlit as st
import pandas as pd

st.title("Streamlit - Filter by sex")

data_url="dataset.csv"

@st.cache
def load_data():
    data=pd.read_csv(data_url)
    return data

@st.cache
def load_data_bysex(sex):
    data=pd.read_csv(data_url)
    filtered_data_bysex =data[data["sex"]==sex]
    return filtered_data_bysex

data=load_data()
selected_sex=st.selectbox("Select Sex",data["sex"].unique())
btnFilterbySex=st.button("Filter by sex")

if (btnFilterbySex):
    filterbysex=load_data_bysex(selected_sex)
    count_row=filterbysex.shape[0]
    st.write(f"Total Items : {count_row}")

    st.dataframe(filterbysex)