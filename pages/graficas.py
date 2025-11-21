import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

st.set_page_config(
    page_title="Graficas de datos",
    page_icon="imagenes/icono.png"
)



st.title("GRAFICAS DE LA DATA 📊", anchor=False)
st.page_link("dashboard.py", label="⬅️ Volver a la página principal")

csv_path = os.path.join(os.path.dirname(__file__), "..", "registro.csv")

try:
    prog_df = pd.read_csv(csv_path)
    st.success("Archivo cargado correctamente")

    st.header("Datos visualizados", anchor=False)
    st.dataframe(prog_df)

    st.divider()
    st.subheader("Distribución de Géneros", anchor=False)
    conteo_genero = prog_df["Género"].value_counts()

    fig, ax = plt.subplots(figsize=(6,6))
    ax.pie(conteo_genero, labels=conteo_genero.index, autopct="%1.1f%%")
    ax.set_title("Distribución de Género en los Estudiantes")
    st.pyplot(fig)
    plt.close()

    with st.expander("Acerca de la gráfica"):
        st.write(
            "Este gráfico muestra la proporción de géneros registrados. "
            "Ayuda a entender la composición del grupo de estudiantes."
        )

    st.divider()
    st.subheader("Número de mascotas por año de nacimiento", anchor=False)

    fig = px.bar(
        prog_df,
        x="Año nacimiento",
        y="Nro Mascotas",
        color="Nro Mascotas",
        title="Relación entre Año de Nacimiento y Número de Mascotas",
    )
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("Acerca de la gráfica"):
        st.write(
            "Este gráfico muestra cómo varía la cantidad de mascotas según el año "
            "de nacimiento. Puede revelar si los estudiantes más jóvenes poseen "
            "más mascotas en promedio."
        )

    st.divider()
    st.subheader("Carreras más registradas", anchor=False)

    conteo_carreras = prog_df["Carrera universitaria"].value_counts().reset_index()
    conteo_carreras.columns = ["Carrera", "Cantidad"]

    fig = px.bar(
        conteo_carreras,
        x="Carrera",
        y="Cantidad",
        color="Cantidad",
        title="Cantidad de Estudiantes por Carrera",
    )
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("Acerca de la gráfica"):
        st.write(
            "Este gráfico permite observar qué carreras cuentan con mayor cantidad "
            "de estudiantes registrados. Es útil para analizar preferencias "
            "académicas o distribución por facultades."
        )

    st.divider()
    st.subheader("Mapa de calor de correlación", anchor=False)

    columnas_numericas = prog_df.select_dtypes(include=["int64", "float64"])
    fig, ax = plt.subplots(figsize=(6,4))
    sns.heatmap(columnas_numericas.corr(), annot=True, cmap="Blues")
    plt.title("Correlaciones entre Variables Numéricas")
    st.pyplot(fig)
    plt.close()

    with st.expander("Acerca de la gráfica"):
        st.write(
            "Este mapa de calor permite identificar qué variables numéricas tienen "
            "mayor relación. Por ejemplo, si el año de nacimiento se relaciona con "
            "la cantidad de mascotas."
        )

except Exception as e:
    st.error(f"Error al leer al archivo: {e}")
