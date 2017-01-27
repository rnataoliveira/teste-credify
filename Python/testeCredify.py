from bs4 import BeautifulSoup
import requests

payload = {'tipo':'pf',
           'authenticity_token':'bQMgJ+4BJxpKGLw3Xcpc29zc8zCZBbaXottyqcX94xk=',
           'nome':'JOSE MARCOS DA SILVA',
           'flag_pesquisa':'value1',
           'commit':'Pesquisar'
}

r = requests.post('http://atualiza.cfa.org.br/pesquisa', data=payload)

soup = BeautifulSoup(r.text, "lxml")

nome = soup.select("table tr")[1].select("td")[0].text
numero_registro = soup.select("table tr")[1].select("td")[1].text
cra = soup.select("table tr")[1].select("td")[2].text
tipo_registro = soup.select("table tr")[3].select("td")[0].text
titulacao = soup.select("table tr")[3].select("td")[1].text
formacao_academica = soup.select("table tr")[3].select("td")[2].text

retorno = {
    "Nome" : nome,
    "Número de registro" : numero_registro,
    "CRA" : cra,
    "Tipo de Registro" : tipo_registro,
    "Titulação" : titulacao,
    "Formação Acadêmica" : formacao_academica
}

print(retorno)