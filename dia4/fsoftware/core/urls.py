from django.urls import path
from .views import ConsultaCepView, EnderecoListView, EnderecoDetailsView, EnderecoDeleteView
urlpatterns = [
    path('', ConsultaCepView.as_view(), name="consulta_cep"),
    path('enderecos/', EnderecoListView.as_view(), name="endereco_list"),
    path('enderecos/<int:pk>/', EnderecoDetailsView.as_view(), name="endereco_detail"),
    path('enderecos/<int:pk>/excluir/', EnderecoDeleteView.as_view(), name="endereco_delete"),
]