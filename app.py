#Juego de la Vida

import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="Juego de la Vida", layout="wide")
st.title("Juego de la Vida")

st.sidebar.title("Configuración")

filas = st.sidebar.slider("Número de filas", min_value=10, max_value=50, value=20, step=5)
columnas = st.sidebar.slider("Número de columnas", min_value=10, max_value=50, value=20, step=5)
velocidad = st.sidebar.slider("Velocidad", min_value=0.05, max_value=1.0, value=0.2, step=0.05)

if "tablero" not in st.session_state or st.session_state.tablero.shape != (filas, columnas):
    st.session_state.tablero = np.random.choice([0, 1], size=(filas, columnas), p=[0.8, 0.2])
    st.session_state.generacion = 0

if "corriendo" not in st.session_state:
    st.session_state.corriendo = False
if "generacion" not in st.session_state:
    st.session_state.generacion = 0

st.sidebar.markdown("---")
st.sidebar.subheader("Controles")
if st.sidebar.button("Iniciar"):
    st.session_state.corriendo = True
if st.sidebar.button("Detener"):
    st.session_state.corriendo = False
if st.sidebar.button("Reiniciar Tablero"):
    st.session_state.tablero = np.random.choice([0, 1], size=(filas, columnas), p=[0.8, 0.2])
    st.session_state.generacion = 0
    st.session_state.corriendo = False

def calcularGeneracion(tablero):
    nuevas_celdas = np.zeros_like(tablero)
    f, c = tablero.shape
    for i in range(f):
        for j in range(c):
            vecinos_vivos = np.sum(tablero[max(0, i-1):min(i+2, f), max(0, j-1):min(j+2, c)]) - tablero[i, j]
            if tablero[i, j] == 1 and (vecinos_vivos < 2 or vecinos_vivos > 3):
                nuevas_celdas[i, j] = 0
            elif tablero[i, j] == 0 and vecinos_vivos == 3:
                nuevas_celdas[i, j] = 1
            else:
                nuevas_celdas[i, j] = tablero[i, j]
    return nuevas_celdas

st.write(f"Generacion: {st.session_state.generacion}")

placeholder = st.empty()

escala = 20
tablero_ampliado = np.repeat(np.repeat(st.session_state.tablero, escala, axis=0), escala, axis=1) * 255
placeholder.image(tablero_ampliado, width=400, clamp=True)

if st.session_state.corriendo:
    st.session_state.tablero = calcularGeneracion(st.session_state.tablero)
    st.session_state.generacion += 1
    time.sleep(velocidad)
    st.rerun()