# ¿CUÁNTO VALE UN CUADRO AL ÓLEO DEl MAESTRO FERNANDO BOTERO?
----------------------------------------------------------------------------------


### INTRODUCCIÓN:

El objetivo del siguiente proyecto es crear un modelo que permita valorizar de manera adecuada cualquier obra al óleo del maestro Fernando Botero.
Dicho interés surgió cuando supe que curadores valorizaban los cuadros de acuerdo a los cm2 de una obra. Mi intuición artística me hizo escéptico que fuese un método razonable para encontrar el valor de un cuadro y por eso me embarque en buscar a través de los datos otro mecanismo que resultara más adecuado. 

Es relevante indicar que el Maestro Fernando Botero se ha ganado el reconocimiento en la historia del arte mundial; sus obras se han exhibido en las mejores galerías del mundo y su estilo único, el “Boterismo”, lo hace estar entre los grandes artistas del siglo XX.

Por otra parte y de manera personal, me siento muy orgulloso del Maestro Fernando Botero, no solo por su arte sino por su humanidad. Es el artista con mayores donaciones a Colombia, reflejado en el Museo Botero en Bogotá y en el museo de Antioquia en Medellín. Además, ha donado muchas esculturas que embellecen las calles de Bogotá y Medellín. Espero que este pequeño trabajo sea también un pequeño tributo para el mejor artista de Colombia.



-----------------------------------------------------------------------------------



### ESTRUCTURA DEL PROYECTO-

1.	DATASET- Explicación del dataset y sus variables. Se sube el archivo de Excel al proyecto.
   
3.	NOTEBOOKS- Son los archivos en Jupyter donde se presenta el código.
   
        a.	EDA- Está todo el proceso exploratorio de los datos donde se concluye las variables importantes.
        
        b.	MODELO 1 ML- Un modelo de recomendación usando de la librería SKLEARN-Coseno de similitud.
        
        c.	MODELO 2- Una regresión logística con las variables relevantes para explicar el valor de los cuadros de Botero.
        
        d.	MODELO 3- Un deployment usando de Streamlit para que el usuario registre atributos de un cuadro cualquiera de Botero y obtenga el cuadro más similar de acuerdo con nuestro         dataset. De esta manera, el usuario podrá saber a que precio se vendió el cuadro  más similar. Es una proxy útil para valorizar su cuadro.

5.	REPORTE Y VISUALIZACIONES- Se presentan las visualizaciones más importantes del proyecto.
   
7.	CONCLUSIONES FINALES
   
9.	AUTOR



---------------------------------------------------------------------------------



### DATASET:


Nuestro data set se extrajo de la página de internet Christie´s, una de la casa de subastas más prestigiosas del mundo y con una trayectoria cercana a los tres siglos. Este trabajo se realizó manualmente porque hay atributos muy complejos de realizar con un programa, por ejemplo saber categorizar si un cuadro es “figuras”, “animales” o “paisaje”, teniendo en cuenta que ninguna de ellas son figuras normales sino figuras del estilo “Boterista”.  Al momento de esta publicación, se extrajo 51 datos de cuadros vendidos a través de la casa de subastas Christie´s.

La primera coyuntura antes de extraer los datos es cómo serían registrados: como variables continuas, discretas, dummies, categóricas nominales, etc. Para resolver esta coyuntura, resolvemos en realizar un EDA a la variable precio de “Venta” para determinar si tiene sentido usar variables continuas. Por esta razón, se realizó el método Shapiro-Wilkin para determinar si la variable seguía una distribución normal. Al realizar la prueba, se rechazo la Hipótesis Nula con un p-valor a 0 dado a una cola pronunciada hacia la derecha. Incluso borrando los outlyers más fuertes, el p-valor seguía cercano a 0.

Por esta razón, se considera que la estructura de datos estilo dummies es la más adecuada para capturar los efectos categóricos de las obras de arte. Además, las dummies dan cierta flexibilidad sin asumir una linealidad estricta entre el Precio y las Variables explicativas dado que el modelo va estimar un coeficiente independiente para cada categoría dummy. Esto va a permitir capturar patrones complejos, mejorar el ajuste y que los residuos se comporten como ruido aleatorio normal. 
De tal manera, al extraer la información de la página de Christie´s, se pone 1 si tiene el aatributo o 0 si no lo tiene.

----------------------------------------------------------------------------



#### DESCRIPCIÓN DEL DATASET:


   FECHA- Se crearon dummies por décadas:
   
        a.	1950-1959
        b.	1960-1969
        c.	1970-1979
        d.	1980-1989
        e.	1990-1999
        f.	2000-2009
        g.	2010-2020

