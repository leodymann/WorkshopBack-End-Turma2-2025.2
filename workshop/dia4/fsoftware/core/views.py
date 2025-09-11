from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Endereco
from .form import ConsultaCepForm
import requests

def home(request):
    return render(request, 'home.html')

class ConsultaCepView(FormView):
    template_name = "consulta_cep.html"
    form_class = ConsultaCepForm
    success_url = reverse_lazy("endereco_list")

    def form_valid(self, form):
        cep = form.cleaned_data['cep']
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

        if response.status_code == 200:
            data = response.json()
            Endereco.objects.create(
                cep=data.get("cep", ""),
                rua=data.get("logradouro", ""),
                bairro=data.get("bairro", ""),
                cidade=data.get("localidade", ""),
                estado=data.get("uf", "")
            )
        return super().form_valid(form)
    

class EnderecoListView(ListView):
    model = Endereco
    template_name = "endereco_list.html"
    context_object_name = "enderecos"
class EnderecoDetailsView(DetailView):
    model = Endereco
    template_name = "endereco_detail.html"
    context_object_name = "endereco"
class EnderecoDeleteView(DeleteView):
    model = Endereco
    template_name = "endereco_delete.html"
    success_url = reverse_lazy("endereco_list")