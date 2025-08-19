# Apresente um gráfico com o salário medio de Cientista de Dados por país

import pandas as pd # é possivel usar para plotar graficos
import numpy as np  # manipulação numerica e estatística
import matplotlib.pyplot as plt  # Necessário para exibir o gráfico
import matplotlib.ticker as mtick
import seaborn as sns  # biblioteca de visualização de dados baseada no matplotlib
import plotly.express as px  # biblioteca de visualização de dados interativa

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

renomear_colunas = {

    'work_year': 'Ano', 
    'experience_level': 'Senioridade', 
    'employment_type': 'Contrato', 
    'job_title': 'Cargo',   
    'salary': 'Salario',  
    'salary_currency': 'Moeda', 
    'salary_in_usd': 'Salario_USD', 
    'employee_residence': 'Residencia',
    'remote_ratio': 'Remoto', 
    'company_location': 'Localizacao', 
    'company_size': 'Tamanho'
}
df.rename(columns=renomear_colunas, inplace=True)

print(df.head())
print('\n')

pd.set_option('display.float_format', '{:.2f}'.format) # formatar floats com 2 casas decimais, pandas costuma exibir em notacao cientifica


df_cd = df[df['Cargo'] == 'Data Scientist']
df_media_salario_residencia = df_cd.groupby('Residencia')['Salario'].mean().reset_index(name='salario_medio')
print(df_media_salario_residencia)

print('\n')


# Ordena e pega os 15 países com maior salário médio
df_top = df_media_salario_residencia.sort_values(by='salario_medio', ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.bar(df_top['Residencia'], df_top['salario_medio'], color='skyblue')

# Formata eixo Y para valores normais com separador de milhar
plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}')) 

plt.xticks(rotation=45, ha='right')
plt.xlabel("País", fontsize=12)
plt.ylabel("Salário Médio (USD)", fontsize=12)
plt.title("Top 10 - Salário médio de Cientistas de Dados por País", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()


