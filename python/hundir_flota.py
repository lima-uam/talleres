from random import randrange

# Tamaño del tablero
ALTURA=3
ANCHURA=3
# Número de barcos que hay que hundir
N_BARCOS=3

def dibujar_tablero(aciertos,fallos,altura=ALTURA,anchura=ANCHURA):
    '''
    Muestra el tablero de juego.

    Parámetros:
      aciertos: lista de coordenadas (tuplas de 2 números)
      fallos: lista de coordenadas (tuplas de 2 números)
      altura: por defecto se toma el valor de ALTURA
      anchura: por defecto se toma el valor de ANCHURA
    '''

    tablero=[[" "]*anchura for _ in range(altura)]
    for coordenada in aciertos:
        tablero[coordenada[0]][coordenada[1]]="~"
    for coordenada in fallos:
        tablero[coordenada[0]][coordenada[1]]="X"

    print("    ┌"+"┬".join([f"{i:^3}" for i in range(anchura)])+"┐")
    filas_form=[
        f"{i:>3} │ "+" │ ".join(tablero[i])+" │" for i in range(altura)
    ]
    print("\n".join(filas_form))
    print("    └"+"┴".join(["───"]*anchura)+"┘")

def obtener_entrada(altura=ALTURA,anchura=ANCHURA):
    '''
    Obtiene la jugada que quiere hacer el jugador.
    
    Parámetros:
      altura: por defecto se toma el valor de ALTURA
      anchura: por defecto se toma el valor de ANCHURA
    
    Retorno:
      Coordenadas (tupla de 2 números) del disparo del jugador, o 
      tupla vacía () si hay algún error
    '''

    latitud=input("> Introduce la latitud (vertical): ")
    longitud=input("> Introduce la longitud (horizontal): ")

    try:
        n_latitud=int(latitud)
        n_longitud=int(longitud)
    except:
        print("Debes introducir números enteros.")
        return ()

    if n_latitud<0 or n_latitud>=altura:
        print(f"La latitud debe estar entre 0 y {altura-1}.")
        return ()

    if n_longitud<0 or n_longitud>=anchura:
        print(f"La longitud debe estar entre 0 y {anchura-1}.")
        return ()

    return (n_latitud,n_longitud)

def colocar_barcos(altura=ALTURA,anchura=ANCHURA,n_barcos=N_BARCOS):
    '''
    Coloca N_BARCOS barcos al azar en el tablero.

    Parámetros:
      altura: por defecto se toma el valor de ALTURA
      anchura: por defecto se toma el valor de ANCHURA
      n_barcos: por defecto se toma el valor de N_BARCOS
    
    Retorno:
      Lista de coordenadas (tuplas de 2 números) en las que están los 
      barcos
    '''

    posiciones=[]

    # Por completar

    return posiciones

def comprobar_disparo(disparo,barcos_sin_hundir,aciertos,fallos):
    '''
    Comprueba si el jugador ha golpeado un barco y actualiza las
    listas de aciertos/fallos.
    La comprobación de los límites del tablero se hace en 
    obtener_entrada.

    Parámetros:
      disparo: coordenadas (tupla de 2 números)
      barcos_sin_hundir: lista de coordenadas (tuplas de 2 números)
      aciertos: lista de coordenadas (tuplas de 2 números)
      fallos: lista de coordenadas (tuplas de 2 números)
    '''

    # Por completar

    pass

# Completa la lógica del juego usando las funciones anteriores y las
# variables e instrucciones adicionales que consideres necesarias
#
# Idea:
# 
# fin_juego=False
# ...
# while not fin_juego:
#     ...
#     if ...:
#         fin_juego=True
#         print("¡Has ganado!")

# Ejemplo de uso de dibujar_tablero
dibujar_tablero(aciertos=[(0,1)],fallos=[(1,0)])
