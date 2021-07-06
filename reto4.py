import json

def SOFAH(cantidad, personajes):
    personajes = json.load(personajes)
    cantidad = cantidad.split()

    salida_cantidad = 0
    salida_personajes = []
    