import pandas as pd
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv(r"C:\Users\Gustavo1\Documents\Programming_codes\POS-ALURA\A1-analise-exploracao-dados\bases\A150850189_28_143_208.csv", encoding="utf-8-sig",
            skiprows=3, sep=";", skipfooter=12, thousands=".", decimal=",", engine="python")

pd.set_option('display.float_format','{:.2f}'.format)
#pd.get_option('float_format', "{:.2f}".format())

#dados['2021/Set'].mean(numeric_only=True)
dados = dados.rename({dados.columns[0]:'UF'}, axis='columns')

### Desafio 1: Executar o comando anterior com os dados mais recentes na base
### Desafio 2: Deixar as legendas ânguladas (45, 90, etc) para facilitar a leitura
colunas_usaveis = dados.mean(numeric_only=True).index.tolist()
colunas_usaveis.insert(0, 'UF')

dados_usaveis = dados[colunas_usaveis]

dados_usaveis = dados_usaveis.set_index('UF')

# O metodo " T ", transpoem as colunas e linhas, basicamente inverte as colunas com as linhas
dados_usaveis = dados_usaveis.drop('Total', axis=1)

### Desafio 3: reposicionar a legenda. Dentro? Fora? Onde?
### Desafio 4: Retocar o título da visualização
### Desafio 5: Adicionar títulos aos dois eixos

dados_usaveis['Total'] = dados_usaveis.sum(axis=1)
dados_usaveis = dados_usaveis.astype(float)
dados_usaveis = dados_usaveis/100000

##### Desafio 6: Ordernar dataframe com base na coluna total, para que na primeira tenha a linha com maior gasto, e na última coluna com menor gasto (ordenação)
##### Desafio 7: adicionar uma coluna com a região de cada estado
##### Desafio 8: adicione seu estado nessa lista de 7 estados

np.random.seed(42)
dados_dos_7_estados = dados_usaveis.sample(7)

# Desafio 8 e desafio 7
dados_dos_7_estados.loc[7] = dados_usaveis.loc['35 São Paulo']
dados_dos_7_estados = dados_dos_7_estados.rename(index={7:'35 São Paulo'})

dados_dos_7_estados['Região'] = None
for i in range(len(dados_dos_7_estados.index)):
    #x = int(dados_usaveis.index[i][:2])
    if int(dados_dos_7_estados.index[i][:2]) >= 11 and int(dados_dos_7_estados.index[i][:2]) <= 16:
        dados_dos_7_estados.iloc[[i][:2], -1] = 'Norte'
    elif int(dados_dos_7_estados.index[i][:2]) >= 17 and int(dados_dos_7_estados.index[i][:2]) <= 29:
        dados_dos_7_estados.iloc[[i][:2], -1]  = 'Nordeste'
    elif int(dados_dos_7_estados.index[i][:2]) >= 31 and int(dados_dos_7_estados.index[i][:2]) <= 35:
        dados_dos_7_estados.iloc[[i][:2], -1]  = 'Sudeste'
    elif int(dados_dos_7_estados.index[i][:2]) >= 41 and int(dados_dos_7_estados.index[i][:2]) <= 50:
        dados_dos_7_estados.iloc[[i][:2], -1] = 'Sul'
    else:
        dados_dos_7_estados.iloc[[i][:2], -1]  = 'Centro-Oeste'

# Desafio 6
dados_dos_7_estados.sort_values(by='Total', ascending=False)
ordenados_por_total = dados_dos_7_estados
ordenados_por_total = ordenados_por_total.drop('Total', axis=1)

colunas_interessantes = ordenados_por_total.columns[6:]
ordenados_por_total = ordenados_por_total[colunas_interessantes]

##### Desafio 9: Formatar o gráfico (titulo, legenda, eixos, rotulos, valores)
##### Desafio 10: Pesquisar a função sort_index
##### Desafio 11: Pesquisar os casos de dengue no Brasil e verificar se existe algum padrão com os gastos encontrados aqui
##### Desafio 12: Plotar apenas os dados de uma região do brasil

np.random.seed(42)
ordenados_por_total.iloc[:,:-2] = ordenados_por_total.iloc[:,:-2].astype(float)

#print(ordenados_por_total.T.columns)
# Formatação eixo Y
ordenados_por_total.T.iloc[:20,:].plot(figsize=(10,6))
current_values = plt.gca().get_yticks() # Armazena valores do eixo Y
plt.gca().set_yticklabels(['R${:,.0f}'.format(x) for x in current_values]) # Formata e configura rotulo do eixo Y
plt.title('Gasto total com saúde por mês/ano')
plt.legend(bbox_to_anchor=(1.25, 1.015), loc='upper right')
plt.xlabel('Período')
plt.ylabel('Gasto aprovado em milhões de reais')
plt.show()


#regiao_especifica = ordenados_por_total[ordenados_por_total['Região'] == 'Sul']
#regiao_especifica.T.iloc[:10,:].plot(figsize=(8,4))

#print(ordenados_por_total.dtypes)