import streamlit as st

def bienvenida(name):
    mymensaje = 'Bienvenido/a : ' + name
    return mymensaje

myname = st.text_input('nombre : ')

if(myname):
    mensaje = bienvenida(myname)
    st.write(mensaje)