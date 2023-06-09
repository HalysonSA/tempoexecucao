import random
import time
import os


def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        # Encontra o índice do menor elemento restante
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j

        # Troca o elemento atual pelo menor elemento restante
        lista[i], lista[min_index] = lista[min_index], lista[i]

# Função para gerar um vetor de tamanho N com números aleatórios


def generate_random_lista(N):
    return [random.randint(1, 100) for _ in range(N)]


# Teste de tempo de execução
N = 100  # Número de testes
# Tamanhos dos vetores a serem testados
lista_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900]

file_path = os.path.join(os.getcwd(), "selection-sort.txt")
with open(file_path, "w") as file:
    for size in lista_sizes:
        total_execution_time = 0
        print(f"Tamanho do vetor: {size}")

        for _ in range(N):
            lista = generate_random_lista(size)

            start_time = time.time()
            selection_sort(lista)
            end_time = time.time()

            execution_time = (end_time - start_time) * \
                1000  # Tempo em milissegundos
            total_execution_time += execution_time

        average_execution_time = total_execution_time / N
        print(f"Tempo médio de execução: {average_execution_time}")
        file.write(f"{size} {average_execution_time}\n")

print("Arquivo gerado com sucesso!")
