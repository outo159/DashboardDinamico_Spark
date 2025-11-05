import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Form dashboard",
    layout="wide"
)

st.title ("Registro de estudiantes", anchor=False)
colum1, colum2 =st.columns([2,1])
with colum1:
    st.write("Llena tus datos en el siguiente registro")

with colum2:
    st.page_link("pages/graficas.py",label="Graficas")

#Creamos un archivo CSV si en caso no este 
if not os.path.exists("registro.csv"):
    df=pd.DataFrame(columns=["Nombre", "Edad", "Codigo de estudiante","Correo","Cursos llevados"])
    df.to_csv("registro.csv",index=False)

#Creamos el formulario

with st.form("form_registro"):
    st.html(
        """
        <style>
        button[data-testid="stNumberInput-SetpUp"],
        button[data-testid="stNumberInput-SetpDown"]{
            display:none;
        }
        </style>
        """ )
    nombre = st.text_input("Nombre completo:")
    edad= st.number_input("Edad:",min_value=0,step=1)
    codigoEstudiante = st.number_input("Codigo de estudiante",min_value=0)
    correo = st.text_input("Correo electronico")
    cursosLlevados = st.number_input("Cursos que llevas este ciclo",min_value=0,step=1)
    enviar = st.form_submit_button("Registrar")

    if(enviar):
        if nombre and codigoEstudiante and correo and cursosLlevados:
            nuevo_dato = pd.DataFrame([[nombre,edad,codigoEstudiante,correo,cursosLlevados]], columns=["Nombre","Edad","Codigo de estudiante","Correo","Cantidad de cursos"])
            nuevo_dato.to_csv("registro.csv",mode="a",header=False,index=False)
            st.success
            st.rerun()
            st.success("Registro guardado correctamente")
        else:
            st.error("Por favor completa los campos solicitados")

#Vista de los registros que se hicieron
st.subheader("Registro actuales", anchor=False)
if os.path.exists("registro.csv"):
    registros =  pd.read_csv("registro.csv")
    st.dataframe(registros)
else:
    st.info("Aun no se ha registrado")


#Boton para descargar, eliminar la data y poder usarla en POWERBI
col1 ,col2 = st.columns([2,1])
with col1:
    if os.path.exists("registro.csv"):
        with open("registro.csv","rb") as file:
            pass
with col2:
    numero = st.number_input("Instancia a borrar",min_value=0,step=1)
    if st.button("Eliminar registro"):
        if numero in registros.index:
            registros.drop(numero,inplace=True)
            registros.to_csv("registro.csv",index=False)
            st.rerun()
        else:
            st.text_input("El numero de instancia no existe")


