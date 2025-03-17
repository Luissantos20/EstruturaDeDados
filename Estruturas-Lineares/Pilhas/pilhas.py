# Criando uma pilha
pilha = []

# Empilhando (adicionando elementos)
pilha.append(1)  # Pilha: [1]
pilha.append(2)  # Pilha: [1, 2]
pilha.append(3)  # Pilha: [1, 2, 3]

# Desempilhando (removendo o topo)
pilha.pop()  # Pilha após desempilhar: [1, 2]

# Acessando o topo da pilha sem removê-lo
print("Topo da pilha:", pilha[-1])  # Saída: 2

# Verificando se a pilha está vazia
print("Pilha está vazia?", len(pilha) == 0)  # Saída: False