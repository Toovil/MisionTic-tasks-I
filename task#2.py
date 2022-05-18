tony = input("Ingrese la palabra propuesta por Tony: ")
tony_Upper = tony.upper()

bruce = input("ingrese la palabra propuesta por Bruce: ")
bruce_upper = bruce.upper()

iniciales = input("Iniciales de los nombres de los heroes:")
iniciales_Upper = list(iniciales.upper())

acmT = 0
acmB = 0
salida = ""
for letraI in iniciales_Upper:
  for letraT in tony_Upper:
    if(letraT == letraI):
      acmT += 1
  for letraB in bruce_upper:
    if(letraB == letraI):
      acmB += 1
  if(acmT == acmB):
    salida += "E"  
  elif (acmT > acmB):
    salida += "T"  
  else:
    salida += "B"     
print(salida)
