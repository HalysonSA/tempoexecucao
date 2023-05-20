import random
import time


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encontra o índice do menor elemento restante
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Troca o elemento atual pelo menor elemento restante
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Função para gerar um vetor de tamanho N com números aleatórios


def generate_random_array(N):
    return [random.randint(1, 100) for _ in range(N)]


# Teste de tempo de execução
N = 10000  # Número de testes
# Tamanhos dos vetores a serem testados
array_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900]


with open("../graficos/select-sort.txt", "w") as file:
    for size in array_sizes:
        total_execution_time = 0
        print(f"Tamanho do vetor: {size}")

        for _ in range(N):
            arr = generate_random_array(size)

            start_time = time.time()
            selection_sort(arr)
            end_time = time.time()

            execution_time = end_time - start_time
            total_execution_time += execution_time

        average_execution_time = total_execution_time / N
        print(f"Tempo médio de execução: {average_execution_time}")
        file.write(f"{size} {average_execution_time}\n")

print("Arquivo gerado com sucesso!")
