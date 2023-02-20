import streamlit as st
import pandas as pd

st.title("Streamlit - filter by ranges")

data_url="dataset.csv"

@st.cache
def load_data_byrange(startid,endid):
    data=pd.read_csv(data_url)
    filtered_data_byrange=data[(data["index"]>= startid) & (data["index"]<=endid)]

    return filtered_data_byrange

startid=st.text_input("Start index :")
endid = st.text_input("end index: ")
btnRange=st.button("Search by range")

if (btnRange):
    filterbyrange=load_data_byrange(int(startid),int(endid))
    count_row=filterbyrange.shape[0]
    st.write(f"Total items: {count_row}")
    st.dataframe(filterbyrange)