
import os

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

def csv_sub_menu():
    print("1: Reconocer textos.\n2: Estadísticas.\n3: Graficación de columnas.\n4: Volver")
    función_csv = int(input("¿Qué desea hacer?: "))
    return función_csv

def contar_palabras_txt():
    archivo = input("Ingrese la ruta del archivo a procesar: ")
    with open(archivo, 'r') as file:
        palabras = archivo.split()
        cant_palabras = palabras.len()
        print(f"El archivo tiene {cant_palabras} palabras")


def main():
    while True:
        opción = main_menu()

        if opción == 1:
            Listar_buscar_sub_menu()
            
        elif opción == 2:
            txt_sub_menu()
            
            if txt_sub_menu() == 1:
                contar_palabras_txt()

            elif txt_sub_menu() == 2:
                pass
            elif txt_sub_menu() == 3:
                pass
            elif txt_sub_menu() == 4:
                break
            else:
                print("Opción no valida") 

        elif opción == 3:
            
            csv_sub_menu()
            if función_csv == 1:
                pass
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
