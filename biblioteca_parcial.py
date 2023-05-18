import os
import re
import json
from functools import reduce

#######################################################################################################################
("---------------------------------------- FUNCIONES COMPLEMENTARIAS ----------------------------------------------") #
                                                                                                                      #
("-----------------------------------------------------------------------------------------------------------------") #
#######################################################################################################################


def buscar_filtrar_claves(lista: list, clave: str)-> list:
    """_summary_
        busca en la lista de diccionarios si es encuentra la clave recibida por parametro. Si se encuentra, filtra las claves que se repiten
    Args:
        lista (list): lista de diccionarios donde estan las claves
        clave (str): clave a ser buscada en la lista

    Returns:
        list: lista con las claves filtradas
    """
    lista_claves = []
    lista_claves_filtrada = []
    for elemento in lista:
        if elemento[clave] == "":
            elemento[clave] = "Sin marca"
        lista_claves.append(elemento[clave])

    for producto in lista_claves:
        if not buscar_item(lista_claves_filtrada, producto):
            lista_claves_filtrada.append(producto)

    return lista_claves_filtrada


def buscar_item (lista:list, item:any)->bool:
    """_summary_
        busca si el item recibido como parametro se encuentra dentro de una lista
    Args:
        lista (list): lista a ser revisada
        item (any): objeto que se quiere buscar en la lista

    Returns:
        bool: devuelve True si el item forma parte de la lista como elemento, o devuelve False en caso contrario
    """
    rta = False
    for elemento in lista:
        if elemento == item:
            rta = True
            break
    return rta



def validar_entero(numero: str)-> bool:
    """_summary_
        evalua y parsea el caracter o string recibido por parametro
    Args:
        numero (str): caracter numerico que sera evaluado y casteado

    Returns:
        bool: devuelve True si el parametro recibido es un caracter numerico o False si no es un caracter numerico 
    """
    if type(numero) == str:
        if re.search(r"^\d{1,}$", numero):
            rta= True
        else:
            rta = False
    else:
        print("El numero ya esta en su tipo de dato correcto.")
        rta = False
    return rta


def normalizar_datos(lista: list) :
    """_summary_
        convierte datos de tipo string al tipo de dato correspondiente.
    Args:
        lista (list): lista de diccionarios con datos a ser normalizados
    """
    bandera_cambios = False
    if len(lista) > 0:
        for dict in lista:
            for clave in dict:
                valor = dict[clave]
                if type(valor) == str:
                    try:
                        if re.search(r"\d+\.", valor):
                            dict[clave] = float(valor)
                            bandera_cambios = True
                        else:
                            dict[clave] = int(valor)
                            bandera_cambios = True
                    except ValueError:
                        pass
                # if re.search(r"\d+\.", valor):
                #     dict[clave] = float(valor)
                # elif re.search(r"\d{1,}", valor):
                #     dict[clave] = int(valor)
                # else:
                #     pass
        if bandera_cambios:        
            os.system("cls")
            print("Datos normalizados.")
            os.system("pause")
    else:
        print("Error, la lista esta vacía.")
        os.system("pause")


def imprimir_menu():
    """_summary_
        imprime las opciones disponibles del menu principal
    """
    print("***      MENU PRINCIPAL    ***")
    print("------------------------------\n")
    print("1) Traer datos desde archivo\n"
          "2) Listar cantidad de insumos por marca\n"
          "3) Listar los insumos por marca\n"
          "4) Buscar insumo por caracteristica\n"
          "5) Listar todos los insumos ordenados\n"
          "6) Realizar compras\n"
          "7) Guardar archivo JSON\n"
          "8) Leer archivo JSON\n"
          "9) Actualizar precios\n\n"
          "0) Salir\n")


#######################################################################################################################
("---------------------------------------- FUNCIONES USADAS EN TRABAJO INFOBAUS -----------------------------------") #
("                                                    ('main.py')                                                  ") #
("-----------------------------------------------------------------------------------------------------------------") #
#######################################################################################################################


