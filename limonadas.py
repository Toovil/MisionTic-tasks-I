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

print(color_requerido([5, 15, 6, 7, 19, 11, 25, 22, 14, 18, 21],[2, 3, 1, 3, 2, 4, 2, 2, 2, 4, 3, 4, 4, 3, 4, 3, 3, 2, 3, 4, 4, 1, 4, 1, 3, 3, 2, 2],4))
