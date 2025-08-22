import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Exibir as 5 primeiras linhas do DataFrame
print(df.head())
print('\n')

# Exibir informações gerais sobre o DataFrame
print(df.info())
print('\n')

# Exibir os nomes das colunas
print(df.columns)
print('\n')

# Exibir o número de linhas e colunas
print(df.shape)
print('\n')

# Exibir os tipos de dados de cada coluna
print(df.dtypes)
print('\n')


linhas, colunas = df.shape[0], df.shape[1]
print(f"O DataFrame tem {linhas} linhas e {colunas} colunas.")
print('\n')

# Exibir os nomes das colunas
print(df.columns)
print('\n')

# Renomear colunas para português
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
print(df.columns)
print('\n')

# Exibir a contagem de valores únicos na coluna 'Senioridade'
print(df['Senioridade'].value_counts())
print('\n')

# Ajustando as siglas de senioridade, remoto, contrato e tamanho para ficar mais claro para o usuário

ajustar_senioridade = {
    'EN': 'Junior', 
    'MI': 'Pleno', 
    'SE': 'Sênior',
    'EX': 'Executivo', 
}

df['Senioridade'] = df['Senioridade'].replace(ajustar_senioridade) # ou .map()
print(df['Senioridade'].value_counts())
print('\n')

ajustar_remoto = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
}
df['Remoto'] = df['Remoto'].map(ajustar_remoto) # ou .replace()
print(df['Remoto'].value_counts())
print('\n')

ajustar_contrato = {
    'FT': 'Tempo Integral',
    'PT': 'Meio Período',
    'CT': 'Contrato',
    'FL': 'Freelancer'
}
df['Contrato'] = df['Contrato'].replace(ajustar_contrato) 
print(df['Contrato'].value_counts())
print('\n')

ajustar_tamanho = {
    'S': 'Pequena',
    'M': 'Média',
    'L': 'Grande',
}
df['Tamanho'] = df['Tamanho'].replace(ajustar_tamanho)
print(df['Tamanho'].value_counts())
print('\n')

print(df.head())
print('\n')

# Exibir estatísticas categóricas
print(df.describe(include=object))

# Exibir estatísticas numéricas
print(df.describe())


# Com isso já conseguimos responder algumas perguntas, como:

# 1- Qual o nível de experiência mais comum na base de dados?
# 2- Qual é o tipo de contrato mais frequente?
# 3- Qual o cargo mais frequente na amostra?
# 4- De qual país são a maioria dos profissionais da base?
# 5- Qual é o país onde mais empresas da amostra estão sediadas?
# 6- Qual o regime de trabalho mais comum?
# 7- Qual é o tamanho mais comum das empresas na amostra?







