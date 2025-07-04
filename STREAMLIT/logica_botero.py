
import pandas as pd

df_botero = pd.read_excel(
    r"C:\Users\param\OneDrive\Escritorio\Programacion\Botero\Datos_modelo_botero.xlsx")


def filtrar_por_entrada(entrada_usuario, df_botero):
    df_filtrado = df_botero.copy()
    df_coincidencia_exacta = df_filtrado.copy()
    df_mas_cercanos = df_filtrado.copy()

    print(f"Total inicial: {len(df_filtrado)} registros")

    # --- 1. Filtro por TAMAÑO ---
    tamaños = [
        'tamaño_colección', 'tamaño_grande', 'tamaño_mediano-grande',
        'tamaño_mediano-pequeño', 'tamaño_pequeño'
    ]
    for tam in tamaños:
        if entrada_usuario.get(tam, 0) == 1:
            df_coincidencia_exacta = df_filtrado[df_filtrado[tam] == 1]
            if not df_coincidencia_exacta.empty:
                df_mas_cercanos = df_coincidencia_exacta.copy()
            print(
                f"Filtrado por tamaño: {tam} → {len(df_coincidencia_exacta)} resultados")
            break

    # --- 2. Más de 4 exhibiciones ---
    if entrada_usuario.get('Mas de 4 exhibiciones', 0) == 1:
        df_coincidencia_exacta = df_coincidencia_exacta[
            df_coincidencia_exacta['Mas de 4 exhibiciones'] == 1]
        if not df_coincidencia_exacta.empty:
            df_mas_cercanos = df_coincidencia_exacta.copy()
        print(
            f"Filtrado por más de 4 exhibiciones → {len(df_coincidencia_exacta)} resultados")

    # --- 3. Más de 4 literaturas ---
    if entrada_usuario.get('Mas de 4 literaturas', 0) == 1:
        df_coincidencia_exacta = df_coincidencia_exacta[df_coincidencia_exacta['Mas de 4 literaturas'] == 1]
        if not df_coincidencia_exacta.empty:
            df_mas_cercanos = df_coincidencia_exacta.copy()
        print(
            f"Filtrado por más de 4 literaturas → {len(df_coincidencia_exacta)} resultados")

    # --- 4. Marlborough NY ---
    if entrada_usuario.get('Marlborough NY_paso', 0) == 1:
        df_coincidencia_exacta = df_coincidencia_exacta[df_coincidencia_exacta['Marlborough NY_paso'] == 1]
        if not df_coincidencia_exacta.empty:
            df_mas_cercanos = df_coincidencia_exacta.copy()
        print(
            f"Filtrado por paso por Marlborough NY → {len(df_coincidencia_exacta)} resultados")

    # --- 5. Década ---
    decadas = ['50-59', '60-69', '70-79',
               '80-89', '90-99', '2000-09', '2010-2019']
    for dec in decadas:
        if entrada_usuario.get(dec, 0) == 1:
            df_coincidencia_exacta = df_coincidencia_exacta[df_coincidencia_exacta[dec] == 1]
            if not df_coincidencia_exacta.empty:
                df_mas_cercanos = df_coincidencia_exacta.copy()
            print(
                f"Filtrado por década: {dec} → {len(df_coincidencia_exacta)} resultados")
            break

    # --- 6. Temática ---
    tematicas = [
        '1 figura', '2 Figuras', 'Grupo de figuras', 'Bodegon', 'Animales',
        'Escenas urbanas/figuras', 'Escenas rurales/Figuras',
        'Escena hogar/ figuras', 'Historico', 'Politico', 'Religion',
        'Desnudo/ Erotico', 'Paisaje', 'Personal', 'Carbon', 'Busqueda(sin Boterismo)'
    ]
    for tema in tematicas:
        if entrada_usuario.get(tema, 0) == 1:
            df_coincidencia_exacta = df_coincidencia_exacta[df_coincidencia_exacta[tema] == 1]
            if not df_coincidencia_exacta.empty:
                df_mas_cercanos = df_coincidencia_exacta.copy()
            print(
                f"Filtrado por temática: {tema} → {len(df_coincidencia_exacta)} resultados")
            break

    columnas_a_mostrar = ['Nombre cuadro', 'URL', 'Venta']

    # --- Si hay coincidencias exactas ---
    if not df_coincidencia_exacta.empty:
        print(
            f"\n✅ Estas obras tienen las mismas condiciones exactas. Estos son sus índices:")
        df_coincidencia_exacta = df_coincidencia_exacta[columnas_a_mostrar].copy(
        )
        df_coincidencia_exacta['Índice'] = df_coincidencia_exacta.index
        print(df_coincidencia_exacta[['Índice'] + columnas_a_mostrar])
        return df_coincidencia_exacta['Índice'].tolist()

    # --- Si no hay coincidencias exactas, mostrar las más similares ---
    print(f"\n⚠️ No hay un cuadro con todas las condiciones, pero estos son los más parecidos:\n")
    df_mas_cercanos = df_mas_cercanos[columnas_a_mostrar].copy()
    df_mas_cercanos['Índice'] = df_mas_cercanos.index

    for _, fila in df_mas_cercanos.iterrows():
        print(f"Índice: {fila['Índice']}")
        print(f"  🎨 Nombre: {fila['Nombre cuadro']}")
        print(f"  🔗 URL: {fila['URL']}")
        print(f"  💰 Venta: {fila['Venta']}\n")

    return df_mas_cercanos['Índice'].tolist()
