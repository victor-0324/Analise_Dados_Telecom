<img src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/datascience-docu.jpg?raw=true" alt="image" />

## As informações que vão alimentar nossa análise, foram extraídas  do site Kaggle link Os dados são referentes a clientes serviços  de telecomunicações e seus hábitos de consumo, produtos, etc

### Analise de dados, tratamentos de dados grafico em python tabelas(DataFrames)
### Machine learning e pyplot no jupyter notbook

# passo 1: Importa a base de dados
#### Inportando a biblioteca pandas 
- import pandas as pd
#### Lendo os dados e salvando na variavel tabela
- tabela = pd.read_csv("Dados/telecom_users.csv")

# passo 2: Vizualizar a base de dados 
- display(tabela)

				Unnamed: 0	IDCliente	Genero	Aposentado	Casado	Dependentes	MesesComoCliente	ServicoTelefone	MultiplasLinhas	ServicoInternet	ServicoSegurancaOnline	ServicoBackupOnline	ProtecaoEquipamento	ServicoSuporteTecnico	ServicoStreamingTV	ServicoFilmes	TipoContrato	FaturaDigital	FormaPagamento	ValorMensal	TotalGasto	Churn	Codigo
		0	1869	7010-BRBUU	Masculino	0	Sim	Sim	72	Sim	Sim	Nao	SemInternet	SemInternet	SemInternet	SemInternet	SemInternet	SemInternet	2 anos	Nao	CartaoCredito	24.10	1734.65	Nao	NaN
		1	4528	9688-YGXVR	Feminino	0	Nao	Nao	44	Sim	Nao	Fibra	Nao	Sim	Sim	Nao	Sim	Nao	Mensal	Sim	CartaoCredito	88.15	3973.2	Nao	NaN
		2	6344	9286-DOJGF	Feminino	1	Sim	Nao	38	Sim	Sim	Fibra	Nao	Nao	Nao	Nao	Nao	Nao	Mensal	Sim	DebitoAutomatico	74.95	2869.85	Sim	NaN
		3	6739	6994-KERXL	Masculino	0	Nao	Nao	4	Sim	Nao	DSL	Nao	Nao	Nao	Nao	Nao	Sim	Mensal	Sim	BoletoEletronico	55.90	238.5	Nao	NaN
		4	432	2181-UAESM	Masculino	0	Nao	Nao	2	Sim	Nao	DSL	Sim	Nao	Sim	Nao	Nao	Nao	Mensal	Nao	BoletoEletronico	53.45	119.5	Nao	NaN
		...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
		5981	3772	0684-AOSIH	Masculino	0	Sim	Nao	1	Sim	Nao	Fibra	Sim	Nao	Nao	Nao	Sim	Sim	Mensal	Sim	BoletoEletronico	95.00	95	Sim	NaN
		5982	5191	5982-PSMKW	Feminino	0	Sim	Sim	23	Sim	Sim	DSL	Sim	Sim	Sim	Sim	Sim	Sim	2 anos	Sim	CartaoCredito	91.10	2198.3	Nao	NaN
		5983	5226	8044-BGWPI	Masculino	0	Sim	Sim	12	Sim	Nao	Nao	SemInternet	SemInternet	SemInternet	SemInternet	SemInternet	SemInternet	Mensal	Sim	BoletoEletronico	21.15	306.05	Nao	NaN
		5984	5390	7450-NWRTR	Masculino	1	Nao	Nao	12	Sim	Sim	Fibra	Nao	Nao	Sim	Nao	Sim	Sim	Mensal	Sim	BoletoEletronico	99.45	1200.15	Sim	NaN
		5985	860	4795-UXVCJ	Masculino	0	Nao	Nao	26	Sim	Nao	Nao	SemInternet	SemInternet	SemInternet	SemInternet	SemInternet	SemInternet	Anual	Nao	CartaoCredito	19.80	457.3	Nao	NaN
		5986 rows × 23 columns

# passo 3: Coluna unnamed é inutil 
- Dropando a coluna Unannamed 0, (axis=1) exclui todas as linhas da coluna.

