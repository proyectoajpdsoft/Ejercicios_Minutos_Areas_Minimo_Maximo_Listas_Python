import math

# Función para calcular el área de un círculo (pi * radio al cuadrado)
def AreaCirculo(radio):
    return math.pi * pow(radio, 2)

# Función para calcular el área de un triágulo ((base * altura) / 2)
def AreaTriangulo(base, altura):
    return (base * altura) / 2

# Muestra el menú y devuelve el valor elegido por el usuario
def MostrarMenu():
    print("Elija una figura geométrica para calcular el área:")
    print(" Triángulo (T).")
    print(" Círculo (C).")
    valorElegido = input("Indique la figura para calcular el área (T ó C)? ")
    return valorElegido

# Función que calcula el área de la figura geométrica elegida
def CalcualarArea (valorElegido):
    if valorElegido.upper() == "C":
        try:
            radio = float(input("Introduzca el radio del círculo: "))
            area = AreaCirculo(radio)
            print(f"El área de un círculo de radio {radio} es: {area}")
        except Exception:
            print("Debe introducir un radio y altura correctos. Use el punto como separador decimal")
    elif valorElegido.upper() == "T":
        try:
            base = float(input("Introduzca la base del triángulo: "))
            altura = float(input("Introduzca la altura del triángulo: "))
            area = AreaTriangulo(altura=altura, base=base)
            print(f"El área de un triángulo con base {base} y altura {altura} es: {area}")
        except Exception:
            print("Debe introducir una base y altura correctas. Use el punto como separador decimal")            
    else:
        print("Debe elegir entre área del triángulo (T) o bien área del círculo (C)")

# Ejecutamos la aplicación
valorElegido = MostrarMenu()
CalcualarArea (valorElegido)