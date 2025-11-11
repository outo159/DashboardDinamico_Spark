import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(
    page_title="Informacion sobre nosotros",
    page_icon="imagenes/icono.png"
)

#CArgar el csv
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ejemregis.csv"))
prog_df = pd.read_csv(csv_path)

st.dataframe(prog_df)

st.title("Informacion sobre el proyecto", anchor=False)
col1, col2 = st.columns([1,1])
with col1:
    st.write("""
         Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
         Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
         nisi ut aliquip ex ea commodo consequat.
         Duis aute irure dolor in reprehenderit in voluptate velit esse
         cillum dolore eu fugiat nulla pariatur.
         Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
         officia deserunt mollit anim id est laborum.
         """)
with col2:
    st.write("""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
         Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
         nisi ut aliquip ex ea commodo consequat.
         Duis aute irure dolor in reprehenderit in voluptate velit esse
         cillum dolore eu fugiat nulla pariatur.
         Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
         officia deserunt mollit anim id est laborum.
             """)
st.divider()
st.subheader("Informacion sobre el proyecto", anchor=False)
col1, col2 = st.columns([1,1])
with col1:
    with st.expander("Loren ipsum dolor sit amet",expanded=True):
        fig = px.pie(prog_df,
                    values='Edad',
                    names='Carrera',
                    title='Relacion carrera edad')
        st.plotly_chart(fig, use_container_width=True, key="pie1")
with col2:
    st.write("""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
         Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
         nisi ut aliquip ex ea commodo consequat.
         Duis aute irure dolor in reprehenderit in voluptate velit esse
         cillum dolore eu fugiat nulla pariatur.
         Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
         officia deserunt mollit anim id est laborum.
             """)
st.divider()
col1, col2 = st.columns([1,1])

with col1:
    st.write("""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
         Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
         Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
         nisi ut aliquip ex ea commodo consequat.
         Duis aute irure dolor in reprehenderit in voluptate velit esse
         cillum dolore eu fugiat nulla pariatur.
         Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
         officia deserunt mollit anim id est laborum.
             """)
with col2:
    fig2 = px.pie(
        prog_df,
        values='Edad',
        names='Carrera',
        title='Relacion carrera edad')

    st.plotly_chart(fig2, use_container_width=True, key="pie2")