- tabela = tabela.drop("Unnamed: 0", axis=1)  
- display(tabela)

  
		IDCliente	Genero	Aposentado	Casado	Dependentes	MesesComoCliente	ServicoTelefone	MultiplasLinhas	ServicoInternet	ServicoSegurancaOnline	ServicoBackupOnline	ProtecaoEquipamento	ServicoSuporteTecnico	ServicoStreamingTV	ServicoFilmes	TipoContrato	FaturaDigital	FormaPagamento	ValorMensal	TotalGasto	Churn	Codigo
		0	7010-BRBUU	Masculino	0	Sim	Sim	72	Sim	Sim	Nao	SemInternet	SemInternet	SemInternet	SemInternet	SemInternet	SemInternet	2 anos	Nao	CartaoCredito	24.10	1734.65	Nao	NaN
		1	9688-YGXVR	Feminino	0	Nao	Nao	44	Sim	Nao	Fibra	Nao	Sim	Sim	Nao	Sim	Nao	Mensal	Sim	CartaoCredito	88.15	3973.2	Nao	NaN
		2	9286-DOJGF	Feminino	1	Sim	Nao	38	Sim	Sim	Fibra	Nao	Nao	Nao	Nao	Nao	Nao	Mensal	Sim	DebitoAutomatico	74.95	2869.85	Sim	NaN
		3	6994-KERXL	Masculino	0	Nao	Nao	4	Sim	Nao	DSL	Nao	Nao	Nao	Nao	Nao	Sim	Mensal	Sim	BoletoEletronico	55.90	238.5	Nao	NaN
		4	2181-UAESM	Masculino	0	Nao	Nao	2	Sim	Nao	DSL	Sim	Nao	Sim	Nao	Nao	Nao	Mensal	Nao	BoletoEletronico	53.45	119.5	Nao	NaN
		...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
		5981	0684-AOSIH	Masculino	0	Sim	Nao	1	Sim	Nao	Fibra	Sim	Nao	Nao	Nao	Sim	Sim	Mensal	Sim	BoletoEletronico	95.00	95	Sim	NaN
		5982	5982-PSMKW	Feminino	0	Sim	Sim	23	Sim	Sim	DSL	Sim	Sim	Sim	Sim	Sim	Sim	2 anos	Sim	CartaoCredito	91.10	2198.3	Nao	NaN
		5983	8044-BGWPI	Masculino	0	Sim	Sim	12	Sim	Nao	Nao	SemInternet	SemInternet	SemInternet	SemInternet	SemInternet	SemInternet	Mensal	Sim	BoletoEletronico	21.15	306.05	Nao	NaN
		5984	7450-NWRTR	Masculino	1	Nao	Nao	12	Sim	Sim	Fibra	Nao	Nao	Sim	Nao	Sim	Sim	Mensal	Sim	BoletoEletronico	99.45	1200.15	Sim	NaN
		5985	4795-UXVCJ	Masculino	0	Nao	Nao	26	Sim	Nao	Nao	SemInternet	SemInternet	SemInternet	SemInternet	SemInternet	SemInternet	Anual	Nao	CartaoCredito	19.80	457.3	Nao	NaN
		5986 rows × 22 columns

#### Ver se tem colunas que eram pra ser numero, e esta sendo reconhecida como texto
- tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
- print(tabela.info())

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
    
#### valor vazio(NaN)
#### Colunas completamentes vazias 
#### Primeiro excluir colunas vazias depois as linhas vazias, seguir sempre essa ordem
- tabela = tabela.dropna(how="all", axis=1)

#### Linhas vazias 
- tabela = tabela.dropna(how="any", axis=0)
- print(tabela.info())

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
#### Contando o total de cancelamento
- display(tabela["Churn"].value_counts())
	Nao    4398
	Sim    1587
	Name: Churn, dtype: int64
