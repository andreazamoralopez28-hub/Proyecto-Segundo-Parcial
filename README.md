# Juego de la Vida

## Resumen
Este documento contiene el extenso técnico correspondiente al desarrollo la aplicación el "Juego de la Vida",
el cuál está basado en el modelo propuesto por John Conway.
La aplicación fue estructurada usando el lenguaje de programación Python, usando las librerías de NumPy la cual ess la adecuada para la vectorización de matrices numéricas. así como Streamlit para el despliegue en tiempo real de una interfaz web interactiva.

.    <img width="389" height="225" alt="image" src="https://github.com/user-attachments/assets/dfa8f565-c3c3-4de1-baa3-246357b7b752" />
.   <img width="389" height="225" alt="image" src="https://github.com/user-attachments/assets/416eadb9-92c1-4cab-ae9f-ea2aff23aa2f" />

## Introducción: Problema 
### ¿Que necesidad aborda este proyecto?
En el ámbito de la informática así como la biología, existe la necesidad de comprender como sistemas formados por elementos
simples y comunes pueden generar comportamientos complejos a una escala mayor y de forma autónoma que surgen en base a una serie de factores que se deben cumplir para dar lugar a cambios dentro del entorno.
El Juego de la Vida aborda este problema simulando la evolución de células en una cuadrícula basándose únicamente en el estado de sus 8 vecinos inmediatos.
Esta simulación permite analizar la autogeneración, auto reorganización y la lógica del algoritmo sin requerir de una intervención continua de un usuario.

## Introducción: objetivos
### Objetivo General
Desarrollar el Juego de la Vida en una página web interactivo usando Streamlit con procesamiento de matrices.
### Objetivos específicos
1. Implementar reglas de algoritmos que permitan la evaluación basandose en la vecindad de Moore para determinar el estado de supervivencia o muerte de cada cuadrícula.
2. Incluir botones básicos de accion para iniciar, detener o reiniciar el programa.
3. Incorporar deslizadores para que el usuario modifique las dimensiones de la cuadricula, así como la velocidad de ejecución en la misma.

## Solución y Evidencia
### Lógica del Programa
La evolución de las células se calcula mediante una función dedicada que analiza los límites de la matriz y suma los vecinos vivos que se encuentra alrededor según el modelo matemático de Conway y vecindad de Moore.
```python
def calcularGeneracion(tablero):
    nuevas_celdas = np.zeros_like(tablero)
    f, c = tablero.shape
    for i in range(f):
        for j in range(c):
            # Cálculo de la vecindad de Moore restando la celda actual
            vecinos_vivos = np.sum(tablero[max(0, i-1):min(i+2, f), max(0, j-1):min(j+2, c)]) - tablero[i, j]
            if tablero[i, j] == 1 and (vecinos_vivos < 2 or vecinos_vivos > 3):
                nuevas_celdas[i, j] = 0
            elif tablero[i, j] == 0 and vecinos_vivos == 3:
                nuevas_celdas[i, j] = 1
            else:
                nuevas_celdas[i, j] = tablero[i, j]
    return nuevas_celdas
```
### Escalado de Matriz y Visualización
Para convertir las celdas booleanas en imágenes escaladas que sean visualizadas como cuadros negros o blancos se ha aplicado la funcion de NumPy np.repeat.
```python
escala = 20
tablero_ampliado = np.repeat(np.repeat(st.session_state.tablero, escala, axis=0), escala, axis=1) * 255
placeholder.image(tablero_ampliado, width=400, clamp=True)
```
<img width="1273" height="919" alt="Captura de pantalla 2026-11-08 191058" src="https://github.com/user-attachments/assets/67664a07-f786-404d-98f6-6f24e415ce8f" />
<img width="1853" height="1209" alt="Captura de pantalla 2026-11-08 193736" src="https://github.com/user-attachments/assets/6776713f-a557-4f8b-9caf-07e5c4112124" />

### Botones y Gestión de estados interactivos
Para permitirse cambiar el estado lógico de la aplicación se implementaron controles ubicados en la barra lateral que posibilitan iniciar, pausar o reiniciar el tablero por completo con valores aleatorios.
```python
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
```
<img width="240" height="238" alt="Captura de pantalla 2026-11-08 211426" src="https://github.com/user-attachments/assets/44de47d7-bb90-4944-ab32-6ae66647cdf2" />

### Deslizadores para  Parámetros Dinámicos
Para lograr que el usuario tenga la posibilidad de ajustar dentro de un alcance configurado, los valores de ejecución de la matriz se implementaron deslizadores que controlan ya sea el número de filas, columnas y velocidad de actualización en segundos.
```python
filas = st.sidebar.slider("Número de filas", min_value=10, max_value=50, value=20, step=5)
columnas = st.sidebar.slider("Número de columnas", min_value=10, max_value=50, value=20, step=5)
velocidad = st.sidebar.slider("Velocidad", min_value=0.05, max_value=1.0, value=0.2, step=0.05)
```
<img width="289" height="321" alt="Captura de pantalla 2026-11-08 211824" src="https://github.com/user-attachments/assets/a98bbf9e-f733-4644-a720-feaba67fab05" />

