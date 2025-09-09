from django.shortcuts import render
from .models import Endereco
import requests
def home(request):
    return render(request, 'home.html')

def consulta_cep(request):
    cep = request.GET.get('cep')  # pega o valor do GET

    if cep:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if response.status_code == 200:
            data = response.json()
            endereco = Endereco(
                cep=data.get('cep'),
                rua=data.get('logradouro'),
                bairro=data.get('bairro'),
                cidade=data.get('localidade'),
                estado=data.get('uf')
            )
            endereco.save()
            return render(request, 'consulta_cep.html', {'endereco': endereco, 'cep': cep})
        else:
            return render(request, 'consulta_cep.html', {'erro': 'Não foi possível consultar o CEP.'})

    return render(request, 'consulta_cep.html', {'mensagem': 'Nenhum CEP foi enviado.'})
