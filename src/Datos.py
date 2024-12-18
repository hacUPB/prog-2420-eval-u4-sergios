
import os
import csv
import matplotlib.pyplot as plt
import statistics

def main_menu():
    try:        
        print("1: Buscar archivos de esta ruta o Buscar archivos de otra ruta.\n2: Procesar archivos de texto (.txt)\n3: Procesar archivos separados por comas (.csv)\n4: Salir")
        opción = int(input("¿Qué desea hacer?: "))
        return opción
    except ValueError:
        print("Por favor ingrese una opción valida.")
        return None

def Listar_buscar_sub_menu():
    print('1: Ver los archivos de esta ruta.\n2: Ver los archivos de otra ruta.')
    Ruta = int(input('¿Qué desea hacer?: '))
    
    if Ruta == 1:
        Ruta = os.getcwd() 
        archivos = os.listdir(Ruta)  
        if archivos:
            print(f"Archivos en la ruta actual ({Ruta}):")
            for archivo in archivos:
                print(f"- {archivo}")
        else:
            print("No hay archivos en la ruta actual.")
    if Ruta == 2:
      Ruta = input("Ingrese la ruta de la carpeta que desea listar: ")
    
    try:
        archivos = os.listdir(Ruta) 
        print(f"\nArchivos en la ruta especificada ({Ruta}):")
        if archivos:
            for archivo in archivos:
                print(f"- {archivo}")
        else:
            print("No hay archivos en esta Ruta.")
    except FileNotFoundError: 
        print("La ruta especificada no existe.")

def txt_sub_menu():
        print("1: Contar número de palabras.\n2: Reemplazar palabras en el texto.\n3: Contar el número de caracteres.\n4: Volver.")
        función_txt = int(input("¿Qué desea hacer?: "))
        return función_txt
    
def contar_palabras_txt():
    archivo = input("Ingrese la ruta del archivo a procesar: ")
    try:    
        with open(archivo, 'r') as ar:
            contenido = ar.read()
            palabras = contenido.split()
            cant_palabras = len(palabras)
            print(f"El archivo tiene {cant_palabras} palabras")
    except FileNotFoundError:
        print("Error en la ruta de archivo")

def reemplazar_palabras_txt():
    Archivo = input('Por favor ingrese la ruta de su archivo: ') 
    try:
        with open(Archivo, 'r') as Lectura:
            Texto_archivo = Lectura.read()

            palabra_a_cambiar = input("¿Qué palabra desea cambiar?: ")
            Palabra_nueva = input("Por qué palabra desea cambiarla?")
            Cambio_Palabra = Texto_archivo.replace(palabra_a_cambiar, Palabra_nueva)

            with open(Archivo, 'w') as escritura:
                escritura.write(Cambio_Palabra)

            print(f'La palabra se modificó')
            
    except FileNotFoundError:
        print("La ruta especificada no existe.")

def contar_caracteres_txt():
    archivo = input("Ingrese la ruta del archivo a procesar: ")
    try:
        with open(archivo, 'r') as ar:
            caracteres = ar.read()
            cant_caracteres_espacios = len(caracteres)
            cant_caracteres_no_espacios = len(caracteres.replace(" ", ""))
            print(f"El archivo tiene {cant_caracteres_espacios} caracteres incluyendo espacios, {cant_caracteres_no_espacios} y sin espacios")
    except FileNotFoundError:
        print("La ruta especificada no existe.")

def csv_sub_menu():
    print("1: Reconocer textos.\n2: Estadísticas.\n3: Graficación de columnas.\n4: Volver")
    función_csv = int(input("¿Qué desea hacer?: "))
    return función_csv

def primeras_lineas_csv():
    archivo = input("Ingrese la ruta del archivo a procesar: ")
    try:

        with open(archivo, 'r') as csv_ar:
            Lectura_archivo = csv.reader(csv_ar)
            for i, Filas in enumerate(Lectura_archivo):
                if i >= 15:
                    break
                print(Filas)

    except FileNotFoundError:
        print("La ruta especificada no existe.")

def estadísticas_csv():
    lista = []
    archivo = input("Ingrese la ruta del archivo a procesar: ")
    a = int(input("Ingrese la columna a analizar: "))
    b = str(input("Ingrese el delimitador de su archivo: "))
    with open(archivo, 'r') as csvfile:
        lector = csv.reader(csvfile, delimiter = b)
        encabezado = next(lector)
        for fila in lector:
            try:
                valor = float(fila[a])
                lista.append(valor)
            
            except ValueError:
                continue
    if lista:
        print(lista)
        print(f"Hay {len(lista)} datos en la columna")
        print(f"El valor máximo es {max(lista)}")
        print(f"El valor mínimo es {min(lista)}")
        print(f"El valor promedio es {sum(lista)/len(lista)}")
        print(f"La mediana es {statistics.median(sorted(lista))}")
    else:
        print("Imposible calcular las estadísticas de esta columna, intente con otra.")

def Graficar_datos_csv():
    c = str(input("Ingrese el delimitador de su archivo: "))
    archivo = input("Por favor ingrese la ruta del archivo csv: ")
    try:
        with open(archivo, 'r') as csvfile:
            lector = csv.reader(csvfile, delimiter = c)
            encabezado = next(lector)  

            print("Columnas disponibles en el archivo:")
            for i, columna in enumerate(encabezado):
                print(f"{i}: {columna}")
                
            indice_columna = int(input("Por favor ingrese el índice de la columna de datos numéricos que desea graficar: "))
            if indice_columna < 0 or indice_columna >= len(encabezado):
                print("Índice de columna no válido.")
                return

            x = []
            y = []

            for i, fila in enumerate(lector, start=1):
                try: 
                    valor = float(fila[indice_columna])
                    x.append(i)  
                    y.append(valor)
                except ValueError:
                    print(f"Advertencia: Valor no numérico en la fila {i+1}.")

            if not y:
                print("No se encontraron datos numéricos en la columna seleccionada.")
                return

            plt.plot(x, y)
            plt.title(f"Gráfico de la columna '{encabezado[indice_columna]}'")
            plt.xlabel("Índice")
            plt.ylabel("Valor")
            plt.show()

    except FileNotFoundError:
        print("El archivo especificado no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def main():
    while True:
        opción = main_menu()

        if opción == 1:
            Listar_buscar_sub_menu()
            
        elif opción == 2:
            while True:
                función_txt = txt_sub_menu()

                if función_txt == 1:
                    contar_palabras_txt()

                elif función_txt == 2:
                    reemplazar_palabras_txt()

                elif función_txt == 3:
                    contar_caracteres_txt()

                elif función_txt == 4:
                    break
                else:
                    print("Opción no valida") 

        elif opción == 3:
            función_csv = csv_sub_menu()

            if función_csv == 1:
                primeras_lineas_csv()

            elif función_csv == 2:
                estadísticas_csv()

            elif función_csv == 3:
                Graficar_datos_csv()

            elif función_csv == 4:
                break
            else:
                print("Opción no valida") 

        elif opción == 4:
            print('Cerrando programa....')
            break
        else:
            
            print("Opción no valida")

if __name__ == "__main__":
    main()
