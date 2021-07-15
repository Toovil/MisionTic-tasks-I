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

def disponible_compra(ID_dis, ID_Nodis):
    lista = []
    for i in ID_dis:
        if i not in ID_Nodis:
            lista.append(i)
    return lista

def disponible_venta(ID_Nodis, Require_ID):
    counter1 = 0
    counter2 = 0
    for i in Require_ID:
        if i not in ID_Nodis:
            counter1 += 1
    for j in ID_Nodis:
        if j not in Require_ID:
            counter2 += 1
    if counter1 < counter2:
        return counter1
    else:
        return counter2

print(disponible_venta([4, 2, 17, 1, 0, 15, 5, 13, 23, 8],[3, 10, 0, 23, 19, 17, 22, 18, 16, 8, 2, 12]))