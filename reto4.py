import json

def reto(personajes,lista):
      lista1=0
      lista2=[]

      personajes = json.loads(personajes)
      lista = lista.split()
      for buy in lista:
        for key in personajes.keys():
         
          if buy == key:
              lista1+=personajes[key]
              lista2.append(buy)
            
      return (print(lista1),"\n" , print(" ".join(lista2)))

reto(input("Personajes: "),input("Lista: "))
