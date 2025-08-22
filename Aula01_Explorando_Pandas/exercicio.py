# Exercício: Análise de Salários na Área de Dados
# Carregue a mesma base de dados de salários que foi utilizada na aula
# Renomeie as colunas para que fiquem em português, seguindo o padrão que foi ensinado
# Utilize o método describe() para obter estatísticas descritivas das colunas numéricas
# Utilize o método value_counts() para analisar a coluna de "senioridade" 
# e descubra qual é o nível de experiência mais comum
# Crie um gráfico simples utilizando a biblioteca Matplotlib ou Seaborn 
# para visualizar a distribuição dos salários em relação ao nível de experiência.

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

print(df.head())
print(df.columns)

print('\n')

renomeando_colunas = {

    'work_year': 'ano', 
    'experience_level': 'senioridade', 
    'employment_type': 'contrato' , 
    'job_title': 'cargo',
    'salary': 'salario', 
    'salary_currency': 'moeda_salarial',
    'salary_in_usd': 'salario_usd',
    'employee_residence': 'residencia_empregado',
    'remote_ratio': 'relacao_remota',
    'company_location': 'localizacao_empresa',
    'company_size': 'tamanho_empresa'
}

df.rename(columns=renomeando_colunas, inplace=True) # inplace=True modifica o DataFrame original
print(df.columns)

print('\n')

print(df.value_counts('senioridade'))

print('\n')

renomear_senioridade = {
    'SE': 'Sênior',
    'MI': 'Pleno',
    'EN': 'Júnior',
    'EX': 'Executivo'   
}
df['senioridade'] = df['senioridade'].map(renomear_senioridade) # usa-se df['senioridade'] para acessar a coluna requerida e depois atribui a mudança utilizando do .map ou do .replace 
print(df['senioridade'])

print('\n')

senioridade_mais_comum = df['senioridade'].mode()[0]  # o metodo mode() obtém o valor mais comum e o 0 é utilizado para pegar o primeiro valor da Series
quantidade = df['senioridade'].value_counts()[senioridade_mais_comum] 
# conta os valores unicos em df['senioridade'] 
# porem ao colocar [senioridade_mais_comum] o value.counts() é aplicado no conteudo da variavel senioridade_mais_comum
# ou seja, conta quantas vezes o que esta dentro da variavel se repetiu

print(f"O valor mais comum é '{senioridade_mais_comum}' e aparece '{quantidade}' vezes.")

print('\n')

print(df.describe())

# Agrupa por senioridade e calcula a média dos salários
salario_por_senioridade = df.groupby('senioridade')['salario'].mean().sort_values(ascending=True)

plt.figure(figsize=(8,5))
salario_por_senioridade.plot(kind='bar', color='m') #kind= 'pie' = 'bar' = 'line' = 'hist' = 'box' = 'barh'
plt.title('Distribuição Média de Salários por Senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salário Médio - USD')
plt.xticks(rotation=0)  # deixa os rótulos na horizontal
plt.show()
