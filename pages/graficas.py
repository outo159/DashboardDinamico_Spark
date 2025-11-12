import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

####
#  AGREGAR NUEVAS GRAFICAS
####

st.set_page_config(
    page_title="Graficas de datos",
    page_icon="imagenes/icono.png"
)

st.title("GRAFICAS DE LA DATA 📊",anchor=False)
st.page_link("dashboard.py", label="⬅️ Volver a la página principal")

csv_path = os.path.join(os.path.dirname(__file__),"..","registro.csv")

try:
    prog_df = pd.read_csv(csv_path)
    st.success("Archivo cargado correctamente")
    st.header("Datos visualizados",anchor=False)
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Grafico de dispercion",anchor=False)
            fig, ax = plt.subplots(figsize=(8,6))
            yearNac = prog_df['Año nacimiento'].head(5)
            almuerzoFav = prog_df['Almuerzo favorito'].head(5)
            ax.scatter(yearNac,almuerzoFav,color='blue',alpha = 0.6)
            plt.xticks(rotation=45)
            plt.title('año de nacimiento con almuerzo favorito')
            plt.ylabel('Almuerzo favorito')
            plt.xlabel('Año de nacimiento')
            st.pyplot(fig)
            plt.close()


        with col2:
            st.subheader("Grafica de barras",anchor=False)
            fig, ax = plt.subplots(figsize=(8,6))
            yearNac = prog_df['Año nacimiento'].head(5)
            almuerzoFav = prog_df['Almuerzo favorito'].head(5)
            ax.bar(yearNac,almuerzoFav,color='blue',alpha = 0.6)
            plt.xticks(rotation=45)
            plt.title('año de nacimiento con almuerzo favorito')
            plt.xlabel('Año de nacimiento')
            plt.ylabel('Almuerzo favorito')
            st.pyplot(fig)
            plt.close()
        st.divider()
        col1,col2=st.columns(2)
        with col1:
            st.subheader("Grafica de violin",anchor=False)
            fig,ax = plt.subplots(figsize=(8,6))
            sns.violinplot(data=prog_df, x='Año nacimiento', y='Almuerzo favorito')
            plt.xticks(rotation=45)
            plt.title('Distribucion de año con comida favorita')
            st.pyplot(fig)
            plt.close()
        with col2:
            st.subheader("Grafica de violin",anchor=False)
            fig,ax = plt.subplots(figsize=(8,6))
            sns.boxplot(data=prog_df, x='Año nacimiento', y='Almuerzo favorito')
            plt.xticks(rotation=45)
            plt.title('Distribucion de año con comida favorita')
            st.pyplot(fig)
            plt.close()
except Exception as e:
    st.error(f"Error al leer al archivo: {e}")

  