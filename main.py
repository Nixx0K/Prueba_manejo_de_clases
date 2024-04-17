##############################################################
from random import choice, seed, randint, choices
import personas
import restaurante
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 4 ###
def crear_repartidores():
    repartidores = []
    for i in range(2):
        nombreale = choice(NOMBRES)
        tiemposDeEspera = randint(20,30)
        repartidores.append(personas.Repartidor(nombreale,tiemposDeEspera))
    return repartidores

def crear_cocineros():
    cocineros = []
    for i in range(6):
        nombreale = choice(NOMBRES)
        habilidad = randint(1, 10)
        cocineros.append(personas.Cocinero(nombreale, habilidad))
    return cocineros

def crear_clientes():
    clientes = []
    menu = [["Pepsi", "Bebestible"], ["Coca-Cola", "Bebestible"], ["Jugo Natural", "Bebestible"], ["Agua", "Bebestible"], ["Papas Duqueza", "Comestible"], ["Lomo a lo Pobre", "Comestible"], ["Empanadas", "Comestible"], ["Mariscos", "Comestible"]]
    for i in range(6):
        nombreale = choice(NOMBRES)
        platosFavorita = choices(menu, k=5)
        clientes.append(personas.Cliente(nombreale, platosFavorita))
    return clientes

def crear_restaurante():
    cocineros = crear_cocineros()
    repartidores = crear_repartidores()
    nombreAleatorio23 = choice(NOMBRES)
    nombreRestaurant = f"la fonda de {nombreAleatorio23}"
    restaurante1 = restaurante.Restaurante(nombreRestaurant, INFO_PLATOS, cocineros, repartidores)
    return restaurante1

### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################

INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = ["Cristian", "Antonio", "Francisca", "Camila", "Caua"]

if __name__ == "__main__":

    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    seed("DSP")
    restaurante = crear_restaurante() # Crea el restaurante a partir de la función crear_restaurante()
    clientes = crear_clientes() # Crea los clientes a partir de la función crear_clientes()
    if restaurante != None and clientes != None:
        restaurante.recibir_pedidos(clientes) # Corre el método recibir_pedidos(clientes) para actualizar la calificación del restaurante
        print(
            f"La calificación final del restaurante {restaurante.nombre} "
            f"es {restaurante.calificacion}"
        )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")
