# ¿CUÁNTO VALE UN CUADRO AL ÓLEO DEl MAESTRO FERNANDO BOTERO?
----------------------------------------------------------------------------------


### INTRODUCCIÓN:

El objetivo del siguiente proyecto es crear un modelo que permita valorizar de manera adecuada cualquier obra al óleo del maestro Fernando Botero.
Dicho interés surgió cuando supe que curadores valorizaban los cuadros de acuerdo a los cm2 de una obra. Mi intuición artística me hizo escéptico que fuese un método razonable para encontrar el valor de un cuadro y por eso me embarque en buscar a través de los datos otro mecanismo que resultara más adecuado. 

Es relevante indicar que el Maestro Fernando Botero se ha ganado el reconocimiento en la historia del arte mundial; sus obras se han exhibido en las mejores galerías del mundo y su estilo único, el “Boterismo”, lo hace estar entre los grandes artistas del siglo XX.

Por otra parte y de manera personal, me siento muy orgulloso del Maestro Fernando Botero, no solo por su arte sino por su humanidad. Es el artista con mayores donaciones a Colombia, reflejado en el Museo Botero en Bogotá y en el museo de Antioquia en Medellín. Además, ha donado muchas esculturas que embellecen las calles de Bogotá y Medellín. Espero que este pequeño trabajo sea también un pequeño tributo para el mejor artista de Colombia.



-----------------------------------------------------------------------------------



### ESTRUCTURA DEL PROYECTO-


