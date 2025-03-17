# Exemplo de Alocação Estática com Arrays em Python

# Em Python, o conceito de alocação estática se aplica principalmente a arrays de tamanho fixo
# ou quando usamos estruturas que não mudam de tamanho durante a execução.

# Simulando um array de tamanho fixo (apesar de listas em Python serem dinâmicas, esse exemplo serve como analogia)
tamanho = 5
array = [0] * tamanho  # Alocação estática: tamanho fixo

# Preenchendo o array
for i in range(tamanho):
    array[i] = i + 1

# Imprimindo os valores
print("Array de alocação estática:", array)


