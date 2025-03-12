try:
    valorPedido = int(input("Escriba una cantidad de segundos: "))
    if valorPedido > 0:
        # Dividimos entre 60 y obtenemos la parte entera para obtener los minutos
        minutos = valorPedido//60
        # Dividimos entre 60 y obtenemos el resto de la división para obtener los segundos
        segundos = valorPedido%60
        # Mostramos el resultado por pantalla
        print(f"{valorPedido} segundos son {minutos} minutos y {segundos} segundos")
    else:
        print("Debe introducir un valor de segundos superior a cero")
except Exception as ex:
    print("Debe introducir un número de segundos")