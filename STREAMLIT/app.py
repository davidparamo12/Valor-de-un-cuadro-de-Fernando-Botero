# app.py
import streamlit as st
import pandas as pd

# Cargar tu dataframe


@st.cache_data
def cargar_datos():
    return pd.read_excel(r"C:\Users\param\OneDrive\Escritorio\Programacion\Botero\Datos_modelo_botero.xlsx") 


df_botero = cargar_datos()

# Entradas del usuario
st.title("🎨 Recomendador de Obras de Botero")

st.header("Selecciona las características deseadas")

# Tamaños (solo uno activo a la vez)
tam_seleccionado = st.radio("Tamaño", [
    'tamaño_colección', 'tamaño_grande', 'tamaño_mediano-grande',
    'tamaño_mediano-pequeño', 'tamaño_pequeño'
], index=None)

# Checkboxes adicionales
filtros_binarios = {
    'Mas de 4 exhibiciones': st.checkbox('Más de 4 exhibiciones'),
    'Mas de 4 literaturas': st.checkbox('Más de 4 literaturas'),
    'Marlborough NY_paso': st.checkbox('Pasó por Marlborough NY')
}

# Décadas
decada = st.selectbox("Década", [
    '', '50-59', '60-69', '70-79', '80-89', '90-99', '2000-09', '2010-2019'
])

# Temática
tematica = st.selectbox("Temática", [
    '', '1 figura', '2 Figuras', 'Grupo de figuras', 'Bodegon', 'Animales',
    'Escenas urbanas/figuras', 'Escenas rurales/Figuras',
    'Escena hogar/ figuras', 'Historico', 'Politico', 'Religion',
    'Desnudo/ Erotico', 'Paisaje', 'Personal', 'Carbon', 'Busqueda(sin Boterismo)'
])

# Botón para ejecutar el filtrado
if st.button("Buscar obras recomendadas"):
    # Construir diccionario de entrada
    entrada_usuario = {tam_seleccionado: 1} if tam_seleccionado else {}
    entrada_usuario.update({k: 1 for k, v in filtros_binarios.items() if v})
    if decada:
        entrada_usuario[decada] = 1
    if tematica:
        entrada_usuario[tematica] = 1

    from logica_botero import filtrar_por_entrada
    # asegúrate de importar tu función

    resultados = filtrar_por_entrada(entrada_usuario, df_botero)

    if resultados:
        st.success(f"Se encontraron {len(resultados)} obras recomendadas.")
        st.subheader("🎯 Obras recomendadas:")
        st.dataframe(df_botero.loc[resultados][['Nombre cuadro', 'Venta', 'URL']])
    else:
        st.warning("No se encontraron coincidencias exactas, pero se muestran las más similares.")
        st.subheader("🎨 Obras más similares encontradas:")
        st.dataframe(df_botero.loc[resultados][['Nombre cuadro', 'Venta', 'URL']])

