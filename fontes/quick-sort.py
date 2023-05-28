import random
import time
import os


def quick_sort(a, ini=0, fim=None):
    fim = fim if fim is not None else len(a)
    if ini < fim:
        pp = particao(a, ini, fim)
        quick_sort(a, ini, pp)
        quick_sort(a, pp + 1, fim)
    return a


def particao(a, ini, fim):
    pivo = a[fim - 1]
    for i in range(ini, fim):
        if a[i] <= pivo:
            a[i], a[ini] = a[ini], a[i]
            ini += 1

    return ini - 1


def generate_random_array(N):
    return [random.randint(1, 100) for _ in range(N)]


N = 100  # Número de testes
array_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900]

file_path = os.path.join(os.getcwd(), "quick-sort.txt")
with open(file_path, "w") as file:
    for size in array_sizes:
        total_execution_time = 0
        print(f"Tamanho do array: {size}")

        for _ in range(N):
            array = generate_random_array(size)

            start_time = time.time()
            quick_sort(array)
            end_time = time.time()

            execution_time = (end_time - start_time) * \
                1000  # Tempo em milissegundos
            total_execution_time += execution_time

        average_execution_time = total_execution_time / N
        print(f"Tempo médio de execução: {average_execution_time}")
        file.write(f"{size} {average_execution_time}\n")

print("Arquivo gerado com sucesso!")
