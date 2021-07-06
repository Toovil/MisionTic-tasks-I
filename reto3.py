mensaje = input("Escribe el mensaje clave separado por espacios:").upper()

mensaje_split = mensaje.split()

output_str = []

counterFinal = []

counter = 1

for i in range(len(mensaje_split) - 1):
    if mensaje_split[i] not in output_str:
        output_str.append(mensaje_split[i])
    if mensaje_split[i] == mensaje_split[i + 1]:
        counter = counter + 1
        
    if mensaje_split[i] != mensaje_split[i + 1]:
        output_str.append(mensaje_split[i+1])
        counterFinal.append(counter)
        counter = 1
    if i + 1 == len(mensaje_split) - 1:
        counterFinal.append(counter)
print(" ".join(output_str))
print(" ".join(map(str, counterFinal)))