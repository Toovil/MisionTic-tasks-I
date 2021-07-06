poder = int(input("Escribe el nivel de poder de Luffy: "))

def luffy(nivel=poder):
  fase1 = nivel
  fase2 = (nivel * 2) + 4
  fase3 = (fase2 + fase1)//5
  print(fase1, fase2, fase3)

  def gear(gear=fase3):
    if(0 <= fase3 <= 20):
      print("Uno")
    elif(21 <= fase3 <= 30):
      print("Dos")
    elif(31 <= fase3 <= 50):
      print("Tres")
    else:
      print("Cuatro")
    return print(gear())
  return gear()

(luffy())
