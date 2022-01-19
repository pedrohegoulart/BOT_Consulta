
def cidades(web):
    cidade_f = ''
    cidade_f += web.find_elements(tag='dd',
                                  classname='col-md-8')[8].text + ' '
    print(cidade_f)
    return cidade_f
