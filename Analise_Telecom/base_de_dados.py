#Analise de dados, tratamentos de dados grafico em python tabelas(fataFrames )

#passo 1:Importa a base de dados 
import pandas as pd

tabela = pd.read_csv("Dados/telecom_users.csv")

#passo 2:Vizualizar a base de dados 
display(tabela)


#passo3: 
#Coluna unnamed é inutil 
tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)

#Ver se tem colunas que eram pra ser numero, e esta sendo reconhecida como texto
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

print(tabela.info())

#valor vazio(NaN)
#Primeiro excluir colunas vazias depois as linhas vazias, seguir sempre essa ordem
#Colunas completamentes vazias 
tabela = tabela.dropna(how="all", axis=1)
#Linhas vazias 
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())

#passo 4: como esta os nossos cancelamentos
display(tabela["Churn"].value_counts())
#em percentual
display(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) 

#passo 5:
#A primeira explicação mostra apenas o grafico de MesesComoCliente
#No segundo mostra o grafico de todas as tabelas 
#ao colocar dentro do "for" ele percorre todas as colunas das tabelas 

import plotly.express as px

grafico = px.histogram(tabela, x="MesesComoCliente", color="Churn")
grafico.show()

for coluna in tabela:
  grafico = px.histogram(tabela, x=coluna, color="Churn")
  grafico.show()