def infobaus_menu_principal()->int:
    """_summary_
        muestra por consola lo que la funcion imprimir_menu y pide al usuario un caracter numerico para ser evaluado como opcion
    Returns:
        int: opcion del menu ya evaluada y validada
    """
    imprimir_menu()
    opcion = input("Ingrese una opcion (en caracteres numericos): ")
    if validar_entero(opcion):
        numero = int(opcion)
    else:
        numero = -1
    
    return numero





def abrir_parsear_csv(nombre_archivo: str)-> list:
    """_summary_
        lee, modifica y parsea el archivo para el optimo uso de los datos contenidos en el.
    Args:
        nombre_archivo (str): archivo de texto plano que contiene los datos

    Returns:
        list: lista de diccionarios con los datos formateados en claves y valores.
    """
    lista = []
    if type(nombre_archivo) == str:
        # APERTURA Y LECTURA DE ARCHIVO
        with open(nombre_archivo, "r", encoding = "utf-8") as file:
            lineas = file.readlines()
            claves = lineas[0].strip("\n") 
            clave = claves.replace('"', '').split(",")
            for linea in lineas[1:]:
                valores = linea.strip("\n").strip()
                valor = valores.replace('"', '').split(",")

                diccionario = {}
                for indice in range(len(clave)):
                    diccionario[clave[indice]] = valor[indice]
                lista.append(diccionario)

        # MODIFICACIONES
        for diccionario in lista:
            marca = diccionario["MARCA"]
            marca_modificada = marca.replace(" ", "")
            diccionario["MARCA"] = marca_modificada

            precio = diccionario["PRECIO"]
            precio_sin_signo = precio.replace("$", "")
            diccionario["PRECIO"] = precio_sin_signo

        # PARSEO
        normalizar_datos(lista)
    else:
        print("Error. El archivo no es de tipo .txt")

    return lista  



def contar_mostar_cuantos_tienen_cada_tipo_atributo(lista: list, clave: str):
    """_summary_
        cuenta e imprime cuantos elementos de esa clave hay en la lista y a que clave pertenece
    Args:
        lista (list): lista de diccionarios donde se encuentra la clave
        clave (str): nombre de la clave que sera buscada
    """
    if type(lista) == list and type(clave) == str:

        lista_atributos_filtrada = buscar_filtrar_claves(lista, clave)

        contador_atributos = 0   # Inicializo

        for atributo in lista_atributos_filtrada:
            print("\n" + atributo)
            print("------------")
            for elemento in lista:
                if atributo == elemento[clave]:
                    contador_atributos +=1
            print("Cantidad de insumos: ", contador_atributos)
            contador_atributos = 0   # Reseteo contador a 0
    else:
        print("Error. La lista o la clave no son del tipo correcto.")



def listar_insumos_por_marca(lista: list, clave: str):
    """_summary_
        busca la clave que recibe por parametro en la lista de diccionarios, si la encuentra, filtra todas esas claves e imprime los valores precio y nombre 
        formateados de todos los diccionarios que contengan la clave.  
    Args:
        lista (list): lista de diccionarios a ser iterada 
        clave (str): nombre de la clave que sirve como criterio de listado
    """
    if type(lista) == list and type(clave) == str:

        lista_productos_filtrada = buscar_filtrar_claves(lista, clave)

        for atributo in lista_productos_filtrada:
            print("\n" + atributo)
            print("------------")
            for elemento in lista:
                if atributo == elemento[clave]:
                    dato = elemento["PRECIO"]
                    nombre = elemento['NOMBRE']
                    print(f"Producto: {nombre} | Precio: ${dato}")
    else:
        print("Error. La lista o la clave no son del tipo correcto.")



