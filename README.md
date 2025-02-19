# Laboratorio-2-PDS
## OBJETIVO
El presente laboratorio tiene como objetivo analizar y comprender las operaciones fundamentales del procesamiento digital de señales, incluyendo la convolución de señales discretas, la correlación entre señales sinusoidales y el análisis de señales fisiológicas reales, mediante la aplicación de métodos analíticos y herramientas de software como Python, con el fin de caracterizar y extraer información relevante de las señales en el dominio del tiempo y la frecuencia.
## Procedimiento
Este laboratorio se divide en tres secciones principales, cada una diseñada para explorar diferentes aspectos del procesamiento digital de señales: convolución de señales discretas, correlación de señales sinusoidales y análisis de señales fisiológicas reales. Para la primera sección Se definieron dos señales discretas:
- h[n]: La señal de respuesta al impulso, cuyos valores corresponden a los dígitos del código de estudiante.
* x[n]: La señal de entrada, cuyos valores corresponden a los dígitos del número de cédula del estudiante.\
Con la intención de realizar la convolución respectiva de cada uno de los 3 estudiantes como se evidencia en la imagen mediante las sumatorias y realizando su respectiva representación gráfica, consiguiente a esto se implementó el mismo proceso en python de la siguiente manera:
### Librerias
Las librerias específicas para realizar la convolución de las señales son:
 ```ruby
import scipy
import matplotlib.pyplot as plt
import numpy as np
import wfdb
```
- scipy: Es una librería para computación científica. Es necesaria para funciones más avanzadas de procesamiento de señales.
* matplotlib.pyplot as plt: Se utiliza para crear gráficos y visualizaciones.
* numpy as np: Es la librería fundamental para computación numérica en Python. Se utiliza para trabajar con arreglos (arrays) y realizar operaciones matemáticas.
* wfdb: Esta librería es para trabajar con datos de señales fisiológicas, como electrocardiogramas (ECG).\
### Definición del eje temporal
 ```ruby
n1 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
```
En principio se crea un arreglo NumPy llamado n1 que representa el eje temporal o el índice de los resultados de la convolución. Los valores van de 0 a 15, lo que indica que los resultados de la convolución tendrán aproximadamente 16 muestras.
### Convolución
A continuación se expondrá el proceso de convolución mediante python se utilizará como ejemplo la convolución de carol y su respectiva respresentación gráfica cabe resaltar que para cada convolución el proceso es el mismo.
 ```ruby
cco = np.array([1,0,0,3,7,4,2,0,3,9])
cce = np.array([5,6,0,0,6,6,4])
ccon = np.convolve(cco,cce,mode='full')
print("\nConvolución Carol:",ccon)
fig, ax = plt.subplots()
ax.stem(n1,ccon,'m')
plt.xlabel("n")
plt.ylabel("Resultado convolución")
plt.title("Convolución Carol")
plt.grid()
plt.show()
```
- cco: Es un arreglo que representa el "código" de Carol.
* cce: Es un arreglo que representa la "cédula" de Carol.
* ccon = np.convolve(cco, cce, mode='full'): Esta línea realiza la convolución de los arreglos cco y cce.
* np.convolve() es la función de NumPy para realizar la convolución.
* mode='full' indica que la convolución se calculará para todos los puntos de superposición, lo que resultará en un arreglo de longitud len(cco) + len(cce) - 1.
* print("\nConvolución Carol:", ccon): Imprime el resultado de la convolución en la consola.
### Visualización
- fig, ax = plt.subplots(): Crea una figura y un eje para el gráfico.
* ax.stem(n1, ccon, 'm'): Crea un gráfico (stem plot) que muestra los resultados de la convolución.
* n1 es el eje x (el índice).
* ccon es el eje y (los valores de la convolución).
* plt.xlabel(), plt.ylabel(), plt.title(): Establecen las etiquetas de los ejes y el título del gráfico.
* plt.grid(): Agrega una cuadrícula al gráfico para una mejor organización de este.
* plt.show(): Muestra el gráfico.
