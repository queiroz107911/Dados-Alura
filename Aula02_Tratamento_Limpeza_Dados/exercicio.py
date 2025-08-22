# Que tal fazer um exercício onde você cria um DataFrame fictício com informações de estudantes, 
# incluindo colunas como "nome", "idade", "nota" e "cidade"

# Aqui estão os passos que você pode seguir:

# Crie um DataFrame com pelo menos 5 estudantes, onde algumas notas estejam ausentes 
# (use np.nan para representar os valores nulos)
# Aplique o método isnull() para verificar quantas notas estão faltando
# Preencha as notas ausentes com a média das notas dos estudantes que têm nota
# Converta a coluna "idade" para o tipo inteiro, caso esteja como float
# Exiba o DataFrame final e verifique se as notas foram preenchidas corretamente e se a idade está no formato correto

# Esse exercício vai te ajudar a praticar a limpeza de dados e a manipulação de DataFrames, assim como vimos na aula!
import pandas as pd
import numpy as np

df_alunos = pd.DataFrame({

    'nome': ['Joao', 'Yan', 'Henrrique', 'Gustavo', 'Kaio'],
    'idade': [19, 20, 15, 23, 30],
    'nota': [np.nan, 50, 35, np.nan, 0],
    'cidade': ['brasilia', 'paraiba', 'sao paulo', 'tocantins', 'natal']

})

print(df_alunos.isnull().sum())

print('\n')

df_alunos['ajeitando_nota'] = df_alunos['nota'].fillna(df_alunos['nota'].mean().round(2)) # divide pelos valores validos
# usando df_alunos['media_aluno'] no inicio faz com que apareça uma coluna a mais no df_alunos chamada de media_aluno

print(type(df_alunos['idade'][0]))

print('\n')

print(df_alunos)
