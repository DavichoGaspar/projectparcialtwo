
class gestionDatos:

    def Verificar(self, cedula, lista):
        obj = None
        for indice in range(len(lista)):
            if cedula == lista[indice].cedula:
                obj = lista[indice]
                break

        return obj

