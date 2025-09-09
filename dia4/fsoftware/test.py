import requests
cep = "58356000"

def buscar_cep(cep):
    url = f'http://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        dados_do_cep = response.json()
        return dados_do_cep
    else:
        return None
    
print(buscar_cep(cep))
    