import streamlit as st
import pandas as pd
import os
import plotly.express as px
import datetime as dt

st.set_page_config(
    page_title="Información",
    page_icon="imagenes/icono.png",
    layout="wide"
)


st.title("ACERCA DE NOSOTROS", anchor=False)
st.page_link("dashboard.py", label="⬅️ Volver a la página principal")


#CArgar el csv
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "registro.csv"))
prog_df = pd.read_csv(csv_path)

#dataframe para crear tabla donde se obtiene solo carrera, edad y ciclo
hoy = dt.date.today()
prog_df["Edad"] = hoy.year - prog_df["Año nacimiento"]

tabla_reducida = prog_df[["Edad", "Ciclo académico", "Carrera universitaria"]]
st.dataframe(tabla_reducida, use_container_width=True)


st.title("Informacion sobre el proyecto", anchor=False)
col1, col2 = st.columns([1,1])
with col1:
    st.write("""
         Este proyecto consiste en la creación de una página web interactiva que integra un dashboard dinámico desarrollado con Streamlit.
         El objetivo principal es proporcionar una plataforma accesible y visualmente intuitiva que permita analizar datos de manera 
         rápida y eficiente. La página ha sido diseñada para ser ligera, moderna y compatible con diferentes dispositivos, ofreciendo una 
         experiencia fluida tanto para usuarios técnicos como no técnicos.
         """)
with col2:
    st.write("""
            El dashboard se construyó con la intención de transformar información cruda en visualizaciones claras y comprensibles. 
             Gracias al uso de librerías como Pandas, Plotly y Matplotlib, el sistema permite generar gráficos dinámicos que facilitan la 
             interpretación de tendencias y patrones relevantes. Este enfoque visual mejora la toma de decisiones basada en datos y ofrece 
             una forma amigable de explorar la información sin necesidad de conocimientos avanzados en programación.
             """)
st.divider()
st.subheader("Informacion sobre el proyecto", anchor=False)
col1, col2 = st.columns([1,1])
with col1:
    with st.expander("Loren ipsum dolor sit amet",expanded=True):
        fig = px.pie(prog_df,
                    values='Edad',
                    names='Carrera universitaria',
                    title='Relacion carrera edad')
        st.plotly_chart(fig, use_container_width=True, key="pie1")
with col2:
    st.write("""
            Para el desarrollo se empleó Streamlit como framework central debido a su rapidez y simplicidad al momento de crear interfaces web 
             interactivas. Además, se integraron diversas librerías de Python para el manejo de datos, generación de estadísticas y creación 
             de visualizaciones. El uso de estas herramientas permitió construir una aplicación modular, escalable y fácilmente mantenible, 
             capaz de adaptarse a distintas necesidades analíticas.
             """)
st.divider()
col1, col2 = st.columns([1,1])

with col1:
    st.write("""
            El sistema carga datos desde archivos CSV y los procesa en tiempo real, permitiendo al usuario visualizar gráficos actualizados de
             manera inmediata. Entre sus características principales se encuentran los filtros interactivos, el despliegue automático de 
             información y la capacidad de expandir o contraer secciones según la necesidad del usuario. Esta estructura mejora la navegación 
             dentro del dashboard y facilita la comprensión de la información mostrada.
             """)
with col2:
    fig2 = px.pie(
        prog_df,
        values='Edad',
        names='Carrera universitaria',
        title='Relacion carrera edad')

    st.plotly_chart(fig2, use_container_width=True, key="pie2")
    col1, col2 = st.columns([1,1])
    with col1:
        pass
    with col2:
        st.page_link("dashboard.py", label="⬅️ Volver a la página principal")
