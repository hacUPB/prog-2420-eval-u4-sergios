
import os
import csv

def main_menu():
    print("1: Buscar archivos de esta ruta o Buscar archivos de otra ruta.\n2: Procesar archivos de texto (.txt)\n3: Procesar archivos separados por comas (.csv)\n4: Salir")
    opción = int(input("¿Qué desea hacer?: "))
    return opción

def Listar_buscar_sub_menu():
    print('1: Ver los archivos de esta ruta.\n2: Ver los archivos de otra ruta.')
    Ruta = int(input('¿Qué desea hacer?: '))
    
    if Ruta is 1:
        Ruta = os.getcwd()  # Obtiene la ruta actual
        archivos = os.listdir(Ruta)  # Lista los archivos en la ruta actual
        if archivos:
            print(f"Archivos en la ruta actual ({Ruta}):")
            for archivo in archivos:
                print(f"- {archivo}")
        else:
            print("No hay archivos en la ruta actual.")
    if Ruta is 2:
      Ruta = input("Ingrese la ruta de la carpeta que desea listar: ")
    
    try:
        archivos = os.listdir(Ruta)  # Lista los archivos en la ruta proporcionada
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
    ar = open(archivo, 'r')
    contenido = ar.read()
    palabras = contenido.split()
    cant_palabras = len(palabras)
    print(f"El archivo tiene {cant_palabras} palabras")

def reemplazar_palabras_txt():
    pass

def contar_caracteres_txt():
    archivo = input("Ingrese la ruta del archivo a procesar: ")
    ar = open(archivo, 'r')
    caracteres = ar.read()
    cant_caracteres_espacios = len(caracteres)
    cant_caracteres_no_espacios = len(caracteres.replace(" ", ""))
    print(f"El archivo tiene {cant_caracteres_espacios} caracteres incluyendo espacios, {cant_caracteres_no_espacios} y sin espacios")

def csv_sub_menu():
    print("1: Reconocer textos.\n2: Estadísticas.\n3: Graficación de columnas.\n4: Volver")
    función_csv = int(input("¿Qué desea hacer?: "))
    return función_csv

def primeras_lineas_csv():
    archivo = input("Ingrese la ruta del archivo a procesar: ")
    with open(archivo, 'r') as csv_ar:
        for i in range():
            primeras_lineas = csv_ar.readline(14)
            lista = []
            lista.append(primeras_lineas)
        print(lista)


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
                    pass
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
                pass
            elif función_csv == 3:
                pass
            elif función_csv == 4:
                break
            else:
                print("Opción no valida") 

        elif opción == 4:
            print('Cerrando programa....')
            break
        else:
            
            print("Opción no valida")

pass


if __name__ == "__main__":
    main()
