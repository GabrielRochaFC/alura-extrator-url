class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.parametro_buscado = ''
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def __str__(self):
        return self.url

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')

    @property
    def url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = url[0:indice_interrogacao]
        return url_base

    @property
    def url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = url[indice_interrogacao + 1:]
        return url_parametros

    @property
    def valor_parametro(self):
        inicio_parametro = self.url_parametros.find(self.parametro_buscado)
        indice_inicial_valor = inicio_parametro + 1 + len(self.parametro_buscado)
        indice_e_comercial = self.url_parametros.find('&', indice_inicial_valor)
        if indice_e_comercial == -1:
            valor = self.url_parametros[indice_inicial_valor:]
        else:
            valor = self.url_parametros[indice_inicial_valor:indice_e_comercial]
        return valor

    @property
    def parametro_buscado(self):
        return self._parametro_buscado

    @parametro_buscado.setter
    def parametro_buscado(self, parametro_buscado):
        self._parametro_buscado = parametro_buscado


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url.parametro_buscado = 'quantidade'
valor_quantidade = extrator_url.valor_parametro
print(valor_quantidade)
