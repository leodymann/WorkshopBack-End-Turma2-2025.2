import math

def arredondamento(num: float):
    piso = math.floor(num)
    teto = math.ceil(num)
    mais_prox = round(num)
    return piso, teto, mais_prox

numero = float(input("escreva um numero: "))
piso, teto, mais_prox = arredondamento(numero)
print(f"valor original: {numero}")
print(f"valor do piso {piso}") #arredonda para baixo
print(f"valor do teto {teto}") #arredonda para cima
print(f"valor arredondado para o mais proximo: {mais_prox}") #arredonda para o mais proximo