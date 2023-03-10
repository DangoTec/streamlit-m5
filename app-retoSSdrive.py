import pandas as pd
import numpy as np
import streamlit as st
#streamlit run .\OSF_Streamlit.py

#---PAGE CONFIG---
st.set_page_config(page_title="Alumnos Inscritos SS FJ2023",
                    )
st.title("Dashboard de Estudiantes por OSF")
sidebar = st.sidebar
sidebar.title("Selección de Datos")

#---READ DATA---
@st.cache
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

data = load_data(st.secrets["public_gsheets_url"])

#---FILTROS---
#Initialising SessionState's
if "load_state" not in st.session_state:
    st.session_state.load_state = False
def SessionStateOff():
    st.session_state.load_state=False

#Filtro por OSF
OSFname=sidebar.selectbox("Seleccionar OSF:", 
                        data['Organización SF'].unique())
OSFdata=data[data["Organización SF"]==OSFname] #Filtra experiencias por OSF
st.sidebar.markdown("##")

#Filtro de experiencias de OSF
with st.sidebar.form(key="my_form"):
    #Selección de experiencia
    OSFexp=st.selectbox("Nombre de la experiencia", 
                            options=OSFdata['Nombre experiencia'].unique())
    #Datos de alumnos deseados
    Datos = st.multiselect(label="Datos de interés sobre los alumnos",
                            #label_visibility="hidden",
                            options=list(OSFdata.columns),
                            default=["No. plazas", "Matrícula (A0 o A00)", "Nombre Completo del estudiante"])
    #Botón de submit
    submit_button=st.form_submit_button(label="Buscar")

OSFexpdata=OSFdata[OSFdata["Nombre experiencia"]==OSFexp] #Filtro
OSFexpdata=OSFexpdata.reset_index()
OSFexpdata=OSFexpdata.drop("index",axis=1)
st.sidebar.markdown("##")

#Obtener datos
def GetDataStudent (Col,fila): #Col: seleccionadas de Datos, Fila: estudiantes
    Dic_Datos={}
    for i in Col:
        Dato=OSFexpdata[i][fila] #Dato individual
        Dic_Datos[i]=Dato #Crear Key:Value
    return Dic_Datos

#---MAIN---
st.subheader("Alumnos")
if submit_button or st.session_state.load_state:
    st.session_state.load_state=True
    #Imprimir Datos por alumno personalizado
    alumnos = []
    for i in range(OSFexpdata.shape[0]):
        Alumno=GetDataStudent(Datos,i) #Datos en diccionario
        alumnos.append(Alumno)
    st.dataframe(alumnos)
    st.markdown("""---""")

    #Salvar datos en excel
    st.subheader("Exportar Datos")
    df=pd.DataFrame(alumnos)
    @st.cache
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')
    csv = convert_df(df)
    st.download_button(
        label="Exportar",
        data=csv,
        file_name=f'Alumnos_{OSFexp}_2023.csv',
        mime='text/csv',
        on_click=SessionStateOff())
