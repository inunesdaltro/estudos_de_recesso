import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
file_path = "vgchartz-2024.xlsx"
df = pd.read_excel(file_path)

# Converter a coluna de datas para datetime
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Criar uma coluna com o mês de lançamento
df['release_month'] = df['release_date'].dt.month

# Filtrar dados da distribuidora "Activision"
df_activision = df[df['publisher'] == 'Activision']

# Agrupar as vendas da Activision por mês
activision_sales_by_month = df_activision.groupby('release_month')['total_sales'].sum()

# Criar o gráfico de linhas para as vendas da Activision por mês
plt.figure(figsize=(10, 5))
plt.plot(activision_sales_by_month.index, activision_sales_by_month.values, marker='o', linestyle='-', color='b')

# Adicionar rótulos e título
plt.xlabel("Mês de Lançamento")
plt.ylabel("Total de Vendas (milhões)")
plt.title("Vendas Mensais da Activision")
plt.xticks(range(1, 13))  # Definir os meses no eixo X
plt.grid(True)

# Exibir o gráfico
plt.show()
