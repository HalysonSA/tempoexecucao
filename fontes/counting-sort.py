import random
import time
import os


def count_sort(input, k):
    count = [0] * (k + 1)
    output = [0] * len(input)

    for i in range(len(input)):
        j = input[i]
        count[j] += 1

    for i in range(1, k + 1):
        count[i] += count[i - 1]

    for i in range(len(input) - 1, -1, -1):
        j = input[i]
        count[j] -= 1
        output[count[j]] = input[i]

    return output

# Função para gerar uma lista de tamanho N com números aleatórios


def generate_random_list(N, k):
    return [random.randint(1, k) for _ in range(N)]


N = 100  # Número de testes
# Tamanhos das listas a serem testadas
list_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900]
k = 1000  # Valor máximo da lista

file_path = os.path.join(os.getcwd(), "count-sort.txt")

with open(file_path, "w") as file:
    for size in list_sizes:
        total_execution_time = 0
        print(f"Tamanho da lista: {size}")

        for _ in range(N):
            input_list = generate_random_list(size, k)

            start_time = time.time()
            count_sort(input_list, k)
            end_time = time.time()

            execution_time = (end_time - start_time) * \
                1000  # Tempo em milissegundos
            total_execution_time += execution_time

        average_execution_time = total_execution_time / N
        print(f"Tempo médio de execução: {average_execution_time} ms")
        file.write(f"{size} {average_execution_time}\n")

print("Arquivo gerado com sucesso!")