def buscar_por_valor(lista: list, clave: str, valor: str):
    """_summary_
        busca dentro de una clave si se encuentra el valor recibido por parametro e imprime su diccionario 
    Args:
        lista (list): lista con el posible valor en sus elementos de tipo diccionario
        clave (str): clave del diccionario donde se va a buscar el valor
        valor (str): contenido a ser buscado en la lista de diccionarios
    """
    if len(lista) > 0:
        caracteristica_encontrada = False
        for diccionario in lista:
            caracteristicas = re.findall(r"[^|!*\n]+", diccionario[clave])
            for caracteristica in caracteristicas:
                if re.search(valor, caracteristica, re.IGNORECASE):
                    print("---------------------------")
                    print(diccionario)
                    caracteristica_encontrada = True

        if not caracteristica_encontrada:
            print("Caracteristica no encontrada.")
    else:
        print("Error, la lista se encuentra vacia.")



def ordenar_lista_diccionario_doble_crit(lista: list, grupo: str, clave: str, asc = True):
    """_summary_
        se encarga de agrupar segun un campo en comun y ordenar de manera ascendente o descendente todos los valores de una lista de diccionarios
    Args:
        lista (list): lista de diccionarios con los campos y valores a ser ordenados
        grupo (str): primer criterio de ordenamiento o agrupamiento
        clave (str): segundo criterio de ordenamiento
        asc (bool, optional): Defaults to True si no se manda por parametro, ordenando de mayor a menor. Si es False, se ordena de menor a mayor
    """
    tam = len(lista)
    for i in range(0, tam - 1):    
        for j in range(i + 1, tam):
            if ((lista[i][grupo] == lista[j][grupo]) 
                and (((lista[i][clave] > lista[j][clave]) and asc) or ((lista[i][clave] < lista[j][clave]) and not asc)) 
                or (lista[i][grupo] > lista[j][grupo])):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
                
def mostrar_producto_por_marca(lista: list, clave: str):
    """_summary_
        imprime el precio, nombre, id y la primer caracteristica en la lista filtrada devuelta por buscar_filtrar_claves
    Args:
        lista (list): lista de diccionarios a ser iterada
        clave (str): cadena usada para 
    """
    # Tambien es un "remake" de mostar_por_atributo pero optimizado para que sirva de complemento
    # a la funcion ordenar_lista_diccionario_doble_crit
    if type(lista) != list or type(clave) == str:
        lista_marcas_filtrada = buscar_filtrar_claves(lista, clave)

        for marca in lista_marcas_filtrada:
            print(f"\n{marca}")
            print("-------------------")
            for elemento in lista:
                if marca == elemento[clave]:
                    print(f'Nombre: {elemento["NOMBRE"]}')
                    print(f'Precio: {elemento["PRECIO"]}')
                    print(f'ID: {elemento["ID"]}')
                    lista_caracteristicas = re.findall(r"^[áéíóúa-zA-Z0-9\s\.\-]+", elemento["CARACTERISTICAS"])
                    for caracteristica in lista_caracteristicas:
                        print(caracteristica)
                    print("-")
    else:
        print("Error. La lista o la clave no son del tipo correcto.")





def crear_factura(lista: list, total_compra: float):
    """_summary_
        funcion que se encarga de generar un archivo de texto que sirve como factura y lo imprime por consola una vez realizada la compra en la funcion realizar_compras
    Args:
        lista (list): carrito de compras con los productos y su informacion
        total_compra (float): precio total de todos los precios de los productos dentro del carrito
    """
    if len(lista) > 0 and type(lista) == list:
        with open("factura.txt", "w", encoding="utf-8") as file:
            file.write("Factura de compra:\n")
            for diccionario in lista:
                file.write(f"Producto: {diccionario['Nombre']}, Precio (subtotal): ${diccionario['Subtotal']}. Cantidad: x{diccionario['Cantidad']}\n")
            file.write(f"\nTotal de la compra: ${total_compra}")
        print("\nFactura generada.")
    else:
        print("Error. La lista de productos esta vacia")
        os.system("pause")


