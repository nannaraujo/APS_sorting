def mergesort(lista, inicio=0, fim=None):
    # Verifica se o parâmetro 'fim' foi fornecido, caso contrário, define-o como o comprimento da lista.
    if fim is None:
        fim = len(lista)
    
    # Verifica se há mais de um elemento para ordenar.
    if (fim - inicio > 1):
        # Calcula o ponto médio da lista.
        meio = (fim + inicio)//2
        
        # Chama recursivamente mergesort para a primeira metade da lista.
        mergesort(lista, inicio, meio)
        
        # Chama recursivamente mergesort para a segunda metade da lista.
        mergesort(lista, meio, fim)
        
        # Chama a função merge para combinar as duas metades ordenadas.
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    # Divide a lista em duas partes: 'left' contém elementos da parte esquerda e 'right' contém elementos da parte direita.
    left = lista[inicio:meio]
    right = lista[meio:fim]
    
    # Inicializa variáveis de controle para as partes esquerda e direita.
    top_left, top_right = 0, 0
    
    # Itera sobre a lista resultante após a mesclagem.
    for k in range(inicio, fim):
        # Se todos os elementos da parte esquerda já foram utilizados, adiciona o próximo elemento da parte direita.
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1  

        # Se todos os elementos da parte direita já foram utilizados, adiciona o próximo elemento da parte esquerda.
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1  

        # Compara os elementos da parte esquerda e direita e adiciona o menor deles à lista.
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1

        else:
            lista[k] = right[top_right]
            top_right = top_right + 1       

# Lista inicial.
lista = [0, 2, 4, 1, 10]

# Imprime a lista antes da ordenação.
print(lista)

# Chama a função mergesort para ordenar a lista.
mergesort(lista)

# Imprime a lista após a ordenação.
print(lista)
