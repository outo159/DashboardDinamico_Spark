import streamlit as st
import pandas as pd
import os
import datetime as dt


st.set_page_config(
    page_title="Form dashboard",
    page_icon="imagenes/icono.png"
)

st.title("Registro de estudiantes", anchor=False)

colum1,colum2,colum3 = st.columns([2,0.5,0.5])
with colum1:
    st.write("Llena tus datos en el siguiente registro")
with colum2:
    st.page_link("pages/graficas.py", label="Graficas")
with colum3:
    st.page_link("pages/info.py",label="Info")


if not os.path.exists("registro.csv"):
    df = pd.DataFrame(columns=[
        "Carrera universitaria", "Especialidad", "Ciclo académico", "Día nacimiento",
        "Mes nacimiento", "Año nacimiento", "Género",
        "Primera letra Nombre", "Almuerzo favorito",
        "Curso favorito", "Nro Mascotas"
    ])
    df.to_csv("registro.csv", index=False)

col1, col2 = st.columns([1, 1])

with col1:
    with st.form("mi_form"):
        nombre = st.text_input("Nombre")
        carrera = st.text_input("Carrera Universitaria")
        especialidad = st.text_input("Especialidad")
        ciclo = st.text_input("Ciclo academico")
        fechaNac = st.date_input(
            "Fecha de Nacimiento",
            value=dt.date(2000, 1, 1),
            min_value=dt.date(1900, 1, 1),
            max_value=dt.date.today()
        )
        genero = st.selectbox("Genero", ("--Seleccionar--", "Masculino", "Femenino", "Otro"))
        almuerzoFav = st.text_input("Almuerzo favorito")
        cursoFav = st.text_input("Curso favorito")
        numeroMasc = st.number_input("Numero de mascotas", min_value=0, step=1)
        enviar = st.form_submit_button("Registrar")

if enviar:
    st.success("Validando datos...")

with col2:
    st.image("imagenes/icono.png", width=380)

if enviar:
    diaNac = fechaNac.day
    mesNac = fechaNac.month
    yearNac = fechaNac.year
    primeraLetraNomb = nombre[0] if nombre else ""

    campos_texto = [
        nombre, carrera, especialidad, ciclo,
        almuerzoFav, cursoFav
    ]

    llenados = sum(1 for c in campos_texto if c.strip() != "")

    if llenados < 3:
        st.error("Debes llenar al menos 3 campos para registrar.")
    else:
        nuevo_dato = pd.DataFrame([[
            carrera, especialidad, ciclo, diaNac, mesNac, yearNac,
            genero, primeraLetraNomb,
            almuerzoFav, cursoFav, numeroMasc
        ]],
            columns=[
                "Carrera universitaria", "Especialidad", "Ciclo académico",
                "Día nacimiento", "Mes nacimiento",
                "Año nacimiento", "Género",
                "Primera letra Nombre", "Almuerzo favorito",
                "Curso favorito", "Nro Mascotas"
            ]
        )

        nuevo_dato.to_csv("registro.csv", mode="a", header=False, index=False)
        st.success("Registro guardado correctamente")
        st.rerun()

st.divider()

st.subheader("Registros actuales", anchor=False)

if os.path.exists("registro.csv"):
    registros = pd.read_csv("registro.csv")
    st.dataframe(registros)
else:
    st.info("Aún no se ha registrado nada")

col1, col2 = st.columns([2, 1])

with col1:
    pass

with col2:
    numero = st.number_input("Instancia a borrar", min_value=0, step=1)

    if st.button("Eliminar registro"):
        if numero in registros.index:
            registros.drop(numero, inplace=True)
            registros.to_csv("registro.csv", index=False)
            st.rerun()
        else:
            st.error("El número de instancia no existe")