-------------------------------------------------
   
   TAMAÑO- Se extrajeron los siguientes datos sin redondear:
   
        a.	Altura
        b.	Ancho
  	
         Al realizar el proceso de clustering se decidió crear 5 clusters. En primera instancia, el método del codo lo permitía, debido a que el óptimo del hyperparametro k gira entorno    entre k=3 y 5. En segunda instancia 5 le daba mayor sentido al contexto de las obras del Maestro Fernando Botero. Estos son los 5 clusters que se volvieron dummies para el proyecto.
     	
         Las medidas son (Altura x Ancho):
     	
         I.	Pequeño-
     	
                 a.	Altura (0 -112cm)
                 b.	Ancho (0- 120 cm)
     	
         II.	Mediano-pequeño:
     	
                 a.	Altura (113 cm – 162 cm)
                 b.	Ancho (90 cm- 129 cm)
     	
         III.	Mediano-grande:
     	
                 a.	Altura (80 cm – 152 cm)
                 b.	Ancho (149cm-190cm)
       	
         IV.	Grande:
     	
                 a.	Altura (160 cm- 225cm)
                 b.	Ancho (115 cm-204cm)
     	
         V.	Colección:
     	
                 a.	Altura(200cm-240cm)
                 b.	Ancho( >300cm)

---------------------------------------------------------------------------

  
   PROVENANCE- 
   
   Los lugares en los que ha estado la obra. Una obra puede tener más de uno. En paréntesis se pone los lugares que aparecieron pero que no son dummies independientes.
   
         a.	Marlborough Gallery New York      
         b.	New York- (Familias, coleccionistas y otras galerías)
         c.	USA- (California, Miami, Florida)
         d.	Hong Kong
         e.	Londres
         f.	Francia- (Paris y Nantes)
         g.	Europa – (Suiza, Italia, Belgica, Alemania)
         h.	Colombia- (Cuando no se especifica nada)
         i.	LATAM- (Mexico, Venezuela)
         j.	Dubai
         k.	Sur-Africa

---------------------------------------------------------------------------------
   
   LUGAR ÚLTIMA COMPRA- 
   El lugar donde se compro la última vez el cuadro.
   
       a.	New York
       b.	USA
       c.	Londres
       d.	Francia
       e.	Europa
       f.	LATAM
       g.	Colombia
       h.	Hong Kong
       i.	Canada

   ------------------------------------------------------------------
   
   PERIODO DE COLECCIONISTA-
   
       a.	Última compra- el año de la última venta
       b.	Penúltima compra- el año de la penúltima venta.

   ------------------------------------------------------------------
   
   SUB O SOBRE VALORADO-
   
       a.	MIN- El precio mínimo que establece Christie´s
       b.	MAX- El precio máximo de Christie´s
   
   --------------------------------------------------------------------------
   
   LITERATURA- Las referencias literarias que aparecen sobre el cuadro.
   
       a.	4 o más literaturas
       b.	Menos de 4 literaturas

   ---------------------------------------------------------------------------------
   
   EXHIBICIÓN DE LA OBRA- 
      
      Museos y galerías donde se ha exhibido la obra.
      
          a.	4 o más exhibiciones.
          b.	Menos de 4 exhibiciones

   ----------------------------------------------------------------------------------
   
   TEMÁTICA DE LA OBRA- (Puede tener más de 1 categoría)
   
       a.	1 figura- 1 figura humana de cualquier tipo que sea el centro del tema del cuadro. Si por ejemplo, es 1 figura pequeña y hay un paisaje o bodegón mucho mas importante, el tema NO sería 1 figura.
       b.	2 figuras- 2 figuras humanas de similares proporciones y que estén interactuando y sea el centro del tema.
       c.	Grupo de figuras- 3 o más figuras humanas que están realizando algo en conjunto.
       d.	Bodegón- Objetos inanimados. NO es un paisaje.
       e.	Animales- Cuando el animal es grande y parte importante del cuadro.
       f.	Escenas urbanas- Cuando hay referencia a ciudades
       g.	Escenas rurales- Pueblos y casas campesinas.
       h.	Escena hogar- Los lugares de un hogar: habitación, cocina, sala, etc.
       i.	Histórico- Si son personajes históricos: Goya, Vermeer, etc.
       j.	Político- Temas como la pobreza, violencia.
       k.	Religión- Cualquier referencia por pequeña que sea; una cruz, ángel pequeño, etc.
       l.	Desnudo/Erótico- No debe ser explícito con un desnudo si la pose de la figura es sugestiva.
       m.	Paisaje- Cuando el paisaje se vuelve el centro del cuadro. No es sólo un medio sino un fin.
       n.	Personal- Eventos personales propios del artista como la primera comunión, amigos, famliares y autoretratos.
       o.	Carbon- Técnica al carbón. Sólo se incluyó como referencia al oleo.
       p.	Búsqueda (sin “Boterismo”)- Estos cuadros tratan del inicio de su carrera donde explora diferentes estilos.


------------------------------------------------------------------------

### REPORTE Y VISUALIZACIONES MÁS IMPORTANTES:

No existe evidencia que el precio de venta siga una distribución normal. 

![image](https://github.com/user-attachments/assets/a4b2a6a5-f883-4054-9045-91da47780d5e)

Al quitar los dos fuertes outlyers, no mejora la distribución normal y se mantiene un sesgo hacia la derecha. El resultado de la prueba Shapiro-Wilk es: p-valor=0.0001 (quitando los dos outlyers más fuertes. Por esta razón procedemos en crear un dataset de dummies.






 
