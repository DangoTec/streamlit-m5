import streamlit as st
import pandas as pd

st.title("Streamlit - Search Name")

DATA_URL=("dataset.csv")

@st.cache
def load_data_byname(name):
    data=pd.read_csv(DATA_URL)
    filtered_data=data[data["name"].str.contains(name)]

    return filtered_data

myname=st.text_input("Name: ")
if (myname):
    filterbyname=load_data_byname(myname)
    count_row=filterbyname.shape[0]
    st.write(f"Total Names : {count_row}")

    st.dataframe(filterbyname)