def buscar_insumo_en_lista(lista_productos:list)->list:
    """_summary_
        busca en la lista de diccionarios si se encuentra la marca ingresada para que luego sean mostrados los productos para su posterior eleccion por el usuario
    Args:
        lista_productos (list): lista de diccionarios donde se encuentran las marcas y los productos a ser buscados

    Returns:
        list: devuelve una lista con los insumos si filter es igual True o regresa al menu principal si filter = False
    """
    if len(lista_productos) > 0 or type(lista_productos) == list: 
        marca = input("Ingrese la marca del producto que desea buscar: ")
        while re.search(r"[^a-zA-Z\-]", marca):
            os.system("cls")
            marca = input("Error, solo podes ingresar caracteres alfabeticos para ingresar una marca. Intente de nuevo: ")

        productos_encontrados = list(filter(lambda producto: producto['MARCA'] == marca, lista_productos))
        if not productos_encontrados:
            print("Esa marca no está disponible por el momento")
            os.system("pause")
            return productos_encontrados
    else:
        print("Error, la lista esta vacía o no es de tipo lista.")
        os.system("pause")

    return productos_encontrados


def agregar_al_carrito(lista_productos:list, carrito:list):
    """_summary_
        agrega y almacena a la lista 'carrito' el producto y cantidad ingresada para su posterior operacion de compra 
    Args:
        lista_productos (list): lista de diccionarios donde se encuentran los productos/insumos que seran agregados al carrito
        carrito (list): lista que almacena los datos del producto agregado
    """
    if len(lista_productos) > 0 or type(lista_productos) == list:
        while True:
            try:
                compra_producto = int(input(f"Que producto va a querer comprar? Indiquelo desde el 1 al {len(lista_productos)}: "))
                while compra_producto < 1 or compra_producto > len(lista_productos):
                    compra_producto = int(input(f"Ese producto no está disponible. Reingrese de nuevo el producto que desea comprar: Indiquelo desde el 1 al {len(lista_productos)}: "))
                cantidad = int(input("Cuantas veces desea comprarlo?: "))
                break
            except ValueError:
                print("Error. Solo podes ingresar caracteres numericos y sin tiles o comas.")
        carrito.append({'Nombre': lista_productos[compra_producto - 1]["NOMBRE"], 'Precio': lista_productos[compra_producto - 1]["PRECIO"], 'Cantidad': cantidad, 'Subtotal': lista_productos[compra_producto - 1]["PRECIO"] * cantidad})
    else:
        print("Error, la lista esta vacía o no es de tipo lista.")
        os.system("pause")


def realizar_compras(lista: list):
    """_summary_
        funcion encargada de llevar a cabo la operacion de compra de productos.\n
        -muestra los productos disponibles luego de encontrarse la marca en la funcion buscar_insumo_en_lista\n
        -contiene el carrito de compras donde se encuentran todos los productos elegidos por el usuario en la funcion agregar_al_carrito y confirma si se realiza la compra o no\n
        -realiza los calulculos para informar el precio subtotal y total de la compra\n
        -invoca a la funcion generar_factura
    Args:
        lista (list): lista de diccionarios con todos los productos a ser operada
    """
    carrito_compras = []
    seguir = "s"
    total = 0
    while seguir == "s":
        os.system("cls")

        # BUSQUEDA DEL PRODUCTO/INSUMO
        lista_productos_encontrados = buscar_insumo_en_lista(lista)
        if len(lista_productos_encontrados) > 0:
            print("PRODUCTOS DISPONIBLES: ")
            print("---------------------")
            i = 1
            for producto in lista_productos_encontrados:
                print(f'[{i}] {producto}')
                print("------------------------------------------------------------------------")
                i += 1

            # AGRGEGADO DEL PRODUCTO AL CARRITO DE COMPRAS
            agregar_al_carrito(lista_productos_encontrados, carrito_compras)
            seguir = input("Desea buscar otros productos? s/n ")
            while seguir != "s" and seguir != "n":
                seguir = input("Solo podes elegir entre 's' o 'n': ")

    if len(carrito_compras) > 0:
        # REALIZACION DE LA COMPRA
        total = reduce(lambda acumulador, compras: acumulador + compras["Precio"] * compras["Cantidad"], carrito_compras, 0)

        os.system("cls")
        print("CARRITO: ")
        print(carrito_compras)
        print("El total del carrito de compras es: ",total)        
        confirmacion = input("\nConfirmar la compra? s/n ")    
        while confirmacion != "s" and confirmacion != "n":
                confirmacion = input("Solo podes elegir entre 's' o 'n': ")


        # GENERACION DE FACTURA
        if confirmacion == "s":
            crear_factura(carrito_compras, total)
    