#### em percentual
- display(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

	    Nao    4387
	    Sim    1587
	    Name: Churn, dtype: int64
	    Nao    73.4%
	    Sim    26.6%
	    Name: Churn, dtype: object
    
# passo 5:
#### Importando a biblioteca plotly
- import plotly.express as px

#### primeira explicação mostra apenas o grafico de MesesComoCliente
- grafico = px.histogram(tabela, x="MesesComoCliente", color="Churn")
- grafico.show()
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/Meses%20como%20cliente.png?raw=true" />	

#### em apenas um for conseguimos criar todos os gráficos disponíveis Além disso, podemos perceber que os dados que possuem valor da coluna Churn como “YES", são representados em uma cor distinta aos clientes Isso também era esperado visto  a parametrização color=‘ Churn
#### Assim, temos vários outros gráficos que nos permitem analisar de maneira mais profunda o nosso problema Boa parte do problema daqui para a frente é muito mais uma questão de análise de dados do que Python propriamente dita Vamos para os destaques da análise

- for coluna in tabela:
- grafico = px.histogram(tabela, x=coluna, color="Churn")
- grafico.show()
- 
### Genero
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/newplot%20(1).png?raw=true"/>

### Proteção e equipamentos
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/newplot%20(11).png?raw=true"/>

### Serviço suport técnico
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/newplot%20(12).png?raw=true"/>

### Tipos de contratos 
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/newplot%20(14).png?raw=true"/>

### faturas digitais
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/newplot%20(15).png?raw=true"/>

#### Análise
- Os métodos automáticos tem uma taxa de churn menor 
#### Insights
- O Eletronic Check possui resultado muito ruim Se possível evitar Ideia oferecer benefícios caso a pessoa escolha um método automático
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/newplot%20(16).png?raw=true"/>

### Total de gastos
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/newplot%20(18).png?raw=true"/>

### Cancelamentos
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/newplot%20(19).png?raw=true"/>

#### Análise 
- Proporção de Cancelamento Alta para valores de Tenure baixo 
#### Insights 
- Baixa qualidade no atendimento do pós venda 1 ª experiência com o cliente não é boa Captação de clientes falha  clientes desqualificados expectativas erradas ao adquirir o produto
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/newplot%20(5).png?raw=true"/>

#### Análise
- Clientes que NÃO possuem serviços adicionais de Suporte Técnico, Proteção a dispositivos e Segurança Online tendem a cancelar mais
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/newplot%20(8).png?raw=true"/>
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/newplot%20(9).png?raw=true"/>
### Insights
- Todos os itens em algum nível falam sobre aumentar a confiabilidade/disponibilidade do serviço recebido pelo cliente
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/newplot%20(10).png?raw=true"/>


#### Análise
- Contrato Mensal com taxa de cancelamento MUITO superior aos demais métodos de pagamento
#### Insights
- Melhorar as condições comerciais dos planos anuais para direcionar a pessoa para estes casos
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/newplot%20(14).png?raw=true"/> 

# 
-
#

# As informações que vão alimentar o nosso código, serão dados dos investimentos em propaganda em diferentes canais e as vendas decorrentes desses investimentos"
- TV
- Jornal
- Radio

### Introdução Entendendo a base de dados Vendas 
#### Portanto, para um melhor entendimento, na primeira linha temos os 3 meios de comunicação que a Hashtag usa para vender ( Radio, Jornal) e o último item ( representa a quantidade em vendas resultante desses canais Usando a segunda linha como exemplo temos que investindo 230 1 kBRL no Canal TV 37 8 kBRL no Canal Radio 69 2 kBRL no Canal Jornal foi gerada uma Venda de 22 1 MBRL

#### o desafio é conseguir prever as vendas que vamos ter em determinado periodo com  base nos gastos em anúcios nas 3 grandes redes que a empresa investe: tv jornal e radio Ciencias de dados, analise exploratoria, inteligencia artificial, analise de modelos

- import pandas as pd 
- tabela = pd.read_csv("advertising.csv")
- display(tabela)

		TV	Radio	Jornal	Vendas
		0	230.1	37.8	69.2	22.1
		1	44.5	39.3	45.1	10.4
		2	17.2	45.9	69.3	12.0
		3	151.5	41.3	58.5	16.5
		4	180.8	10.8	58.4	17.9
		...	...	...	...	...
		195	38.2	3.7	13.8	7.6
		196	94.2	4.9	8.1	14.0
		197	177.0	9.3	6.4	14.8
		198	283.6	42.0	66.2	25.5
		199	232.1	8.6	8.7	18.4
		200 rows × 4 columns

# Analise exploratoria
#### vamos tentar vizualizar como as informações de cada item estão destribuidas
#### vamos ver a correlação entre cada um dos itens 
#### import seaborn as sns

- import matplotlib.pyplot as plt
- sns.heatmap(tabela.corr(), annot=True, cmap="Wistia")
- plt.show
- sns.pairplot(tabela)
- plt.show

#### Tivemos alguns direcionadores do que pode estar acontecendo, mas não faz muito sentido ficarmos avaliando os pontos 1 a 1 no olho Vamos usar outro método da biblioteca seaborn para conseguirmos avaliar melhor esses dados Este método é o heatmap Aqui, vamos usar alguns argumentos dentro do método Argumentos são essencialmente configurações que o método deverá seguir ao ser executado Vamos entende los um pouco melhor • df corr esse argumento indica o que está sendo plotado Nesse caso, df corr indica que será calculado a CORRELAÇÃO entre os dados do dataframe df que é uma • cmap Wistia ’’-->indica a paleta de cores a ser utilizada no gráfico • annot Escreve dentro dos quadrados o valor
<img height="150" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/informa%C3%A7oes.png?raw=true"/>

#### Achou estranho com apenas 2 linhas gerar o que parecem ser 16 gráficos diferentes? Legal né? Aqui usamos um gráfico de dispersão para cada uma das combinações de colunas possíveis Isso nos permite perceber se existem alguma relação entre elas Alguns casos, serão úteis, outros, não Alguns nem sentido farão Saber diferenciar isso e entender o que está acontecendo é uma peça chave para um bom resultado no fim do processo Lembre se por enquanto estamos em uma ANÁLISE EXPLORATÓRIA! Estamos mais buscando caminhos do que grandes conclusões  Vamos pegar 2 dos 16 gráficos para entende los um pouco melhor
<img height="200" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/Correla%C3%A7%C3%A3o.png?raw=true"/>

# separando em dados de treino e dados de teste

#### Vamos agora para fase de criação de um modelo O que precisamos identificar são • Os inputs do modelo (eixo X) • Os outputs do modelo (eixo Y) Lembrando que nosso objetivo é criar um modelo de previsão de vendas baseado nos dados de investimento nos diferentes canais ( radio, jornais) Ou seja, nossos inputs são valor do investimento nos diferentes canais e nosso output será a venda prevista dado os inputs informados Vamos iniciar este bloco de código informando exatamente isso Usaremos para essa etapa uma nova biblioteca E como sempre, vamos precisar importa las

- from sklearn.model_selection import train_test_split
- y = tabela["Vendas"]
- x = tabela.drop("Vendas", axis=1)
#### Criando as variaveis de treino e de texte 
- x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1) 

