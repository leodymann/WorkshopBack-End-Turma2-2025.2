from django.db import models

# Create your models here.
class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return f"rua: {self.rua}, bairro: {self.bairro}, cidade: {self.cidade}, estado: {self.estado} e cep: {self.cep}"


objetos = models.Manager()