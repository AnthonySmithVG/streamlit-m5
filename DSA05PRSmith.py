import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@st.cache
def data(filas):
    return pd.read_csv("Employees.csv").head(filas)

@st.cache
def alldata():
    return pd.read_csv("Employees.csv")

@st.cache
def buscar_empleado(dato):
    if dato != '':
        if df['Employee_ID'].str.contains(str(dato)).any():
            return df[df['Employee_ID'].str.contains(str(dato))]

        elif df['Hometown'].str.contains(dato).any():
            return df[df['Hometown'].str.contains(dato)]

        elif df['Unit'].str.contains(dato).any():
            return df[df['Unit'].str.contains(dato)]
        
        else:
            return 'No se encontraron resultados'
    return 'Ingresa un valor'
   
@st.cache
def buscar_por_nivel_educativo(dato):
    if dato in df['Education_Level'].values:
        return df[df['Education_Level'] == dato]

@st.cache
def buscar_por_ciudad(dato):
    if dato in df['Hometown'].values:
        return df[df['Hometown'] == dato]

@st.cache
def buscar_por_unidad(dato):
    if dato in df['Unit'].values:
        return df[df['Unit'] == dato]

df = data(500)
st.title('Reto número 5')
st.header("Aplicación web de Ciencia de Datos")
st.text('Ánalisis de empleados')
sidebar = st.sidebar
sidebar.title("Empleados")

# histograma
st.subheader('Total de empleados agrupados por edad')
chart_data = df.groupby('Age')['Employee_ID'].count()
st.bar_chart(chart_data)

# frecuencias
st.subheader('Frecuencia de unidades funcionales')
unit_counts = df['Unit'].value_counts()
st.area_chart(unit_counts)

# Hometown / Attrition_rate
st.subheader('Ciudades con su índice de deserción')
city_attrition = df.groupby('Hometown')['Attrition_rate'].mean()
st.bar_chart(city_attrition)

# Age / Attrition_rate
st.subheader('Deserción por edad')
Age_attrition = df.groupby('Age')['Attrition_rate'].mean()
st.bar_chart(Age_attrition)

# Age / Attrition_rate
st.subheader('Deserción por tiempo de servicio')
Time_of_service_attrition = df.groupby('Time_of_service')['Attrition_rate'].mean()
st.line_chart(Time_of_service_attrition)

if sidebar.checkbox("Mostrar todos los empleados"):
    st.write(alldata())

#Búsqueda de empleados
text = st.sidebar.text_input('Ingresa el Id de empleado, ciudad o área: ')

if st.sidebar.button('Buscar'):
    st.write(buscar_empleado(text))

#Nivel educativo
selectedBox = st.sidebar.selectbox('Selecciona el nivel educativo', df['Education_Level'].unique())

if st.sidebar.button('Buscar por nivel educativo'):
    dfEmpleadosNE = buscar_por_nivel_educativo(selectedBox)
    st.subheader(r'Total de empleados: ' + str(dfEmpleadosNE.shape[0]))
    st.write(dfEmpleadosNE)

#Ciudad
selectedBoxCity = st.sidebar.selectbox('Selecciona la ciudad', df['Hometown'].unique())

if st.sidebar.button('Buscar por ciudad'):
    dfCiudad = buscar_por_ciudad(selectedBoxCity)
    st.subheader(r'Total de empleados: ' + str(dfCiudad.shape[0]))
    st.write(dfCiudad)

#Unit
selectedBoxUnit = st.sidebar.selectbox('Selecciona la unit', df['Unit'].unique())

if st.sidebar.button('Buscar por unidad'):
    dfUnit = buscar_por_unidad(selectedBoxUnit)
    st.subheader(r'Total de empleados: ' + str(dfUnit.shape[0]))
    st.write(dfUnit)