# modelo da inteligencia artificiais
#### regressão linear
#### randomforest(arvore de decisão)
- from sklearn.linear_model import LinearRegression
- from sklearn.ensemble import RandomForestRegressor

# cria as inteligencias artificiais
- modelo_regressaolinear = LinearRegression()
- modelo_arvoredecisao = RandomForestRegressor()

# treina as inteligencias artificiais
- modelo_regressaolinear.fit(x_treino, y_treino)
- modelo_arvoredecisao.fit(x_treino, y_treino) 

#### import a biblioteca sklearn
- from sklearn import metrics

# criar as previsões 
- previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
- previsao_arvoredecisao = modelo_arvoresdecisao.predict(x_teste)

# comparar os modelos
- print(metrics.r2_score(y_teste, previsao_regressaolinear))
- print(metrics.r2_score(y_teste, previsao_arvoredecisao))
	0.9071151423684272
	0.9634248429820929
	
# visualização grafica das previsões 
- tabela_auxiliar = pd.DataFrame()
- tabela_auxiliar["y_teste"] =y_teste
- tabela_auxiliar["previsao ArvoresDecisão"] = previsao_arvoredecisao

- tabela_auxiliar["previsao Regressao Linear"] = previsao_regressaolinear
# PLotando o grafico
- plt.figure(figsize=(15,5))
- sns.lineplot(data=tabela_auxiliar)
- plt.show()

#### O gráfico ao lado mostra todos os 60 pontos de teste que são dados reais extraídos da nossa base ao lado das duas curvas geradas pelos nossos modelos A linha azul representa os dados reais de teste A linha tracejada laranja representa os dados de previsão calculados pelo modelo de Random Forest A linha verde tracejada representa os dados de previsão calculados pelo modelo de Regressão Linear Perceba que após a elaboração dos testes, utilizamos novamente o Pandas para criar um dataframe apenas com os resultados calculados e os dados de teste 

- *lembrando que tínhamos 200 pontos e definimos
- 30% para teste, logo 0,3X200 = 60
<img height="200" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/download.png?raw=true"/>

# esse grafico mostra quem é mais importante da base de dados 
- sns.barplot (x=x_treino.columns, y=modelo_arvoresdecisao.feature_importances_)
- plt.show() 

### Lembra que na fase exploratória percebemos que o investimento em TV era o que possuía maior correlação com as vendas? Será que nosso modelo possui a mesma característica? Utilizando novamente nosso pandas e seaborn para auxiliar na elaboração do gráfico, podemos perceber que em termos de importância para o modelo via Random Forest • O investimento em TV é 85 relevante • O Rádio que também avaliamos anteriormente, pouco mais de 10 • Jornal não chegando a mais de 5 de relevância 

<img height="200" src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/Dados_final.png?raw=true"/>

<img src="https://github.com/victor-0324/Analise_Dados_Telecom/blob/main/Graficos%20do%20projeto/Desenvolvimento%20de%20projetos%20de%20DATA%20SCIENCE_large.jpg?raw=true" alt="image" />
