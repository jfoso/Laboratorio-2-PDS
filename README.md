# Laboratorio-2-PDS
## OBJETIVO
El presente laboratorio tiene como objetivo analizar y comprender las operaciones fundamentales del procesamiento digital de señales, incluyendo la convolución de señales discretas, la correlación entre señales sinusoidales y el análisis de señales fisiológicas reales, mediante la aplicación de métodos analíticos y herramientas de software como Python, con el fin de caracterizar y extraer información relevante de las señales en el dominio del tiempo y la frecuencia.
## Procedimiento
Este laboratorio se divide en tres secciones principales, cada una diseñada para explorar diferentes aspectos del procesamiento digital de señales: convolución de señales discretas, correlación de señales sinusoidales y análisis de señales fisiológicas reales. Para la primera sección Se definieron dos señales discretas:
- h[n]: La señal de respuesta al impulso, cuyos valores corresponden a los dígitos del código de estudiante.
* x[n]: La señal de entrada, cuyos valores corresponden a los dígitos del número de cédula del estudiante.\
Con la intención de realizar la convolución respectiva de cada uno de los 3 estudiantes como se evidencia en las imagenes mediante las sumatorias y realizando su respectiva representación gráfica a mano:
![WhatsApp Image 2025-02-20 at 10 51 50 AM](https://github.com/user-attachments/assets/5abd5087-49c2-4b9a-9a80-e8cec599b554)
![WhatsApp Image 2025-02-20 at 10 51 51 AM](https://github.com/user-attachments/assets/d8a08b18-c536-4c5a-8700-94a256372f85)
![WhatsApp Image 2025-02-20 at 10 53 49 AM](https://github.com/user-attachments/assets/b9411bdc-80cd-4b7c-82cc-459b388a9994)
![WhatsApp Image 2025-02-20 at 10 51 51 AM](https://github.com/user-attachments/assets/717d153d-b7ec-4e2a-9b78-c843905e1d28)
![WhatsApp Image 2025-02-20 at 10 59 16 AM](https://github.com/user-attachments/assets/493930a4-d0d8-46aa-b8c1-716c69e80924)

 Consiguiente a esto se implementó el mismo proceso en python de la siguiente manera:
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
![WhatsApp Image 2025-02-14 at 9 13 38 PM](https://github.com/user-attachments/assets/09634d58-8000-4ae9-914a-2d400d5b35da)
![WhatsApp Image 2025-02-14 at 9 12 54 PM](https://github.com/user-attachments/assets/20480566-78ab-4eb0-8833-2a17ca73cc81)
![WhatsApp Image 2025-02-14 at 9 13 14 PM](https://github.com/user-attachments/assets/08945b45-0a02-4395-88c6-9ced0996eb06)

### Visualización
- fig, ax = plt.subplots(): Crea una figura y un eje para el gráfico.
* ax.stem(n1, ccon, 'm'): Crea un gráfico (stem plot) que muestra los resultados de la convolución.
* n1 es el eje x (el índice).
* ccon es el eje y (los valores de la convolución).
* plt.xlabel(), plt.ylabel(), plt.title(): Establecen las etiquetas de los ejes y el título del gráfico.
* plt.grid(): Agrega una cuadrícula al gráfico para una mejor organización de este.
* plt.show(): Muestra el gráfico.
## Convolución señales dadas 
Para el siguiente punto del laboratorio se ha encontrado la correlacion de dos señales: $𝑥1[𝑛𝑇𝑠] = cos(2𝜋100𝑛𝑇𝑠)$ para $0 ≤ 𝑛 < 9$ , $𝑥2[𝑛𝑇𝑠] = sin(2𝜋100𝑛𝑇𝑠)$ para 0 ≤ 𝑛 < 9  para 𝑇𝑠 = 1.25𝑚s. Con la intención de encontrar la representación gráfica y secuencial de las mismas de la siguiente manera:
```ruby
# Señales dadas
n2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
x1 = np.cos(2 * np.pi * 100 * n2 * 1.25e-3)
x2 = np.sin(2 * np.pi * 100 * n2 * 1.25e-3)

# Correlación cruzada
corr = np.correlate(x1, x2, mode='full')
print("Correlación señales dadas: ", corr)

# Gráfico de la correlación
tc = np.arange(-len(n2) + 1, len(n2))
plt.figure(figsize=(10, 4))
plt.stem(tc, corr, 'k')
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Convolución señales dadas")
plt.grid()
plt.show()
```
### Correlación cruzada
- np.correlate(x1, x2, mode='full'): Calcula la correlación cruzada entre x1 y x2. El modo 'full' asegura que se calcule la correlación para todos los posibles desplazamientos de la señal. La correlación cruzada mide la similitud entre dos señales a medida que una se desplaza con respecto a la otra.
* print(...): Imprime el resultado de la correlación.
* Posterior a esto se realiza el grafico de la correlación.\
Donde se obtuvo el siguiente resultado:
![image](https://github.com/user-attachments/assets/d89e1371-ddeb-4395-ad80-e58eb3700623)

## Adquisición y Análisis de Datos ECG
Posterior a esto se descargará una señal de la base de datos physionet en este caso es una señal ECG para caracterizar la señal en función del tiempo calculando sus estadisticos utilizando la libreria numpy y realizando su respectivo grafico de la siguiente manera :
```ruby
# Adquirir datos
ruta = 'C:\\Users\\sachi\\OneDrive - unimilitar.edu.co\\Sexto semestre\\Lab señales\\Lab 2\\ecg-id-database-1.0.0\\Person_35\\rec_4'
record = wfdb.rdrecord(ruta, channels=[1])
signal = record.p_signal
fs = record.fs
muestreo = int(5 * fs)
print("\nFrecuencia de muestreo = ", fs)

time = [i / fs for i in range(len(signal))]
signal = signal[:muestreo]
time = time[:muestreo]

# Estadísticos descriptivos numpy
print("\nEstadísticos descriptivos señal")
print("Promedio: ", np.mean(signal))
print("Varianza: ", np.var(signal))
print("Desviación estándar: ", np.std(signal))
print("Coeficiente de variación: ", np.std(signal) / np.mean(signal))
```
![image](https://github.com/user-attachments/assets/e1d3360e-ec5a-4a63-8d1f-9c12fe86396c)
Para los estadísticos de la señal obtuvimos que: 
* Promedio: -8.39999999999998e-05
* Varianza: 0.019397332944
* Desviación estándar: 0.1392743082696877
* Coeficiente de variación: -1658.027479401048

### Transformada de Fourier y Densidad Espectral de Potencia (PSD)
Para culminar la práctica de laboratorio se aplicará la transformada de fourier de la señal y graficar tanto su densidad espectral, su transformada y calcular sus estadísticos descriptivos en función de la frecuencia de la siguiente manera:
```ruby
t = np.linspace(0,1,fs,endpoint=False)
N = len(t)
transfou = np.fft.fft(signal)/N
frec = np.fft.fftfreq(N, 1/fs)
magni = 2*np.abs(transfou[:N//2])
psd = (magni**2)/N

plt.figure(figsize=(10,4))
plt.plot(frec[:N//2], magni,'brown')
plt.title('Espectro de la señal de ECG Persona 35')
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud")
plt.grid()
plt.show()

plt.figure(figsize=(10,4))
plt.plot(frec[:N//2], psd,'yellow')
plt.title('Densidad espectral señal Persona 35')
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Densidad Espectral")
plt.grid()
plt.show()

#Estadísticos descriptivos numpy
print("\nEstadísticos descriptivos transformada")
print("Promedio: ",np.mean(magni))
print("Desviación estándar: ",np.std(magni))
print("Mediana: ",np.median(magni))

plt.figure(figsize=(10,4))
plt.hist(magni, bins=50, alpha=0.75, color='b', edgecolor='black',density=True)
plt.title("Histograma de la frecuencia")
plt.xlabel("Magnitud")
plt.ylabel("Frecuencia [Hz]")
plt.show()
```
![image](https://github.com/user-attachments/assets/28e485f2-0e3d-4c16-b56a-e40057be2cd7)
![image](https://github.com/user-attachments/assets/cf860846-744e-4a19-bc4b-5f694c38e406)

- t = np.linspace(0, 1, fs, endpoint=False): crea un vector de tiempo de un segundo de duración.
* N = len(t): calcula la longitud del vector de tiempo, que también será la longitud de la transformada.
* transfou = np.fft.fft(signal) / N: Calcula la Transformada de Fourier Discreta (DFT) de la señal ECG.
* frec = np.fft.fftfreq(N, 1 / fs): Calcula las frecuencias correspondientes a la DFT.
* magni = 2 * np.abs(transfou[:N // 2]): Calcula la magnitud del espectro de frecuencia, tomando solo la mitad positiva del espectro.
* psd = (magni**2) / N: Calcula la densidad espectral de potencia (PSD), que representa la distribución de la potencia de la señal en función de la frecuencia.

Para los datos estadísticos de la frecuencia obtuvimos que:
* Promedio: 0.0002752
* Desviación estándar: 0.0005354887113656084
* Mediana: 0.00014000000000000001
## Resultados
El análisis de las señales sintéticas demostró la capacidad de la correlación cruzada para medir la similitud entre señales. El análisis de la señal ECG real proporcionó información valiosa sobre sus características en el dominio del tiempo y la frecuencia.
