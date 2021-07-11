def listar_color(lista):
    output = []
    for i in range(len(lista)):
        if lista[i] not in output:
            output.append(lista[i])
    return output
 

def color_requerido(ID, Lista_Col, color):
    output = []
    for j in range(len(Lista_Col)):
        for i in ID:
            if Lista_Col[i] == color:
                output.append(i)
        break
    return output

# REVISASR ESTA FUNCIÓN

def disponible_compra(ID_dis, ID_Nodis):
    output = []
    for i in ID_dis:
        print(i)
        for j in ID_Nodis:
           if i != ID_Nodis

    return output


print(disponible_compra([3, 5, 7, 10, 15, 16], [4, 10, 5, 8]))
