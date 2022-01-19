from cidades import cidades


def multas(web):

    # Variaveis Locais
    h = 0
    multa = ''
    cidade = ''
    orgao = ''
    contador = 0

    # Caso sem Atuação  e com multa
    web.click('Multa', tag='h5')  # Clicar em +Multas

    # Puxar dados
    # Conta quantos dados multas <TD> temos
    td = web.find_elements(tag='td').copy()
    # print(td[0].text)
    contador = len(td)
    print(contador)

    for j in range(1, contador, 3):
        print('j ==> ')
        print(j)
        # Pego o nome do orgao
        # Tem que ser H pois esse find é diferente
        orgao = web.find_elements(tag='a', classname='text-danger')[h].text
        print(orgao)
        # Entro na multa do orgao
        web.click(orgao, tag='a', classname='text-danger')

        # Pego a cidade
        cidade = cidades(web)

        # Caso a outras multas do mesmo orgao
        while(web.exists(tag='a', text='Próxima Multa >>') == True):

            # ir na proxima multa
            web.click('Próxima Multa >>', tag='a', classname='btn-primary')
            print('Entro loop multa')
            # E pegar a nova cidade
            cidade = cidades(web)

        # Volto para a pagina geral
        web.click('Retornar à Dados do Veículo',
                  tag='a', classname='text-secondary')

        # Clicar em +Multas para abrir de novo
        web.click('Multa', tag='h5')

        # coloco os resultados na variavel multa
        multa += '  ' + orgao
        multa += '(' + web.find_elements(tag='td')[j].text + ')'
        h += 1

    print(multa)

    # Para fechar
    web.click('Multa', tag='h5')

    return (multa, cidade)
