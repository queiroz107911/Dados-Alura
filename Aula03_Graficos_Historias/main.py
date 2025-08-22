import pandas as pd # é possivel usar para plotar graficos
import numpy as np  # manipulação numerica e estatística
import matplotlib.pyplot as plt  # Necessário para exibir o gráfico
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


df_limpo = df.dropna()
print(df_limpo.isnull().sum())  

df_limpo = df_limpo.assign(Ano = df_limpo['Ano'].astype('int64')) # Converte a coluna 'Ano' de float para int
print(df_limpo.head())
print('\n')

# Usando somente pandas o grafico é criado porem não é exibido, para ser exibido é necessario importar o matplotlib.pyplot e usar o plt.show()
df_limpo['Senioridade'].value_counts().plot(kind='bar', title='Vagas por Senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Vagas')
plt.show()

# calcular o salario medio para cada senioridade
sns.barplot(data=df_limpo, x='Senioridade', y='Salario_USD')
plt.show()

# Personalizando o gráfico é bom usar matplotlib
plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='Senioridade', y='Salario_USD')
plt.title('Salário Médio por Senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salário Médio Anual (USD)')
plt.show()

# exibe a media salarial por senioridade no console do maior pro menor
print(df_limpo.groupby('Senioridade')['Salario_USD'].mean().sort_values(ascending=False)) # sort é usado para ordenar os valores / colocar False para ordenar do maior pro menor e True do menor pro maior
ordem = df_limpo.groupby('Senioridade')['Salario_USD'].mean().sort_values(ascending=False).index # index é usado para pegar o indice do resultado
print(ordem)
print('\n')

plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='Senioridade', y='Salario_USD', order=ordem) # order é usado para ordenar os valores
plt.title('Salário Médio por Senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salário Médio Anual (USD)')
plt.show()
# Juntamente com a variavel ordem que foi passada como parametro dentro de sns.barplot(), nota-se que o gráfico foi ordenado tornando sua visuzalização e entendimento mais fácil.


# Distruibuição salarial num histograma
plt.figure(figsize=(8, 4)) # bin é usado para definir o numero de barras que o grafico vai ter, o intervalo, e nesse caso é de 50 em 50
sns.histplot(df_limpo['Salario_USD'], bins=50, kde=True) # kde é usado para adicionar uma linha de densidade ao gráfico
plt.title('Distribuição Salarial Anual')
plt.xlabel('Salário (USD)')
plt.ylabel('Frequência')
plt.show()    

# Distribuição salarial num boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x=df_limpo['Salario_USD'])
plt.title('Distribuição Salarial Anual')
plt.xlabel('Salário (USD)') 
plt.show()

# Organizando os dados por senioridade e salario, é como se fosse uma caixa para cada nivel de senioridade
ordem_senioridade = ['Junior', 'Pleno', 'Sênior', 'Executivo']
plt.figure(figsize=(8, 5))
sns.boxplot(x='Senioridade', y='Salario_USD', data=df_limpo, order=ordem_senioridade)
plt.title('Boxplot da Distribuição Salarial por Senioridade')
plt.xlabel('Senioridade')   
plt.show()

# Mudar as cores do boxplot
ordem_senioridade = ['Junior', 'Pleno', 'Sênior', 'Executivo']
plt.figure(figsize=(8, 5))
sns.boxplot(x='Senioridade', y='Salario_USD', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='Senioridade') # 'set2' é uma paleta de cores do seaborn
plt.title('Boxplot da Distribuição Salarial por Senioridade')
plt.xlabel('Senioridade')  
plt.show()


# Graficos interativos com plotly 
# Gráfico de barras interativo

senioridade_media_salario = df_limpo.groupby('Senioridade')['Salario_USD'].mean().sort_values(ascending=False).reset_index()
fig = px.bar(senioridade_media_salario,
             x='Senioridade',
             y='Salario_USD',
             title='Salário Médio por Senioridade',
             labels={'Senioridade': 'Nivel de Senioridade', 'Salario_Usd': 'Media Salarial (USD)'})
fig.show()  # Exibe o gráfico interativo onde ao passar o mouse sobre as barras, é possível ver o valor exato de cada barra e cada valor foi calculado pela media

# Gráfico de pizza interativo
remoto_contagem = df_limpo['Remoto'].value_counts().reset_index() # contagem da frequencia de cada categoria
remoto_contagem.columns = ['tipo_trabalho', 'quantidade'] # renomeando as colunas
fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção do tipo de trabalho (Remoto, Híbrido, Presencial)')
fig.show() 

# Grafico rosca interativo
remoto_contagem = df_limpo['Remoto'].value_counts().reset_index() # contagem da frequencia de cada categoria
remoto_contagem.columns = ['tipo_trabalho', 'quantidade'] # renomeando as colunas
fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção do tipo de trabalho (Remoto, Híbrido, Presencial)',
             hole=0.5) # hole é usado para criar o buraco no meio do gráfico, transformando-o em um gráfico de rosca
fig.update_traces(textinfo='percent+label') # textinfo é usado para mostrar o percentual e o label dentro do gráfico
fig.show() 


df_limpo.to_csv('Dados_Imersão.csv', index=False)  # Salva o DataFrame em um arquivo CSV, nao criar um index a mais, em cima do arquivo
