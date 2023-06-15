import streamlit as st
import pandas as pd
import numpy as np
from pandas import read_csv


#Título da página
st.title('Dashboard')
st.markdown('''## Análise de dados das vacinas da Covid 19''')


#Mostra a tabela inteira
tabela = read_csv("vaccination-data.csv")   #Lê a tabela
st.write(tabela)    #Mostra a tabela



# Menu
with st.sidebar:    #Mostra as opções disponíveis para o usuário
    opcao = st.radio(
        "Menu de seleção",
        ("Selecionar opção", "Visualizar tabela em ordem crescente", "Visualizar tabela em ordem decrescente")
    )

#Se o usuário escolher a opção 'Visualizar tabela em ordem crescente' acontece isso:
if opcao == "Visualizar tabela em ordem crescente":
    tabela_produtos = tabela.groupby('COUNTRY').sum()  #Agrupa a tabela que eu quiser
    tabela_produtos = tabela_produtos[["DATE_UPDATED"]].sort_values(by="DATE_UPDATED", ascending=True)  #Agrupa em ordem crescente
    st.write(tabela_produtos)   #Mostra a tabela

    tabela_produtos = tabela.groupby('COUNTRY').sum()  #Agrupa a tabela que eu quiser
    tabela_produtos = tabela_produtos[["NUMBER_VACCINES_TYPES_USED"]].sort_values(by="NUMBER_VACCINES_TYPES_USED", ascending=True)  #Agrupa em ordem crescente
    st.write(tabela_produtos)   #Mostra a tabela


#Se o usuário escolher a opção 'Visualizar tabela em ordem decrescente' acontece isso
elif opcao == "Visualizar tabela em ordem decrescente":
    tabela_produtos = tabela.groupby('COUNTRY').sum()  #Agrupa a tabela que eu quiser
    tabela_produtos = tabela_produtos[["DATE_UPDATED"]].sort_values(by="DATE_UPDATED", ascending=False) #Agrupa em ordem decrescente
    st.write(tabela_produtos)   #Mostra a tabela

    tabela_produtos = tabela.groupby('COUNTRY').sum()  #Agrupa a tabela que eu quiser
    tabela_produtos = tabela_produtos[["NUMBER_VACCINES_TYPES_USED"]].sort_values(by="NUMBER_VACCINES_TYPES_USED", ascending=False) #Agrupa em ordem decrescente
    st.write(tabela_produtos)   #Mostra a tabela

