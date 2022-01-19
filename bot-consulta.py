from webbot import Browser
import time
import pandas as pd
from atuacoes import atuacoes
from multas import multas
from situacoes import situacoes

# Variaveis Globais
Cidade_A = ''
Cidade_M = ''


####################################################### MAIN ##########################################################################

# Importo excel com todos os dados
pl = pd.read_excel(
    r'/home/pedrogoulart/BOTS/bot-consulta/Vespasiano-2366.xlsx')
planilha = pl.copy()  # Faço uma cópia

# Ativo o navegador e entro no site do detran
web = Browser()
web.go_to('https://www.detran.mg.gov.br/veiculos/situacao-do-veiculo/consultar-situacao-do-veiculo')

i = 0
parar = False  # Variavel de Parada do while


while(parar == False):

    # Inserir placa de chassi
    time.sleep(2)
    web.type(planilha['Placa'][i], into='text', id='placa')
    time.sleep(2)
    web.type(planilha['Chassi'][i], into='text', id='chassi')

    #                                                    #
    #                                                    #
    # Confirmando o reCapthca e clicamos em pesquisar    #
    #                                                    #
    #                                                    #

    continua = input("Puxar os dados do veículo S/n: ")

    if continua == 's' or continua == 'S':

        # atualizamos a situação na nossa copia da tabela
        situacao = situacoes(web)
        planilha.loc[i, 'Situação'] = situacao

        # Olha situação mais simples = SEM CADASTRO E SEM MULTAS OU AUTUAÇÃO
        if situacao == 'Este Veículo não tem Autuação e não tem Multas.' or situacao == 'Veículo não Cadastrado na Base de Minas Gerais':

            # NAO TEM O QUE FAZER
            web.click('Consultar Outro Veículo', tag='a',
                      classname='text-secondary')
            i += 1
            continue

        elif situacao.find('Este Veículo não tem Autuação') != -1:

            if situacao.find('não tem Multas') != -1:
                print('Caso impossivel')  # pois ja foi contemplado acima
            else:
                multa, Cidade_M = multas(web)
                planilha.loc[i, 'Multa'] = multa
                planilha.loc[i, 'Cidade_M'] = Cidade_M
                Cidade_M = ''
        else:

            # VEICULO COM ATUAÇÃO E SEM MULTA
            if situacao.find('não tem Multas') != -1:
                atuacao, Cidade_A = atuacoes(web)
                planilha.loc[i, 'Atuação'] = atuacao
                planilha.loc[i, 'Cidade_A'] = Cidade_A
                Cidade_A = ''

            # VEICULO COM ATUAÇÃO E COM MULTA
            else:
                atuacao, Cidade_A = atuacoes(web)
                planilha.loc[i, 'Atuação'] = atuacao
                planilha.loc[i, 'Cidade_A'] = Cidade_A
                Cidade_A = ''
                multa, Cidade_M = multas(web)
                planilha.loc[i, 'Multa'] = multa
                planilha.loc[i, 'Cidade_M'] = Cidade_M
                Cidade_M = ''

        web.click('Consultar Outro Veículo', tag='a',
                  classname='text-secondary')
        i += 1
        continue

    elif continua == 'n' or continua == 'N':

        df = pd.DataFrame(planilha, columns=[
            'Lote', 'Chassi', 'Placa', 'Ano', 'Situação', 'Multa', 'Cidade_M', 'Atuação', 'Cidade_A'])

        df.to_excel(r'/home/pedrogoulart/Downloads/2166.xlsx',
                    index=False, header=True)

        web.click('Consultar Outro Veículo', tag='a',
                  classname='text-secondary')

        # Fechar Guia
        web.close_current_tab()

        parar = True  # Parar while
