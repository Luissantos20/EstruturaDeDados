# Criando uma fila
fila = []

# Enfileirando (adicionando elementos)
fila.append(1)  # Fila: [1]
fila.append(2)  # Fila: [1, 2]
fila.append(3)  # Fila: [1, 2, 3]
print(f"Fila após enfileirar: {fila}")

# Desenfileirando (removendo o primeiro item)
item_removido = fila.pop(0)  # Fila após desenfileirar: [2, 3]
print(f"Item removido: {item_removido}")
print(f"Fila após desenfileirar: {fila}")

# Acessando o primeiro item da fila sem removê-lo
print(f"Primeiro item da fila: {fila[0]}")  # Saída: 2

# Verificando se a fila está vazia
if len(fila) == 0:
    print("A fila está vazia!")
else:
    print("A fila não está vazia.")
