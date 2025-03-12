# Mostra mensaje de inicio y solicitar número al usuario
def MensajeInicio():
    try:
        valorElegido = int(input("Introduzca el número de valores: "))
        if valorElegido > 0:
            return valorElegido
        else:
            return None
    except Exception:
        return None
    
# Pide los números al usuario y los devuelve en una lista
def ObtenerNumeros(cantidad):
    listaNumeros = []
    if cantidad > 0:
        num = 0
        for _ in range(cantidad):
            num += 1
            try:
                numero = float(input(f"Introduzca {num}º de {cantidad} elementos: "))
                listaNumeros.append(numero)
            except Exception:
                print("Debe introducir un número correcto")
        return listaNumeros
    else:
        return None

# Función para calcular el máximo de una lista
def ValorMaximo(lista):
    # Ordenamos la lista de mayor a menor 
    # y obtenemos el primer valor que será el máximo
    lista.sort(reverse=True)
    return lista[:1][0]

# Función para calcular el mínimo de una lista
def ValorMinimo (lista):
    # Ordenamos la lista de menor a mayor 
    # y obtenemos el primer valor que será el mínimo
    lista.sort()
    return lista[:1][0]

# Función para calcular la media de una lista
def ValorMedio (lista):
    suma = 0
    for i in lista:
        suma += i
    # La media será la suma de los valores divida entre el número de valores
    media = suma/len(lista)
    return media

# Función para calcular la mediana de una lista
def ValorMediana(lista):
    mediana = 0
    # Ordenamos la lista de menor a mayor
    lista.sort()
    # Obtenemos el tamaño de la lista
    tamano = len(lista)
    # Si la lista contiene un solo elemento, la mediana será el propio elemento
    if tamano == 1:
        mediana = lista [:1][0]
    elif tamano % 2 != 0: # Si la lista tiene un número de valores impar
        # La mediana será su valor central
        posLista = tamano // 2
        mediana = lista[posLista] + 0
    else: # Si la lista tiene un número de valores par
        # La mediana será la media de sus dos valores centrales
        posLista1 = tamano // 2
        posLista2 = (tamano // 2) - 1
        mediana = (lista[posLista1] + lista[posLista2]) / 2
    return mediana

# Función para realizar y mostrar todos los cálculos
def MostrarCalculos(lista):
    minimo = ValorMinimo(lista)
    maximo = ValorMaximo(lista)
    media = ValorMedio(lista)
    mediana = ValorMediana(lista)
    print(f"El número más pequeño es: {minimo}")
    print(f"El número más grande es: {maximo}")
    print(f"La media es: {media}")
    print(f"La mediana es: {mediana}")
    
# Ejecutamos la aplicación
valorElegido = MensajeInicio()
if valorElegido == None:
    print("Debe indicar un número correcto (mayor que cero)")
else:
    listaNumeros = ObtenerNumeros(valorElegido)
    if listaNumeros == None:
        print("Debe indicar un número de números correcto (mayor que cero)")
    else:
        MostrarCalculos(listaNumeros)