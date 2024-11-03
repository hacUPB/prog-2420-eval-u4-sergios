import system

def main_menu():
    print("1: Buscar o listar archivos.\n2: Procesar archivos de texto (.txt)\n3: Procesarr archivos separados por comas (.csv)\n4: Salir")
    opción = int(input("¿Qué desea hacer?: "))
    return opción

def txt_sub_menu():
    print("1: Contar número de palabras.\n2: Remplazar palabras en el texto.\n3: Contar el número de caracteres.\n4: Volver.")
    función_txt = int(input("¿Qué desea hacer?: "))
    return función_txt

def csv_sub_menu():
    print("1: Reconocer textos.\n2: Estadísticas.\n3: Graficación de columnas.\n4: Volver")
    función_csv = int(input("¿Qué desea hacer?: "))
    return función_csv

def contar_palabras_txt():
    pass

def main():
    while True:
        opción = main_menu()

        if opción == 1:
            system ('cls')


        elif opción == 2:
            system ('cls')
            función_txt = txt_sub_menu
            if función_txt == 1:
                pass
            elif función_txt == 2:
                pass
            elif función_txt == 3:
                pass
            elif función_txt == 4:
                break
            else:
                print("Opción no valida") 

        elif opción == 3:
            system ('cls')
            función_csv = csv_sub_menu
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
            break
        else:
            system ('cls')
            print("Opción no valida")

pass


if __name__ == "__main__":
    main()
