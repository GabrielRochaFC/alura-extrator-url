url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
print(url)

# Separando url
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]

# Pegando inicio dos parametros
print(url_parametros)
parametro_buscado = 'quantidade'
inicio_parametro = url_parametros.find(parametro_buscado)
indice_inicial_valor = inicio_parametro + 1 + len(parametro_buscado)

# Pegando onde fica o final do valor
indice_e_comercial = url_parametros.find('&', indice_inicial_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_inicial_valor:]
else:
    valor = url_parametros[indice_inicial_valor:indice_e_comercial]
print( indice_inicial_valor, indice_e_comercial)
print(valor)
