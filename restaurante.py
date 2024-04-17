##############################################################

## Si necesita agregar imports, debe agregarlos aquí arriba ##
### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self, nombre, platos, cocineros, repartidores):
        self.nombre = nombre
        self.platos = platos
        self.cocineros = cocineros
        self.repartidores = repartidores
        self.calificacion = 0

    def SeleccionarCocinero(self, cocineros):
        for cocinero in cocineros:
            if cocinero.enegia > 0:
                return cocinero
        return None

    def SeleccionarRepartidor(self, repartidores):
        list = []
        for repartidor in repartidores:
            if repartidor.energia > 0:
                return repartidor
            else:
                continue
        return list

    def recibir_pedidos(self, clientes):
        for cliente in clientes:
            pedido = []
            for platoFavorito in cliente.platos_preferidos:
                cocinero = self.SeleccionarCocinero(self.cocineros)
                if cocinero is None:
                    break
                else:
                    pedido.append(cocinero.cocinar(platoFavorito))
            repartidor = self.SeleccionarRepartidor(self.repartidores)
            if repartidor == []:
                self. calificacion += cliente.recibir_pedido(repartidor, 0)
            else:
                tiempoDemora = repartidor.repartir(pedido)
                self.calificacion += cliente.recibir_pedido(pedido, tiempoDemora)
        self.calificacion /= len(clientes)

### FIN PARTE 3 #


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")