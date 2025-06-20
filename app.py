import streamlit as st
import pandas as pd
import plotly_express as px

df=pd.read_csv('vehicles_us.csv')
st.header('Datos de anuncios de coches')
hist_button=st.button
disp_button=st.button
if hist_button:
    st.white('Creacion de histograma')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
if disp_button:
    st.white('Creación de graf. dispersion')
    disp = px.scatter(df)
    st.plotly_chart(disp)