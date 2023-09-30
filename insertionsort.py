from utils import read_txt as rtxt
import time

selected_file, list_of_numbers = rtxt.read_file_content()
print(list_of_numbers)
print("#######################################################")
start_time = time.time()

# Faz o loop no tamanho da lista
for i in range(1,len(list_of_numbers)):
    j = i
    # Enquanto o valor do indice anterior for maior que o atual, faz a troca
    while list_of_numbers[j - 1] > list_of_numbers[j] and j > 0:
        list_of_numbers[j - 1], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[j - 1]
        # Diminue o index a ser checado, fazendo assim, o while checar todo o loop
        j -= 1

end_time = time.time()

print(list_of_numbers)
print(f"Tempo levado pelo algoritmo de InsertionSort: {end_time-start_time}")
print(f"Arquivo: {selected_file}")