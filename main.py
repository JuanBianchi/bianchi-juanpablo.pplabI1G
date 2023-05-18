import os
import re
from biblioteca_parcial import *

lista_productos = []
bandera_primera_opcion = False
bandera_json = False

while True:
    os.system("cls")
    match(infobaus_menu_principal()):
        case 1:
            lista_productos = (abrir_parsear_csv("Insumos.csv"))
            bandera_primera_opcion = True
        case 2:
            if bandera_primera_opcion:
                os.system("cls")
                contar_mostar_cuantos_tienen_cada_tipo_atributo(lista_productos, "MARCA")
                os.system("pause")
            else:
                print("\nNo se puede acceder a esta opcion sin antes haber elegido la opcion 1)")
                os.system("pause")
        case 3:
            if bandera_primera_opcion:
                os.system("cls")
                listar_insumos_por_marca(lista_productos, "MARCA")
                os.system("pause")
            else:
                print("\nNo se puede acceder a esta opcion sin antes haber elegido la opcion 1)")
                os.system("pause")
        case 4:
            if bandera_primera_opcion:
                os.system("cls")
                caracteristica = input("Ingrese una caracteristica: ")
                buscar_por_valor(lista_productos, "CARACTERISTICAS", caracteristica)
                os.system("pause")
            else:
                print("\nNo se puede acceder a esta opcion sin antes haber elegido la opcion 1)")
                os.system("pause")
        case 5:
            if bandera_primera_opcion:
                os.system("cls")
                ordenar_lista_diccionario_doble_crit(lista_productos, "MARCA", "PRECIO", False)
                mostrar_producto_por_marca(lista_productos, "MARCA")
                os.system("pause")
            else:
                print("\nNo se puede acceder a esta opcion sin antes haber elegido la opcion 1)")
                os.system("pause")
        case 6:
            if bandera_primera_opcion:
                os.system("cls")
                realizar_compras(lista_productos)
                os.system("pause")
            else:
                print("\nNo se puede acceder a esta opcion sin antes haber elegido la opcion 1)")
                os.system("pause")
        case 7:
            if bandera_primera_opcion:
                bandera_json = True
                os.system("cls")
                guardar_disco_duro_json(lista_productos)
                os.system("pause")
            else:
                print("\nNo se puede acceder a esta opcion sin antes haber elegido la opcion 1)")
                os.system("pause")
        case 8:
            if bandera_primera_opcion:
                if bandera_json:
                    os.system("cls")
                    leer_archivo_json("Insumos.json")
                    os.system("pause")
                else:
                    print("\nNo podes entrar a esta opcion si no generaste el archivo json en la opcion 7)")
                    os.system("pause")
            else:
                print("\nNo se puede acceder a esta opcion sin antes haber elegido la opcion 1)")
                os.system("pause")
        case 9:
            if bandera_primera_opcion:
                actualizar_precios("Insumos.csv", lista_productos, 8.4)
                os.system("cls")
                print("Precios actualizados con exito.")
                os.system("pause")
            else:
                print("\nNo se puede acceder a esta opcion sin antes haber elegido la opcion 1)")
                os.system("pause")
        case 0:
            if salir():
                break
            else:
                os.system("cls")
                print("Volviendo al menu principal...")
                os.system("pause")
        case default:
            os.system("cls")
            print("Esa opcion no esta disponible por el momento.\n")
            os.system("pause")