def guardar_disco_duro_json(lista: list):
    """_summary_
        crea un archivo en formato json y guarda todos los valores que contengan de nombre "Disco Duro"
    Args:
        lista (list): lista de diccionarios donde cada diccionario es un insumo
    """
    if len(lista) > 0 or type(lista) == list:
        productos = []
        with open("Insumos.json", "w", encoding="utf-8") as file:
            for diccionario in lista:
                if re.match(r"D[a-zA-Z]+", diccionario["NOMBRE"]):
                    productos.append(diccionario)
            json.dump(productos, file, indent=4)        
    else:
        print("Error. La lista se encuentra vacia o no es de tipo lista.")
        os.system("pause")



def leer_archivo_json(archivo: str):
    """_summary_
        recibe un archivo de texto para imprimir sus datos por consola
    Args:
        archivo (str): archivo de tipo texto plano que sera abierto y leido
    """
    if type(archivo) == str:
        with open(archivo, "r") as file:
            lista = json.load(file)
            for diccionario in lista:
                print(diccionario)
    else:
        print("Error. El archivo no es de tipo str")
        os.system("pause")



def actualizar_precios(archivo: str, lista: list, aumento: float):
    """_summary_
        aplica el aumento recibido a los precios que estan dentro de la lista de productos
    Args:
        archivo (str): archivo de texto plano donde se van a guardar los precios actualizados 
        lista (list): lista de productos donde se aplicara el aumento
        aumento (float): el porcentaje de aumento a aplicar
    """
    if (len(lista) > 0 and type(lista) == list) or type(archivo) != str:
        aumento_total = list(map(lambda elemento: (elemento["PRECIO"] * aumento) / 100, lista))
        for indice in range(len(lista)):
            precio_actualizado = lista[indice]["PRECIO"] + aumento_total[indice]
            lista[indice]["PRECIO"] = precio_actualizado
    else:
        print("Error, la lista esta vacia o no ingresaste los datos en su tipo correspondiente.")
    
    guardar_dato_csv(archivo, lista)


def guardar_dato_csv(archivo: str, lista: list):
    """_summary_
        guarda y sobreescribe los datos de una lista de diccionarios en el archivo
    Args:
        archivo (str): archivo de texto en donde se van a guardar los datos
        lista (list): lista de diccionarios a iterar donde estan contenidos los datos a ser guardados
    """
    if (len(lista) > 0 and type(lista) == list) or type(archivo) != str:
        with open(archivo, "w", encoding="utf-8") as file:
            # CLAVES
            for diccionario in lista:
                linea = ",".join(diccionario)
                file.write(linea + "\n")
                break
            # VALORES
            for diccionario in lista:
                for clave in diccionario:
                    valor = str(diccionario[clave])
                    file.write(valor + ",")
                file.write("\n")    
    else:
        print("Error, la lista esta vacia o no ingresaste los datos en su tipo correspondiente.")
                

def salir()->bool:
    """_summary_
        funcion que se usa para salir de un menu de opciones. Confirma la accion o la deshace.
        Valida que solo se ingrese "s" o "n" para confirmaciones. 
    Returns:
        bool: devuelve True si se ingresa "s" o False si se ingresa "n"
    """
    confirmar_salida = input("Esta seguro de querer salir del programa? s/n")
    while confirmar_salida != "s" and confirmar_salida != "n":
        confirmar_salida = input("Error, ingrese solo 's' o 'n'. Desea salir del programa?")
    if confirmar_salida == "s":
        rta = True
    else:
        rta = False
 
    return rta

                















