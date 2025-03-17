### Exemplo prático para ilustrar o impacto da escolha da estrutura de dados no desempenho. ###
import time

# Estrutura de Dados: Lista
def buscar_lista(lista, valor):
    for item in lista:
        if item == valor:
            return True
    return False

# Estrutura de Dados: Dicionário (equivalente a uma árvore hash)
def buscar_dicionario(dicionario, valor):
    return valor in dicionario

# Criando uma lista de 1 milhão de elementos
lista = list(range(1000000))

# Criando um dicionário com 1 milhão de elementos
dicionario = {i: None for i in range(1000000)}

# Função para medir o tempo de execução
def medir_tempo(func, *args):
    inicio = time.perf_counter()  # Usando time.perf_counter() para medir o tempo com mais precisão
    func(*args)
    fim = time.perf_counter()
    return fim - inicio

# Medindo o tempo para buscar um elemento na lista
tempo_lista = medir_tempo(buscar_lista, lista, 999999)

# Medindo o tempo para buscar um elemento no dicionário
tempo_dicionario = medir_tempo(buscar_dicionario, dicionario, 999999)

# Mostrando os resultados
print(f"Tempo para buscar na lista: {tempo_lista:.6f} segundos")
print(f"Tempo para buscar no dicionário: {tempo_dicionario:.6f} segundos")


#Explicação:

#No exemplo acima, comparamos o tempo de busca entre uma lista e um dicionário (que é uma estrutura de dados baseada em hash). A busca na lista é feita de forma sequencial, o que leva mais tempo à medida que a lista cresce. No dicionário, a busca é feita em tempo constante O(1), o que é muito mais rápido. 🚀

#Resultado esperado:

#O tempo de busca na lista será significativamente maior do que no dicionário, especialmente com listas grandes. ⏳