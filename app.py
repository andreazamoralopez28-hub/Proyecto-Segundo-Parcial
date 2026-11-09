import streamlit as st
import numpy as np
import time

st.set_page_config(page_title="Juego de la Vida", layout="wide")
st.title("Juego de la Vida")

filas = 20
columnas = 20
if "tablero" not in st.session_state:
    st.session_state.tablero = np.random.choice([0, 1], size=(filas, columnas), p=[0.8, 0.2])
if "corriendo" not in st.session_state:
    st.session_state.corriendo = False
def calcularGeneracion(tablero):
    nuevas_celdas = np.zeros_like(tablero)
    for i in range(tablero.shape[0]):
        for j in range(tablero.shape[1]):
            vecinos_vivos = np.sum(tablero[max(0, i-1):min(i+2, tablero.shape[0]), max(0, j-1):min(j+2, tablero.shape[1])]) - tablero[i, j]
            if tablero[i, j] == 1 and (vecinos_vivos < 2 or vecinos_vivos > 3):
                nuevas_celdas[i, j] = 0
            elif tablero[i, j] == 0 and vecinos_vivos == 3:
                nuevas_celdas[i, j] = 1
            else:
                nuevas_celdas[i, j] = tablero[i, j]
    return nuevas_celdas

st.sidebar.title("Controles")
if st.sidebar.button("Iniciar"):
    st.session_state.corriendo = True
if st.sidebar.button("Detener"):
    st.session_state.corriendo = False
if st.sidebar.button("Reiniciar"):
    st.session_state.tablero = np.random.choice([0, 1], size=(filas, columnas), p=[0.8, 0.2])
    st.session_state.corriendo = False

placeholder = st.empty()
while st.session_state.corriendo:
    st.session_state.tablero = calcularGeneracion(st.session_state.tablero)
    placeholder.table(st.session_state.tablero)
    time.sleep(0.3)

placeholder.table(st.session_state.tablero * 255, width=500, clamp=True)

if st.session_state.corriendo:
    st.session_state.tablero = calcularGeneracion(st.session_state.tablero)
    time.sleep(0.3)
    st.rerun()