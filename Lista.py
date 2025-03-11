def ordenar_por_primer_element(tupla):
    return tupla[0]

def ordenar_por_segundo_elemnto(tupla):
    return tupla[1]

lista = [(5,2),(8,1), (7,3), (4,8)]

lista_ordenada = sorted(lista, key=ordenar_por_segundo_elemnto)
print("Lista original:",lista)
print("Lista ordenada:",lista_ordenada)

lista_nueva=sorted(lista, key=lambda tupla: tupla[1])
print("Lista ordenada:",lista_nueva)


"""
Vamos a tener un grafo 
"""