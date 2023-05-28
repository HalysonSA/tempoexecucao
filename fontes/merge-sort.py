import random
import time
import os


def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]

        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):
            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k] = listaDaEsquerda[i]
                i += 1
            else:
                lista[k] = listaDaDireita[j]
                j += 1
            k += 1

        while i < len(listaDaEsquerda):
            lista[k] = listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k] = listaDaDireita[j]
            j += 1
            k += 1

    return lista


# Função para gerar uma lista de tamanho N com números aleatórios
def generate_random_list(N):
    return [random.randint(1, 100) for _ in range(N)]


# Teste de tempo de execução
N = 100  # Número de testes
# Tamanhos das listas a serem testadas
list_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900]


file_path = os.path.join(os.getcwd(), "merge-sort.txt")
with open(file_path, "w") as file:
    for size in list_sizes:
        total_execution_time = 0
        print(f"Tamanho da lista: {size}")

        for _ in range(N):
            lista = generate_random_list(size)

            start_time = time.time()
            mergeSort(lista)
            end_time = time.time()

            execution_time = (end_time - start_time) * \
                1000  # Tempo em milissegundos
            total_execution_time += execution_time

        average_execution_time = total_execution_time / N
        print(f"Tempo médio de execução: {average_execution_time}")
        file.write(f"{size} {average_execution_time}\n")

print("Arquivo gerado com sucesso!")
