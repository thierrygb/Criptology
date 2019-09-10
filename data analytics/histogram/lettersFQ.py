# -*- coding: utf-8 -*-

import pylab as pl
import numpy as np

nome = input("Digite o nome do arquivo: ")
with open(nome, 'r', encoding='UTF-8') as arq:
    string1 = str(arq.read().encode(encoding=('UTF-8')))
    arq.close()

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", ",", ";", "-", "_", "+"]

# A função abaixo efetua o calculo do numero de ocorrencia de um caractere
# A saida é uma lista dos caracteres seguidos de suas ocorrencia

def ocorrencias(string, letras):
    lista_frequencias = []

    for letra in letras:
        freq = 0
        for i in string:
            if i == letra:
                freq += 1
        if freq != 0:
            lista_frequencias.append(letra)
            lista_frequencias.append(freq)
    return lista_frequencias

print(ocorrencias(string1, alfabeto))

# Essa função retorna duas listas, a de letras e suas respectivas frequencias
def lista_letras(list_1):
    lista_letras = []
    lista_letras.append(list_1[0])
    lista_freq = []

    for i in range(1, len(list_1)):
        if i % 2 == 0:
            lista_letras.append(list_1[i])
        else:
            lista_freq.append(list_1[i])
    if len(lista_letras) != len(lista_freq):
        return "ERRO!"
    else:
        final_list = [lista_letras, lista_freq]
        return final_list

count = ocorrencias(string1,alfabeto)

final = lista_letras(count)
letras = final[0]
freq = final [1]
print("Total de caracteres",sum(freq), sep=" ")

def freq_relativa(list_1):
    list_to_ret = []
    for i in list_1:
        list_to_ret.append(i/sum(list_1))
    return list_to_ret

freq = freq_relativa(freq)

fig = pl.figure()
ax = pl.subplot(111)
width = 0.8
ax.bar(range(len(letras)), freq, width=width)
ax.set_xticks(np.arange(len(letras)) + width/2)
ax.set_xticklabels(letras, rotation=45)
pl.show()