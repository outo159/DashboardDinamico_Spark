import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# Configuración inicial
st.set_page_config(page_title="Graficas de datos", page_icon="imagenes/icono.png", layout="wide")

st.title("GRAFICAS DE LA DATA", anchor=False)

# -------------------------------------------
# PRIMER BLOQUE 
# -------------------------------------------

csv_path_local = os.path.join(os.path.dirname(__file__), "..", "registro.csv")

try:
    prog_df = pd.read_csv(csv_path_local)
    st.success("Archivo cargado correctamente desde registro.csv")

    st.header("Datos visualizados", anchor=False)

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Grafico de dispersion", anchor=False)
            fig, ax = plt.subplots(figsize=(8, 6))
            yearNac = prog_df['Año nacimiento'].head(5)
            almuerzoFav = prog_df['Almuerzo favorito'].head(5)
            ax.scatter(yearNac, almuerzoFav, color='blue', alpha=0.6)
            plt.xticks(rotation=45)
            plt.title('Año de nacimiento con almuerzo favorito')
            plt.ylabel('Almuerzo favorito')
            plt.xlabel('Año de nacimiento')
            st.pyplot(fig)
            plt.close()

        with col2:
            st.subheader("Grafica de barras", anchor=False)
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.bar(yearNac, almuerzoFav, color='blue', alpha=0.6)
            plt.xticks(rotation=45)
            plt.title('Año de nacimiento con almuerzo favorito')
            plt.xlabel('Año de nacimiento')
            plt.ylabel('Almuerzo favorito')
            st.pyplot(fig)
            plt.close()

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Grafica de violin", anchor=False)
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.violinplot(data=prog_df, x='Año nacimiento', y='Almuerzo favorito')
            plt.xticks(rotation=45)
            plt.title('Distribucion de año con comida favorita')
            st.pyplot(fig)
            plt.close()

        with col2:
            st.subheader("Grafica de caja", anchor=False)
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.boxplot(data=prog_df, x='Año nacimiento', y='Almuerzo favorito')
            plt.xticks(rotation=45)
            plt.title('Distribucion de año con comida favorita')
            st.pyplot(fig)
            plt.close()

except Exception as e:
    st.error(f"Error al leer el archivo registro.csv: {e}")

# -------------------------------------------
# SEGUNDO BLOQUE: ANALISIS CSV DATOS_SIMULADOS
# -------------------------------------------

st.header("Analisis del archivo datos_simulados.csv")

ruta = r"C:\Users\COMPUTER\Downloads\datos_simulados.csv"

try:
    df = pd.read_csv(ruta)
    df.columns = df.columns.str.replace('\ufeff', '').str.strip()

    st.success("Archivo datos_simulados.csv cargado correctamente.")

    st.subheader("Vista previa de los datos")
    st.dataframe(df.head())

    df["Edad_aproximada"] = 2025 - df["Año nacimiento"]

    # Función para clasificar generación
    def grupo_generacional(anio):
        if anio >= 2005:
            return "Gen Alpha"
        elif anio >= 1997:
            return "Centennial"
        elif anio >= 1981:
            return "Millennial"
        else:
            return "Boomer"

    df["Grupo_generacional"] = df["Año nacimiento"].apply(grupo_generacional)

    df["Mascotas_por_edad"] = df.apply(
        lambda row: row["Nro Mascotas"] / row["Edad_aproximada"] if row["Edad_aproximada"] > 0 else 0,
        axis=1
    )

    st.subheader("Datos con nuevas columnas")
    st.dataframe(df.head())

    st.subheader("Análisis descriptivo")
    st.write(df.describe(include="all"))

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Edad promedio", f"{df['Edad_aproximada'].mean():.1f}")
        st.metric("Edad mínima", df["Edad_aproximada"].min())
        st.metric("Edad máxima", df["Edad_aproximada"].max())
    with col2:
        st.metric("Mascotas promedio", f"{df['Nro Mascotas'].mean():.2f}")
        st.metric("Máximo de mascotas", df["Nro Mascotas"].max())
        st.metric("Carreras distintas", df["Carrera universitaria"].nunique())

    # Boxplot mascotas por genero
    fig1 = px.box(df, x="Género", y="Nro Mascotas",
                  color="Género", title="Distribución de mascotas por género", points="all")
    st.plotly_chart(fig1, use_container_width=True)

    # Sunburst
    fig2 = px.sunburst(df, path=["Carrera universitaria", "Almuerzo favorito"],
                       title="Almuerzo favorito por carrera")
    st.plotly_chart(fig2, use_container_width=True)

    # Scatter
    fig3 = px.scatter(df, x="Edad_aproximada", y="Nro Mascotas",
                      color="Curso favorito", size="Mascotas_por_edad",
                      title="Edad vs mascotas por curso favorito")
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("Gráficos adicionales")

    fig4 = px.histogram(df, x="Edad_aproximada", nbins=20, title="Histograma de edades")
    st.plotly_chart(fig4, use_container_width=True)

    # Gráfico de género corregido
    df_genero = df["Género"].value_counts().rename_axis("Género").reset_index(name="Cantidad")
    fig5 = px.bar(df_genero, x="Género", y="Cantidad", title="Cantidad de estudiantes por género")
    st.plotly_chart(fig5, use_container_width=True)

    fig6 = px.pie(df, names="Grupo_generacional", title="Proporción por grupo generacional")
    st.plotly_chart(fig6, use_container_width=True)

    fig7 = px.box(df, x="Carrera universitaria", y="Edad_aproximada",
                  title="Distribución de edades por carrera")
    st.plotly_chart(fig7, use_container_width=True)

    fig8 = px.histogram(df, x="Curso favorito", color="Género",
                        barmode="group", title="Popularidad del curso favorito por género")
    st.plotly_chart(fig8, use_container_width=True)

    st.subheader("Tablas dinámicas")

    st.write("Número de estudiantes por carrera y género")
    tabla1 = df.pivot_table(index="Carrera universitaria", columns="Género",
                            aggfunc="size", fill_value=0)
    st.dataframe(tabla1)

    st.write("Promedio de mascotas por carrera")
    tabla2 = df.groupby("Carrera universitaria")["Nro Mascotas"].mean().reset_index()
    st.dataframe(tabla2)

    st.write("Edad promedio por curso favorito")
    tabla3 = df.groupby("Curso favorito")["Edad_aproximada"].mean().reset_index()
    st.dataframe(tabla3)

except FileNotFoundError:
    st.error("No se encontró el archivo datos_simulados.csv. Verifica la ruta.")
except KeyError as e:
    st.error(f"Falta la columna requerida: {e}")
except Exception as e:
    st.error(f"Ocurrió un error inesperado: {e}")
  
