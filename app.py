import streamlit as st
import pandas as pd
import plotly.express as px

#lectura de datos con el archvio cvs
df=pd.read_csv('vehicles_us.csv')

st.title('Listado de datos de anuncios de coches')
st.header('Datos de anuncios de coches')

#creacion del valor para el checkbox como los 100 primeros datos
mostrar_datos = st.checkbox('Los 100 primero datos')
# Si está marcado, muestra los primeros 100 registros
if mostrar_datos:
    st.dataframe(df.head(100))
else:
    st.dataframe(df)

#2
col1, col2 = st.columns(2)

# Botón para histograma en la primera columna
with col1:
    hist_button = st.button('Construir histograma')

# Botón para gráfico de dispersión en la segunda columna
with col2:
    scatter_button = st.button('Construir gráfico de dispersión')

#muestra de histograma con los datos de vehiculos
#hist_button=st.button
if hist_button:
    st.write('Histograma')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# nuestra de grafico de dispersion de los datos de vehiculos
#scatter_button=st.button
if scatter_button:
    st.write('Grafico de dispersion')
    disp = px.scatter(df, x='model_year', y='price', color='condition')
    st.plotly_chart(disp, use_container_width=True)