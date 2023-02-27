import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Caso Bicicletas NY")
st.write("Equipo 5 TI3005B.103")
sidebar = st.sidebar
sidebar.title("Panel de Control")
sidebar.write("Selecciona las opciones deseadas")

Data_URL="citibike-tripdata.csv"
@st.cache
def load_data(nrows):
    data=pd.read_csv(Data_URL,nrows=nrows)
    data["started_at"] = pd.to_datetime(data["started_at"])
    data=data.rename(columns={"start_lat":"lat","start_lng":"lon"})
    return data

data_load_state=st.text("Loading data...")
data=load_data(1000)
data_load_state.text("Done...")

# Some number in the range 0-23
hour_to_filter = st.sidebar.slider('hour', 0, 23, 17)
filtered_data = data[data["started_at"].dt.hour == hour_to_filter]

if sidebar.checkbox("Show dataframe"):
    st.dataframe(filtered_data)

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)

data_2=data.copy()
data_2["hour"]=data_2["started_at"].dt.hour
avg_hours=(data_2.groupby(by=['hour']).count()["ride_id"])

st.sidebar.markdown("##")
st.sidebar.write("Recorridos por hora")
if sidebar.checkbox("Show graph"):
    st.subheader("Número de recorridos por hora")
    fig = px.bar(avg_hours,
                orientation="v"
                )
    st.plotly_chart(fig)
