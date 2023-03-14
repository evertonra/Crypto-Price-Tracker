from pickle import FRAME
from tkinter import *
from tkinter import ttk


### Importando bibliotecas ###
import requests
import json


### Cores ###
co0 = "#444466"  # Preto
co1 = "#feffff"  # Branco
co2 = "#222222"  # Azul
fundo = "#030303"
# fundo = "#484f60"

### Criando a janela ###
janela = Tk()
janela.title('Criptos Price Tracker')
janela.geometry('450x250')
janela.configure(bg=fundo)

### Dividindo a janela em 2 frames ###
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_cima = Frame(janela, width=450, height=50, bg=co1,
                   pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=450, height=200, bg=fundo,
                    pady=0, padx=0, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NW)

### Função para obter os dados ###


def info():
    ### API ###
    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=BRL'
    api_eth_link = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BRL'
    api_ltc_link = 'https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=BRL'

    ### HTTP Requests ###
    response = requests.get(api_link)
    response_eth = requests.get(api_eth_link)
    response_ltc = requests.get(api_ltc_link)

    ### Convertendo os dados para dicionário ###
    dados = response.json()
    dados_eth = response_eth.json()
    dados_ltc = response_ltc.json()

    ### Valor do BTC em BRL ###
    valor_brl = float(dados['BRL'])
    valor_formatado_brl = "R$ {:,.3f}".format(valor_brl)
    l_pbtc_reais['text'] = '1 BTC =' + \
        ' ' + valor_formatado_brl

    ### Valor do ETH em BRL ###
    valor_brl_eth = float(dados_eth['BRL'])
    valor_formatado_brl_eth = "R$ {:,.3f}".format(valor_brl_eth)
    l_peth_reais['text'] = '1 ETH =' + \
        ' ' + valor_formatado_brl_eth

    ### Valor do LTC em BRL ###
    valor_brl_ltc = float(dados_ltc['BRL'])
    valor_formatado_brl_ltc = "R$ {:,.3f}".format(valor_brl_ltc)
    l_pltc_reais['text'] = '1 LTC =' + \
        ' ' + valor_formatado_brl_ltc

    ### Refresh dos valores ###
    frame_baixo.after(5000, info)


### Configurando o frame de cima ###
l_nome = Label(frame_cima, text='     Criptos Price Tracker', bg=co1, fg=co2,
               relief=FLAT, anchor='center', font=('Roboto 24 bold'))
l_nome.place(x=10, y=6)

### Configurando o frame de baixo ###
l_pbtc_reais = Label(frame_baixo, text='', bg=fundo, fg=co1,
                     relief=FLAT, anchor='center', font=('Roboto 12 bold'))
l_pbtc_reais.place(x=70, y=30)

l_peth_reais = Label(frame_baixo, text='', bg=fundo, fg=co1,
                     relief=FLAT, anchor='center', font=('Roboto 12 bold'))
l_peth_reais.place(x=70, y=80)

l_pltc_reais = Label(frame_baixo, text='', bg=fundo, fg=co1,
                     relief=FLAT, anchor='center', font=('Roboto 12 bold'))
l_pltc_reais.place(x=70, y=130)


info()

janela.mainloop()