1.	[DATASET](#dataset)- Explicación del dataset y sus variables. Se sube el archivo de Excel al proyecto.
   
3.	NOTEBOOKS- Son los archivos en Jupyter donde se presenta el código.
   
        a.	EDA- Está todo el proceso exploratorio de los datos donde se concluye las variables importantes.
        
        b.	MODELO 1 ML- Un modelo de recomendación usando de la librería SKLEARN-Coseno de similitud.
        
        c.	MODELO 2- Una regresión logística con las variables relevantes para explicar el valor de los cuadros de Botero.
        
        d.	MODELO 3- Un deployment usando de Streamlit para que el usuario registre atributos de un cuadro cualquiera de Botero y obtenga el cuadro más similar de acuerdo con nuestro         dataset. De esta manera, el usuario podrá saber a que precio se vendió el cuadro  más similar. Es una proxy útil para valorizar su cuadro.

5.	[REPORTE Y VISUALIZACIONES](#reporte-y-visualizaciones-mas-importantes)- Se presentan las visualizaciones más importantes del proyecto.
   
7.	[CONCLUSIONES FINALES](#conclusiones-finales)
   
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

Al quitar los dos fuertes outlyers, no mejora la distribución normal y se mantiene un sesgo hacia la derecha. El resultado de la prueba Shapiro-Wilk es: p-valor=0.0001 (quitando los dos outlyers más fuertes). Por esta razón procedemos en crear un dataset de dummies.

Indicadores relevantes de la variable precio de venta: Promedio=$902.981 USD y una Desviación Estandar= $892.194 USD


#### VARIABLE FECHA:

![image](https://github.com/user-attachments/assets/33d6679e-61a4-4f0f-877b-10e0323bcab5)


Se puede concluir que la carrera artística del maestro Fernando Botero llega a su cúspide en el periodo 1970-1990, que es cuando inicia su estilo artístico: el "Boterismo". Antes de esta década es una exploración y por eso se explica un precio promedio muy inferior al resto del dataset. Tambien en el contexto de la industría artística, entre más autenticidad de la obra, mayor su valor. Tener las obras que iniciaron su obra artística le da una mayor propuesta de valor y esto puede explicar los dos outlyers fuertes: Playroom con un precio de venta de U$3.6 millones y The musicians en U$5.13 millones, ambos elaborados en la década de 1970-1980.

Se puede apreciar una caída considerable del valor de las obras entre 1990-2010. La razón principal es que en este periodo los formatos de los cuadros son mucho más pequeños que los de la década 1970-1990. En la década de 2010-2020 retoma un formato más grande que explica el aumento de su precio, no obstante hay pocos cuadros en el dataset.


--------------------------------------

### VARIABLE TAMAÑO

![image](https://github.com/user-attachments/assets/99b4f6ba-08ab-4623-8120-de030d566d92)

Es evidente que si existe una alta correlación entre el tamaño y el precio de venta (0.7 se considera una relación fuerte). Lo interesante por anotar es que la ALTURA del cuadro es la que en mayor medida afecta el precio.

Para nuestro modelo, creamos 5 tamaños que serán las dummies para nuestro modelo:


![image](https://github.com/user-attachments/assets/f780145e-4c4a-44d7-8a96-9d990fec2399)



------------------------------------------

### VARIABLE PROVENANCE

![image](https://github.com/user-attachments/assets/5d88435f-d092-40ef-a515-a8757a9fe9a5)


La galería Marlborough en NY, es una galeria fundamental para la carrera artística del maestro Fernando Botero que lo acompaño desde 1970. Es donde inicio su carrera artística con fama mundial y donde sus obras más cotizadas en algún momento han pasado por esa galeria.

Cabe anotar que al realizar el HEATMAP, no se encontró una alta correlacion con Provenance a excepcion de la galeria Marlborough de NY con un un indicador de 0.49, que es una relación moderada y que sólo este lugar se tomará para el modelo.

---------------------------------

### VARIABLE TIEMPO DE COLECCION

![image](https://github.com/user-attachments/assets/78d170b2-9c95-4a43-90e6-38d584b84e48)


No existe evidencia que el tiempo entre la penúltima compra y la última ayude a valorizar el cuadro. Es decir, tener un cuadro por años en tu casa no va aumentar su valor. 


---------------------------------


### VARIABLE SUB O SOBRE VALORADO LOS CUADROS DE BOTERO


![image](https://github.com/user-attachments/assets/db6a806e-260d-4a52-a92e-bf8b5bc6f48e)


Podemos ver que el máximo precio que establece Christie´s para la subasta es roto en la gran mayoría de los casos. Es decir, existe evidencia que Botero está sub-valorado. Puede ser interesante verlo como una herramienta de inversión.


------------------------------------

### VARIABLE LITERATURA

![image](https://github.com/user-attachments/assets/fbfadee5-49b3-44c9-982d-3d5ce5e28f54)


Existe una relacion moderada entre 4 literaturas o más para valorizar un cuadro. 


-----------------------------

### VARIABLE EXHIBICIONES

![image](https://github.com/user-attachments/assets/52a93747-b955-46ac-b772-64d6c575a5db)


Existe una relacion moderada entre 4 exhibiciones o más.


-------------------------------

### VARIABLE TEMÁTICA

![image](https://github.com/user-attachments/assets/ce83c611-f81f-4476-bd3d-4815682d1cdc)

Es evidente que la temática GRUPO DE FIGURAS es el que mayor valoriza los cuadros. Esto tiene sentido desde el contexto artístico: las figuras es lo que mejor permite expresar el "Boterismo". El grupo de figuras arrojó una correlación fuerte de 0.68.

--------------



 ## PRIMER MODELO- EL DE ML

 ![image](https://github.com/user-attachments/assets/4459c0a8-0429-4ceb-b3e4-6da91ec386b9)

Podemos observar que al ingresar el cuadro más costoso- "The Musicians" no apareció el cuadro que le sigue en precio sino un cuadro que se vendió en 2019 por U$2 millones cuyo nombre es "Tablao Flamenco" y que debería tener un precio mucho más alto. Este cuadro está muy subvalorado y hay oportunidades de arbitraje con grandes utilidades, similar al duplicar mínimo su valor. 

 Al probarlo con todo tipo de indices, los resultados son satisfactorios del modelo.


 ------------------

 ## SEGUNDO MODELO DE REGRESIÓN 

 ![image](https://github.com/user-attachments/assets/ae2b231f-4fcd-4fe1-b784-1a2894e9ebec)


Al observar el resultado del modelo de regresión lineal se puede concluir:

   1. Un R2 alto (0.84) significa que el modelo puede explicar la variable VENTA.
   2. R2 ajustado (0.56) hay muchas variables que no son relevantes. Se creará otro modelo, quitando gran parte de la temática a excepción de "Grupo Figuras" para reducir el sobreajuste.
   3. F-estadístico (3.042) significa que el modelo SI es estadísticamente significativo.


 Al eliminar todas las variables temáticas, se obtuvo:

 ![image](https://github.com/user-attachments/assets/d2e4f7f7-d6a3-43a0-a5c7-37aa2aa458ee)


El modelo mejoró su R2 ajustado y y su F-estadístico mejoró muchisimo. El análisis de estas variables las escribimos en las conclusiones


-----------------------

## TERCER MODELO

Llega un señor y te ofrece un cuadro de Botero, ¿qué hacer? Realizamos un deployment con Streamlit para que puedas rellenar los atributos del cuadro y obtener el cuadro más similar.

![image](https://github.com/user-attachments/assets/efda038e-c325-4972-9623-fcea85611ff2)


![image](https://github.com/user-attachments/assets/abdb8e04-ffc7-41ee-aab2-75831f88fabe)


![image](https://github.com/user-attachments/assets/06973646-1da7-4137-ab79-68a8447939ba)




---------------------

# CONCLUSIONES FINALES:


1. El tamaño no es un método confiable para valorizar un cuadro del maestro Fernando Botero. Sí es una variable importante con una correlación positiva, pero muy lejos de ser un método fiable. Se requiere de un conjunto de atributos para entender el valor de un cuadro. Estas son algunos de los atributos más importantes que encontramos en el proyecto:
   
         1. Número de literatura elaborada para el cuadro (cabe anotar que esta literatura por lo general es escrita por curadores con phD o que son de galerias importantes). No es    literatura convencional o fácil de hacer; requiere de un trabajo.  
         2. Número de exhibiciones es importante tambíen. 
         3. La temática: Grupo de Figuras resulta de gran importancia. Un grupo de Figuras expresa mejor el "Boterismo" que cualquier otra temática.
         4. Los formatos pequeños reducen bastante el valor. Es probable que cuadros pequeños no puedan expresar de manera adecuada el "Boterismo".
         5. La fecha tiene importancia, especialmente si es anterior a 1970 (reduce bastante su valor).
         

3. Si eres dueño de un cuadro de Botero, estas son algunas recomendaciones:
   
         1. No tenerlo guardado en la casa sino más bien exhibirla en galerias o museos. Exhibirla al público, aumenta su reconocimiento y valor. Ideal llevarla al menos a 4 lugares (si nunca ha salido el cuadro) antes de venderlo.
         2. Llevarla a una galeria en New York. Se recomienda la galeria Marlborough y negociar un % adecuado. Este costo, vale la pena asumirlo, porque valoriza el activo mucho más que             el % de intervención de la galeria.
         3. Buscar la manera que se escriba literatura sobre el cuadro. Buscar curadores y expertos de la industria artística. 
     
4. Si te quieren vender un cuadro, estas son algunas recomendaciones:

         1. Evita tratar con curadores que venden un cuadro por cm2, por lo general te están cobrando mucho por ese cuadro. Es asumir que el cm2 de los ouytlyers pueden explicar las medidas centrales de una variable; esto es un despropósito estadístico.
         2. La fecha es clave- no asumas que entre "mas viejo mejor". Los cuadros al inicio de su carrera son los más baratos.
         3. Evitar comprar cuadros con temáticas como Bodegones o Animales o que sean pequeños.
         4. Hay oportunidades de negocio. Hay cuadros muy sub-valorados. Para este caso, Tablao Flamenco podría valer el doble del precio al que fue comprado. También hay otros cuadros de mediano formato con oportunidades de negocio. Sientete libre de usar el modelo elaborado en el proyecto para que veas cuál cuadro puede tener un futuro prometedor como inversión. No dudes en contactarme para mayor información.
