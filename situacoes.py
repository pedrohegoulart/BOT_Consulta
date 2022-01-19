
def situacoes(web):
    # Puxamos a situação geral do veículo
    contador = len(web.find_elements(tag='div', classname='alert'))

    if (contador != 0):
        i = contador - 1

    situacao = web.find_elements(tag='div', classname='alert')[i].text
    return situacao
