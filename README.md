# Analise_Dados_Telecom
- A nalisando banco de dados de uma telecom, com pandas, machine learning e pyplot no jupyter notbook
- Analise de dados, tratamentos de dados grafico em python tabelas(DataFrames)

# passo 1: Importa a base de dados

  ### import pandas as pd
- Salvando os dados na variavel tabela
  ### tabela = pd.read_csv("Dados/telecom_users.csv")

# passo 2: Vizualizar a base de dados 
  ### display(tabela)

	Unnamed: 0	IDCliente	Genero	Aposentado	Casado	Dependentes	MesesComoCliente	ServicoTelefone	MultiplasLinhas	ServicoInternet	ServicoSegurancaOnline	ServicoBackupOnline	ProtecaoEquipamento	ServicoSuporteTecnico	ServicoStreamingTV	ServicoFilmes	TipoContrato	FaturaDigital	FormaPagamento	ValorMensal	TotalGasto	Churn	Codigo
- 5986 rows × 23 columns

# passo 3: Coluna unnamed é inutil 
- Dropando a coluna Unannamed 0, (axis=1) exclui todas as linhas da coluna.

### tabela = tabela.drop("Unnamed: 0", axis=1)  
### display(tabela)
       IDCliente	Genero	Aposentado	Casado	Dependentes	MesesComoCliente	ServicoTelefone	MultiplasLinhas	ServicoInternet	ServicoSegurancaOnline	ServicoBackupOnline	ProtecaoEquipamento	ServicoSuporteTecnico	ServicoStreamingTV	ServicoFilmes	TipoContrato	FaturaDigital	FormaPagamento	ValorMensal	TotalGasto	Churn	Codigo  
- 5986 rows × 22 columns

- Ver se tem colunas que eram pra ser numero, e esta sendo reconhecida como texto
### tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

### print(tabela.info())


    RangeIndex: 5986 entries, 0 to 5985
    Data columns (total 22 columns):
     #   Column                  Non-Null Count  Dtype  
    ---  ------                  --------------  -----  
     0   IDCliente               5986 non-null   object 
     1   Genero                  5986 non-null   object 
     2   Aposentado              5986 non-null   int64  
     3   Casado                  5986 non-null   object 
     4   Dependentes             5985 non-null   object 
     5   MesesComoCliente        5986 non-null   int64  
     6   ServicoTelefone         5986 non-null   object 
     7   MultiplasLinhas         5986 non-null   object 
     8   ServicoInternet         5986 non-null   object 
     9   ServicoSegurancaOnline  5986 non-null   object 
     10  ServicoBackupOnline     5986 non-null   object 
     11  ProtecaoEquipamento     5986 non-null   object 
     12  ServicoSuporteTecnico   5986 non-null   object 
     13  ServicoStreamingTV      5986 non-null   object 
     14  ServicoFilmes           5986 non-null   object 
     15  TipoContrato            5986 non-null   object 
     16  FaturaDigital           5986 non-null   object 
     17  FormaPagamento          5986 non-null   object 
     18  ValorMensal             5986 non-null   float64
     19  TotalGasto              5976 non-null   float64
     20  Churn                   5985 non-null   object 
     21  Codigo                  0 non-null      float64
    dtypes: float64(3), int64(2), object(17)
    memory usage: 1.0+ MB
    None
    
- valor vazio(NaN)
- Colunas completamentes vazias 
- Primeiro excluir colunas vazias depois as linhas vazias, seguir sempre essa ordem
### tabela = tabela.dropna(how="all", axis=1)

- Linhas vazias 
### tabela = tabela.dropna(how="any", axis=0)
### print(tabela.info())

    Int64Index: 5974 entries, 0 to 5985
    Data columns (total 21 columns):
     #   Column                  Non-Null Count  Dtype  
    ---  ------                  --------------  -----  
     0   IDCliente               5974 non-null   object 
     1   Genero                  5974 non-null   object 
     2   Aposentado              5974 non-null   int64  
     3   Casado                  5974 non-null   object 
     4   Dependentes             5974 non-null   object 
     5   MesesComoCliente        5974 non-null   int64  
     6   ServicoTelefone         5974 non-null   object 
     7   MultiplasLinhas         5974 non-null   object 
     8   ServicoInternet         5974 non-null   object 
     9   ServicoSegurancaOnline  5974 non-null   object 
     10  ServicoBackupOnline     5974 non-null   object 
     11  ProtecaoEquipamento     5974 non-null   object 
     12  ServicoSuporteTecnico   5974 non-null   object 
     13  ServicoStreamingTV      5974 non-null   object 
     14  ServicoFilmes           5974 non-null   object 
     15  TipoContrato            5974 non-null   object 
     16  FaturaDigital           5974 non-null   object 
     17  FormaPagamento          5974 non-null   object 
     18  ValorMensal             5974 non-null   float64
     19  TotalGasto              5974 non-null   float64
     20  Churn                   5974 non-null   object 
    dtypes: float64(2), int64(2), object(17)
    memory usage: 1.0+ MB
    None
    
# passo 4: como esta os nossos cancelamentos
### display(tabela["Churn"].value_counts())
- em percentual
### display(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

    Nao    4387
    Sim    1587
    Name: Churn, dtype: int64
    Nao    73.4%
    Sim    26.6%
    Name: Churn, dtype: object
    
# passo 5:
### import plotly.express as px

- primeira explicação mostra apenas o grafico de MesesComoCliente
### grafico = px.histogram(tabela, x="MesesComoCliente", color="Churn")
### grafico.show()



- No segundo mostra o grafico de todas as tabelas 
- ao colocar dentro do "for" ele percorre todas as colunas das tabelas
### for coluna in tabela:
  ### grafico = px.histogram(tabela, x=coluna, color="Churn")
  ### grafico.show()
  
