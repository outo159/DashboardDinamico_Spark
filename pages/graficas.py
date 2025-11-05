import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.express as px

st.title("GRAFICAS DE LA DATA 📊")
st.page_link("dashboard.py", label="⬅️ Volver a la página principal")

csv_path = os.path.join(os.path.dirname(__file__),"..","registro.csv")

try:
    prog_df = pd.read_csv(csv_path)
    st.success("Archivo cargado correctamente")
    st.header("Datos visualizados")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Graficos de barras")
            fig, ax = plt.subplots(figsize = (8,6))
            ax.bar(prog_df["Edad"],prog_df["Cursos llevados"],color = 'skyblue')
            plt.title('Cursos llevados por persona')
            plt.xlabel('Edad')
            plt.ylabel('Cursos llevados')
            plt.xticks(rotation = 45)
            st.pyplot(fig)
            plt.close()
        with col2:
            st.subheader("grafico de pastel")
            fig = px.pie(prog_df,
                         values='Cursos llevados',
                         names = 'Edad',
                         title='Distribucion de Cursos por edad')
            st.plotly_chart(fig, use_container_width=True)
except Exception as e:
    st.error(f"Error al leer al archivo: {e}")

  