### Funcionamiento de la Interfaz
### Estado por Default
<img width="917" height="627" alt="Captura de pantalla 2026-11-08 212019" src="https://github.com/user-attachments/assets/27be73f5-eea9-4442-9022-e3714dc97be8" />

### Ajuste de Parámetros
<img width="917" height="627" alt="Captura de pantalla 2026-11-08 212019" src="https://github.com/user-attachments/assets/f34b15af-7695-4d33-8857-f26fce185a4d" />

### Ejecución
<img width="917" height="627" alt="Captura de pantalla 2026-11-08 212019" src="https://github.com/user-attachments/assets/bcf39fe8-965e-4559-9162-985cf539971c" />

## Conclusiones
El desarrollo de este proyecto permitió aplicar de manera integrada conceptos matemáticos, científicos, e informáticos, así como la creación y diseño de aplicaciones web dinámicas en Python. 
Se logro la creación de una aplicación simulando el juego de la vida que nos permite visualizar comportamientos lógicos y aleatorios en comportamientos dinámicos dentro de una interfaz web ligera mediante Streamlit.

## Reproducibilidad
Para clonar, instalar y ejecutar este proyecto en cualquier equipo local, sigue las instrucciones detalladas a continuación:
### Requisitos del sistema
**Python** versión 3.8 o superior (En caso de no tener python verifica en tu sistema la version e instalala).
**Gestor de paquetes:** `pip`actualizado.
**Control de versiones:** `git` instalado en la terminal

### Pasos de Instalación y Ejecución
Abre la terminal o consola de comandos de tu sistema y clona el proyecto desde GitHub hacia tu equipo local:
```bash
   git clone https://github.com/andreazamoralopez28-hub/Proyecto-Segundo-Parcial.git
   cd <Nombre de la carpeta>
```
#### Instalar Dependencias
Dentro de la carpeta que se creo, abre la terminal del comando y ejecuta:

Windows.
```bash
pip install -r requirements.txt
```
MacOs.
```bash
python3 -m pip install -r requirements.txt
```

### Ejecución VS CODE
Abre VS Code, da clic en open folder 
<img width="363" height="201" alt="Captura de pantalla 2026-11-08 213815" src="https://github.com/user-attachments/assets/1a20b98a-f518-4f15-a3c9-e198efc17df9" />

selecciona la carpeta que clonaste
<img width="196" height="232" alt="Captura de pantalla 2026-11-08 213948" src="https://github.com/user-attachments/assets/97e19735-04f0-49a2-bb5b-6387def65269" />

da clic en select folder y selecciona el archivo llamado app.py
<img width="303" height="138" alt="Captura de pantalla 2026-11-08 214046" src="https://github.com/user-attachments/assets/5e06cb6f-eb23-4855-8fe6-c17369b90f20" />

abre la terminal dentro de VS code (puedes usar ctrl + ñ), y ejecuta el siguiente comando:
```bash
 streamlit run app.py
```
### Ejecución en terminal del sistema

Puedes ejecutarlo en la terminal de **Windows** de tu equipo ubicando la ruta de la carpeta en donde se encuentra el proyecto.
```bash
python -m streamlit run app.py
```
Comando para **MacOs**.
```bash
python3 -m streamlit run app.py
```

Da clic en enter y se desplegara la interfaz web con el programa listo para usar.

### Como usar
Da clic en iniciar despues de haber ajustado los parámetros a tu conveniencia.
<img width="809" height="603" alt="Captura de pantalla 2026-11-08 214932" src="https://github.com/user-attachments/assets/ea4ec21d-145e-42de-ac64-2d57b10b08a4" />

Da clic en detener para pausar la simulación.
<img width="809" height="603" alt="Captura de pantalla 2026-11-08 214932" src="https://github.com/user-attachments/assets/e02edb8d-fe82-42f2-a5b0-be2bb66a4c89" />

Da clic en Reiniciar Tablero para restaurar la cuadricula.
<img width="809" height="603" alt="Captura de pantalla 2026-11-08 214932" src="https://github.com/user-attachments/assets/d39710e5-a2de-4e19-b461-e3f1bf9dead5" />

## Listo!
### Disfruta de la simulación del Juegos de la Vida :)

## Licencia

Eres libre de utilizar, modificar, copiar y distribuir este código con fines académicos o personales, siempre y cuando se reconozca la autoría original del proyecto.





