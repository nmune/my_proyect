import pandas as pd
import streamlit as st
import plotly.express as px
car_data = pd.read_csv('D:/TripleTen/my_proyect/vehicles_us.csv') # leer los datos
st.header('Información de venta de autos por marca')
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

sc_button = st.button('Construir un gráfico de dispersión') # crear un botón
     
if sc_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
         
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.write('Esta aplicación aún no es funcional. En construcción.')