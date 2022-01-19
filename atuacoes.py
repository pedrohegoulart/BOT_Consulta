from cidades import cidades


def atuacoes(web):

    # Variaveis Locais
    h = 0
    atuacao = ''
    cidade = ''
    orgao = ''
    contador = 0

    web.click('Autuação', tag='h5')  # Clicar em +Autuacao

    # Conta quantos dados atuações <TD> temos
    td = web.find_elements(tag='td').copy()
    # print(td[0].text)
    contador = len(td)
    # print(contador)
    contador = len(web.find_elements(tag='td'))
    # print(contador)

    for j in range(1, contador, 2):
        print('j ==>')
        print(j)
        # Pego o nome do orgao
        # Tem que ser H pois esse find é diferente
        orgao = web.find_elements(tag='a', classname='text-danger')[h].text
        print(orgao)
        # Entro na Atuação do orgao
        web.click(orgao, tag='a', classname='text-danger')

        # Pego a cidade
        cidade = cidades(web)

        # Caso a outras Atuação do mesmo orgao
        while(web.exists(tag='a', text='Próxima Atuação >>') == True):

            # ir na proxima Atuação
            web.click('Próxima Atuação >>', tag='a', classname='btn-primary')

            # E pegar a nova cidade
            cidade = cidades(web)
            print('Entrou')

        # Volto para a pagina geral
        web.click('Retornar à Dados do Veículo',
                  tag='a', classname='text-secondary')

        # Clicar em +Atuação para abrir de novo
        web.click('Autuação', tag='h5')

        # coloco os resultados na variavel Atuação
        atuacao += '  ' + orgao

        atuacao += '(' + web.find_elements(tag='td')[j-1].text + ')'
        h += 1
    print(atuacao)

    # Clicar em atuação para fechar
    web.click('Autuação', tag='h5')

    return (atuacao, cidade)
