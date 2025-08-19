import pandas as pd
import numpy as np # manipulação numerica e estatística 

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

ajustar_senioridade = {
    'EN': 'Junior', 
    'MI': 'Pleno', 
    'SE': 'Sênior',
    'EX': 'Executivo', 
}

df['Senioridade'] = df['Senioridade'].replace(ajustar_senioridade) # ou .map()

ajustar_remoto = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
}
df['Remoto'] = df['Remoto'].map(ajustar_remoto) 

ajustar_contrato = {
    'FT': 'Tempo Integral',
    'PT': 'Meio Período',
    'CT': 'Contrato',
    'FL': 'Freelancer'
}
df['Contrato'] = df['Contrato'].replace(ajustar_contrato) 

ajustar_tamanho = {
    'S': 'Pequena',
    'M': 'Média',
    'L': 'Grande',
}
df['Tamanho'] = df['Tamanho'].replace(ajustar_tamanho)

print(df.head())
print('\n')

print(df.describe(include=object))

print(df.describe())

# Exibe os dados nulos, TRUE é nulo FALSE não é nulo
print(df.isnull())
print('\n')

# Exibe a contagem de dados nulos por coluna
print(df.isnull().sum()) 
print('\n')

# Verificar valores únicos na coluna 'Ano', nan = valor nulo not a number
print(df['Ano'].unique())
print('\n')

# Exibe todos os dados da base que possuem ao menos um valor nulo -> colunas das linhas que estao com valores nulos
print(df[df.isnull().any(axis=1)])
# ao lidar com dados nulos, podemos optar por remover ou substituir os valores nulos, é importante preenche-los para evitar problemas em análises futuras para tomadas de decisão
print('\n')


# Preencher valores nulos -> uma estratégia é preencher com a média, mediana ou moda
# Como nessa base principal os valores nulos estão na coluna ANO, não faz sentido preencher com a média, mediana ou moda, pois o ano é uma variável categórica
# Sendo assim, irei criar um DataFrame totalmente diferente a fim de testar o preenchimento de valores nulos
df_salarios = pd.DataFrame({
    'nome': ['Joao', 'Bruno', 'Bia', 'Yan', 'Ana'],
    'salario': [2000, 100000, 3550, np.nan, np.nan],
})

# Preencher com a media dos salários, tudo que for nulo será preenchido com a média
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2)) # fillna = prencher valores nulos / mean = média / round = arredondar / 2 = duas casas decimais

# Caso exista um valor muito discrepante, podemos optar por preencher com a mediana
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())
print(df_salarios)
print('\n')


# Vao existir casos que nao faz sentido usar media, moda ou mediana, por exemplo quando se trata de temperatura
# Um meio de fazer isso é usando o metodo ffill, que preenche os valores nulos com o valor anterior
df_temperaturas = pd.DataFrame({
    'dia': ['Seg', 'Ter', 'Qua', 'Qui'],
    'temperatura': [np.nan, np.nan, 25, 30] # exemplo para bfill
    # 'temperatura': [25, np.nan, np.nan 30] # exemplo para ffill
})
df_temperaturas['preenchimento_ffill'] = df_temperaturas['temperatura'].ffill() # ffill = forward fill, preenche com o valor anterior


# Caso aconteça de o primeiro valor ser nulo, podemos usar o método bfill, que preenche os valores nulos com o valor posterior
df_temperaturas['preenchimento_bfill'] = df_temperaturas['temperatura'].bfill() # bfill = backward fill, preenche com o valor posterior
print(df_temperaturas)
print('\n')


# É possivel preencher com valores específicos e fixos, por exemplo, preencher com 0 ou não informado usando o método fillna
df_cidades = pd.DataFrame({
    'nome': ['Joao', 'Bruno', 'Bia', 'Yan', 'Ana'],
    'cidade': ['SP', np.nan, 'RJ', 'MG', np.nan]
})
df_cidades['preenchimento_fixo_cidade'] = df_cidades['cidade'].fillna('Não Informado') # Preenche com o valor fixo 'Não Informado'
print(df_cidades)
print('\n')


# Voltando para a base de salários em que não faz sentido optar resolver pelos metodos acima, podemos optar por remover as linhas que possuem valores nulos
df_limpo = df.dropna()
print(df_limpo.isnull().sum())  # Exibe a contagem de valores nulos por coluna após a remoção
print(df_limpo.head()) # ano esta em dicimal pq é float oq é visto aplicando o metodo .info(), para tirar devemos converteer de float para int
print('\n')

df_limpo = df_limpo.assign(Ano = df_limpo['Ano'].astype('int64')) # Converte a coluna 'Ano' de float para int
print(df_limpo.head())
print(df_limpo.info())
# agora sim a coluna ano esta como int64
print('\n')





















