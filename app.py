import streamlit as st
import pandas as pd
import plotly_express as px

df=pd.read_csv('vehicles_us.csv')
st.header('Datos de anuncios de coches')
#mostrar dataframe con los datos de los anuncios por coche
st.dataframe(df)
hist_button=st.button
disp_button=st.button
#muestra de histograma con los datos de vehiculos
if hist_button:
    st.write('Creacion de histograma')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
# nuestra de grafico de dispersion de los datos de vehiculos
if disp_button:
    st.write('Creación de graf. dispersion')
    disp = px.scatter(df, x='model_year', y='price', color='condition')
    st.plotly_chart(disp, use_container_width=True)