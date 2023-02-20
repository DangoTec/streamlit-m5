import streamlit as st

def bienvenida(nombre):
    mensaje = "bienvenido/a: " + nombre
    return mensaje

myname=st.text_input("Nombre: ")

if (myname):
    mensaje=bienvenida(myname)
    st.write(mensaje)
