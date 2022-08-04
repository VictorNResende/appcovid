import pandas as pd
import plotly.express as px
import streamlit as st 

#streamlit run codigoBase.py

#LENDO O DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#MELHORANDO O NOME DAS COLUNAS DA TABELA
df = df.rename(columns={'newDeaths': 'Novos óbitos','newCases': 'Novos casos','deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes','totalCases_per_100k_inhabitants':'Casos por 100 mil habitantes'})

#SELECÃO DO ESTADO
estados = list(df['state'].unique())
state = st.slidebar.selectbox('Qual estado?', estados)

#SELEÇÃO DA COLUNA
#column ='Casos por 100 mil habitantes'
colunas = ['Novos óbitos','Novos casos','Óbitos por 100 mil habitantes','Casos por 100 mil habitantes']
column = st.slidebar.import pandas as pd
import plotly.express as px
import streamlit as st 

#streamlit run codigoBase.py

#LENDO O DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#MELHORANDO O NOME DAS COLUNAS DA TABELA
df = df.rename(columns={'newDeaths': 'Novos óbitos','newCases': 'Novos casos','deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes','totalCases_per_100k_inhabitants':'Casos por 100 mil habitantes'})

#SELECÃO DO ESTADO
estados = list(df['state'].unique())
state = st.slidebar.import pandas as pd
import plotly.express as px
import streamlit as st 

#streamlit run codigoBase.py

#LENDO O DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#MELHORANDO O NOME DAS COLUNAS DA TABELA
df = df.rename(columns={'newDeaths': 'Novos óbitos','newCases': 'Novos casos','deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes','totalCases_per_100k_inhabitants':'Casos por 100 mil habitantes'})

st.image("https://img2.gratispng.com/20180604/xlh/kisspng-becton-dickinson-philippines-inc-bd-associates-s-bd-logo-5b14dcc01514f7.3845814815280938880864.jpg")

#SELECÃO DO ESTADO
estados = list(df['state'].unique())
state = st.slidebar.multiselect('Qual estado?', estados)

#SELEÇÃO DA COLUNA
#column ='Casos por 100 mil habitantes'
colunas = ['Novos óbitos','Novos casos','Óbitos por 100 mil habitantes','Casos por 100 mil habitantes']
column = st.slidebar.selectbox('Qual tipo de informação?', colunas)

#SELEÇÃO DAS LINHAS QUE PERTECEM AO ESTADO 
df = df[df['state'] == state]

fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.')

st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')('Qual estado?', estados)

#SELEÇÃO DA COLUNA
#column ='Casos por 100 mil habitantes'
colunas = ['Novos óbitos','Novos casos','Óbitos por 100 mil habitantes','Casos por 100 mil habitantes']
column = st.slidebar.selectbox('Qual tipo de informação?', colunas)

#SELEÇÃO DAS LINHAS QUE PERTECEM AO ESTADO 
df = df[df['state'] == state]

fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.')

st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')('Qual tipo de informação?', colunas)

#SELEÇÃO DAS LINHAS QUE PERTECEM AO ESTADO 
df = df[df['state'] == state]

fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a mostragem.')

st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
