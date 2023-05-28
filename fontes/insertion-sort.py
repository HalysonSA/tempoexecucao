import random
import time
import os


def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        k = i
        while k > 0 and chave < lista[k - 1]:
            lista[k] = lista[k - 1]
            k -= 1
        lista[k] = chave


# Função para gerar uma lista de tamanho N com números aleatórios
def generate_random_list(N):
    return [random.randint(1, 100) for _ in range(N)]


def generate_worst_case(size):
    return list(range(size, 0, -1))


def generate_best_case(size):
    return list(range(1, size + 1))


# Teste de tempo de execução
N = 100  # Número de testes
# Tamanhos das listas a serem testadas
list_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900]

# Mudar o nome do arquivo para a função que está sendo usada
file_path = os.path.join(os.getcwd(), "insertion-sort.txt")
with open(file_path, "w") as file:
    for size in list_sizes:
        total_execution_time = 0
        print(f"Tamanho da lista: {size}")

        for _ in range(N):
            # generate_worst_case(size)   generate_random_list(size)  generate_best_case(size)
            lista = generate_random_list(size)
            start_time = time.time()
            insertion_sort(lista)
            end_time = time.time()

            execution_time = (end_time - start_time) * \
                1000  # Tempo em milissegundos
            total_execution_time += execution_time

        average_execution_time = total_execution_time / N
        print(f"Tempo médio de execução: {average_execution_time}")
        file.write(f"{size} {average_execution_time}\n")

print("Arquivo gerado com sucesso!")
