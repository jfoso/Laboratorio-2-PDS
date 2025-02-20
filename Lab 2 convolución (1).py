#Laboratorio 2
import scipy
import matplotlib.pyplot as plt
import numpy as np
import wfdb

#Convolución de códigos y cédulas:
n1 = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

#Carol:
cco = np.array([1,0,0,3,7,4,2,0,3,9])
cce = np.array([5,6,0,0,6,6,4])
ccon = np.convolve(cco,cce,mode='full')
print("\nConvolución Carol:",ccon)
fig, ax = plt.subplots()
ax.stem(n1,ccon,'m')
plt.xlabel("n")
plt.ylabel("y[n]")
plt.title("Convolución Carol")
plt.grid()
plt.show()

#Juanfe:
jco = np.array([1,0,1,6,9,4,5,6,9,3])
jce = np.array([5,6,0,0,6,7,5])
jcon = np.convolve(jco,jce,mode='full')
print("\nConvolución Juan Felipe:",jcon)
fig, ax = plt.subplots()
ax.stem(n1,jcon,'r')
plt.xlabel("n")
plt.ylabel("y[n]")
plt.title("Convolución Juan Felipe")
plt.grid()
plt.show()

#Santiago:
sco = np.array([1,0,2,3,1,6,2,9,3,4])
sce = np.array([5,6,0,0,6,6,3])
scon = np.convolve(sco,sce,mode='full')
print("\nConvolución Santiago:",scon)
fig, ax = plt.subplots()
ax.stem(n1,scon,'g')
plt.xlabel("n")
plt.ylabel("y[n]")
plt.title("Convolución Santiago")
plt.grid()
plt.show()

#Convolución señales dadas
n2=np.array([0,1,2,3,4,5,6,7,8])

x1 = np.cos(2*np.pi*100*n2*1.25e-3)
x2 = np.sin(2*np.pi*100*n2*1.25e-3)
corr = np.correlate(x1,x2,mode='full')
print("Correlación señales dadas: ",corr)

tc = np.arange(-len(n2) + 1, len(n2))
plt.figure(figsize=(10,4))
plt.stem(tc,corr,'k')
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Convolución señales dadas")
plt.grid()
plt.show()

#Adquirir datos
ruta = 'C:\\Users\\sachi\\OneDrive - unimilitar.edu.co\\Sexto semestre\\Lab señales\\Lab 2\\ecg-id-database-1.0.0\\Person_35\\rec_4'
record = wfdb.rdrecord(ruta,channels=[1])
signal = record.p_signal
fs = record.fs
muestreo = int(5*fs)
print("\nFrecuencia de muestreo = ",fs)

time=[i / fs for i in range(len(signal))]
signal = signal[:muestreo]
time = time[:muestreo]

#Estadísticos descriptivos numpy
print("\nEstadísticos descriptivos señal")
print("Promedio: ",np.mean(signal))
print("Varianza: ",np.var(signal))
print("Desviación estándar: ",np.std(signal))
print("Coeficiente de variación: ",np.std(signal)/np.mean(signal))

plt.figure(figsize=(10,4))
plt.plot(time, signal, label="Señal ECG")
plt.title('Señal de ECG Persona 35')
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud [mV]")
plt.grid()
plt.show()

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
plt.grid()
plt.show()
