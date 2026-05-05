# Grupo: 01 | Técnica: Lock (threading.Lock)
# Integrantes: Sara Román, Alvaro Vega, Fernando Guerra, Bruce Inostroza, Nicolás Jara
# Asignatura: Sistemas Operativos | Universidad La Serena


import threading # Se importa el módulo threading para trabajar con hilos
import random 
import math

# Lock para sincronización
lock = threading.Lock()

# Archivo compartido
archivo = "resultados.txt"

# Función del productor
def productor(): # Genera números aleatorios y los escribe en el archivo
    with lock: # Se adquiere el lock para asegurar que solo un hilo acceda al archivo a la vez, evitando condiciones de carrera.
        with open(archivo, "a") as f: 
            for _ in range(5): # Se generan 5 números aleatorios y se escriben en el archivo.
                numero = random.randint(1, 10) # Se genera un número aleatorio entre 1 y 10 utilizando la función randint del módulo random.
                f.write(f"Numero generado: {numero}\n") 

# Función del consumidor                
def consumidor():
    """Lee números del archivo y escribe su factorial"""
    with lock:
        # Lee los números generados
        with open(archivo, "r") as f:
            lineas = f.readlines() 

        # Calcular factorial y escribir resultados
        with open(archivo, "a") as f: # Se abre el archivo en modo "append" para agregar los resultados sin borrar los números generados por el productor.
            for linea in lineas:
                if "Numero generado" in linea:
                    numero = int(linea.split(":")[1]) # Se extrae el número generado del texto, se convierte a entero y se calcula su factorial.
                    f.write(f"El factorial de: {numero} es {math.factorial(numero)}\n") 

if __name__ == "__main__":
    # Crear archivo vacío
    open(archivo, "w").close()

    # Crear hilos
    t1 = threading.Thread(target=productor) # El hilo del productor se encarga de generar números aleatorios y escribirlos en el archivo compartido.
    t2 = threading.Thread(target=consumidor) # El hilo del consumidor se encarga de leer los números generados por el productor, calcular su factorial y escribir los resultados en el mismo archivo compartido.

    # Ejecutar hilos
    t1.start()
    t1.join()
    t2.start()
    t2.join()

    print("Finalizo la ejecucion. revisar el archivo resultados.txt para ver los resultados.")
