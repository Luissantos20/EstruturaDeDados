# 📌 Sistema de Cadastro de Notas e Análise dos Alunos

pip install pandas matplotlib

## 📖 Sobre o Projeto
Este projeto consiste em um **sistema de cadastro de notas e análise do desempenho dos alunos** com base nas suas avaliações e frequência. O sistema permite:
- Registrar alunos e suas notas.
- Calcular a nota final e verificar se o aluno está aprovado, reprovado ou precisará fazer uma avaliação final.
- Gerar **análises visuais** através de **gráficos**.

## 🛠️ Estrutura de Dados Utilizada
A estrutura de dados principal utilizada neste projeto é o **dicionário** (`dict`).

### 🔹 Por que usar um dicionário?
O **dicionário** é uma estrutura de dados do tipo **chave-valor**. Neste projeto:
- A **chave** é o **nome do aluno**.
- O **valor** é uma **tupla contendo suas notas e quantidade de faltas**.

Isso facilita o armazenamento e a recuperação rápida dos dados dos alunos, além de permitir manipulações eficientes na análise do desempenho acadêmico.

## ⚙️ Como Funciona o Sistema?

### 1️⃣ **Cadastro de Alunos**
O programa solicita ao usuário que informe os dados do aluno:
- **Nome**
- **Nota A1**
- **Nota A2**
- **Quantidade de faltas**

Esses dados são armazenados no dicionário `dic_alunos`.

**Exemplo de cadastro:**
```python
aluno = input('Digite o nome do aluno: ')
nota_A1 = float(input('Digite a nota da avaliação A1: '))
nota_A2 = float(input('Digite a nota da avaliação A2: '))
qtde_faltas = float(input('Digite a quantidade de faltas: '))

dic_alunos[aluno] = (nota_A1, nota_A2, qtde_faltas)
```

### 2️⃣ **Cálculo da Nota Final e Situação do Aluno**
O sistema calcula a **nota final** somando as notas A1 e A2. Compara também a porcentagem de faltas com o limite permitido (25%).

Critérios de aprovação:
- Nota final **≥ 6** e faltas **≤ 25%** → ✅ **Aprovado**
- Faltas **> 25%** → ❌ **Reprovado por falta**
- Alguma nota **< 1** → ❌ **Reprovado direto**
- Caso contrário → 📝 **Avaliação Final**

**Exemplo de lógica aplicada:**
```python
if nota_final >= 6 and porcentagem_faltas <= 0.25:
    situacao = 'APROVADO!'
elif porcentagem_faltas > 0.25:
    situacao = 'REPROVADO POR FALTA!'
elif nota_A1 < 1 or nota_A2 < 1:
    situacao = 'REPROVADO!'
else:
    situacao = 'AVALIAÇÃO FINAL!'
```

Os resultados são armazenados no dicionário `situacao_alunos`.

### 3️⃣ **Exibição dos Dados em Tabelas**
Os dados são organizados em **DataFrames** (do Pandas) para melhor visualização.

**Exemplo de exibição de tabela:**
```python
df_alunos = pd.DataFrame.from_dict(dic_alunos, orient='index', columns=['Nota A1', 'Nota A2', 'Quantidade de Faltas'])
df_situacao = pd.DataFrame.from_dict(situacao_alunos, orient='index', columns=['Nota Final', 'Porcentagem de Faltas (%)', 'Situação'])
```

### 4️⃣ **Geração de Gráficos** 📊
Para melhor análise do desempenho dos alunos, o programa gera **vários gráficos**:
1. **Gráfico de Barras** - Exibe as notas A1, A2 e quantidade de faltas.
2. **Gráfico de Dispersão** - Mostra a relação entre faltas e notas.
3. **Gráfico de Pizza** - Exibe a porcentagem de alunos aprovados, reprovados e em avaliação final.

**Exemplo de código para criar o gráfico de barras:**
```python
plt.figure(figsize=(12, 6))
df_alunos[['Nota A1', 'Nota A2', 'Quantidade de Faltas']].plot(kind='bar', color=['skyblue', 'orange', 'red'])
plt.title('Notas A1 e A2 dos Alunos e Quantidade de Faltas')
plt.xlabel('Alunos')
plt.ylabel('Notas e Faltas')
plt.xticks(rotation=45)
plt.legend(['Nota A1', 'Nota A2', 'Faltas'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
```

## 📌 Conclusão
Este projeto **automatiza o processo de análise de desempenho acadêmico**, oferecendo um meio rápido e eficiente de registrar, calcular e visualizar os resultados dos alunos. A escolha do **dicionário** como estrutura de dados foi essencial para permitir o armazenamento e acesso rápido das informações, facilitando a manipulação dos dados e a análise dos resultados.

Os **gráficos** gerados ajudam na compreensão visual das dificuldades enfrentadas pelos alunos, permitindo identificar padrões e possíveis melhorias no processo de ensino.

🚀 **Este sistema pode ser ampliado para incluir mais métricas e funcionalidades, tornando-se uma ferramenta ainda mais poderosa para avaliação educacional!**

