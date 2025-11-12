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


# Crear archivo CSV si no existe
if not os.path.exists("registro.csv"):
    df = pd.DataFrame(columns=[
        "Carrera universitaria", "Ciclo académico", "Día nacimiento",
        "Mes nacimiento", "Año nacimiento", "Género",
        "Primera letra Nombre", "Almuerzo favorito",
        "Curso favorito", "Nro Mascotas"
    ])
    df.to_csv("registro.csv", index=False)

# FORMULARIO
col1, col2 = st.columns([1, 1])

with st.form("mi_form"):
    with col1:
        nombre = st.text_input("Nombre")
        carrera = st.text_input("Carrera Universitaria")
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

    with col2:
        left, center, right = st.columns([1, 2, 0.3])
        with center:
            st.image("imagenes/logo.jpg", width=300, use_container_width=False)
    enviar = st.form_submit_button("Registrar")

# PROCESAR FORMULARIO
if enviar:
    diaNac = fechaNac.day
    mesNac = fechaNac.month
    yearNac = fechaNac.year

    if nombre:
        primeraLetraNomb = nombre[0]
    else:
        primeraLetraNomb = ""
    if (nombre and carrera and ciclo and genero != "--Seleccionar--"
            and almuerzoFav and cursoFav):
        nuevo_dato = pd.DataFrame([[carrera, ciclo, diaNac, mesNac, yearNac, genero,primeraLetraNomb, almuerzoFav, cursoFav, numeroMasc]],
            columns=["Carrera universitaria", "Ciclo académico","Día nacimiento", "Mes nacimiento", "Año nacimiento","Género", "Primera letra Nombre", "Almuerzo favorito","Curso favorito", "Nro Mascotas"]
        )

        nuevo_dato.to_csv("registro.csv", mode="a", header=False, index=False)
        st.success("Registro guardado correctamente")
        st.rerun()

    else:
        st.error("Por favor completa los campos solicitados")

st.divider()
# MOSTRAR REGISTROS
st.subheader("Registros actuales", anchor=False)

if os.path.exists("registro.csv"):
    registros = pd.read_csv("registro.csv")
    st.dataframe(registros)
else:
    st.info("Aún no se ha registrado nada")

# ELIMINAR REGISTROS
col1, col2 = st.columns([2, 1])

with col1:
    if os.path.exists("registro.csv"):
        with open("registro.csv", "rb"):
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

