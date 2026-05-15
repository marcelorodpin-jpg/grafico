import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo Excel
dados = pd.read_excel("dados.xlsx")

# Separando as colunas
periodo = dados["Periodo"]
valor = dados["Valor"]

# Criando o gráfico
plt.figure(figsize=(10, 5))
plt.plot(periodo, valor, marker="o") # Grafico com pontos
plt.bar(periodo, valor) # grafico de barras
plt.fill_between(periodo, valor) # grafico entre



# Deixando as legendas do eixo X na vertical
plt.xticks(rotation=80)

# Configurações do gráfico
plt.title("Evolução dos Valores ao Longo do Tempo")
plt.xlabel("Período")
plt.ylabel("Valor")
plt.grid(axis="y")
plt.grid(axis="x")

# Ajusta automaticamente os espaços
plt.tight_layout()

# Exibindo o gráfico
plt.show()