import math

def calcular_raiz(num:float):
    if num < 0:
        return "numero negativo, nao é possivel calcular a raiz."
    else:
        raiz = math.sqrt(num)
        return f"a raiz quadrada de {num} é {raiz}"

def verifica_loop(opcao:str):
    if opcao != '1':
        return "encerrado."
    return "continuar"

while True:
    numero = float(input("digite um valor para calcular a raiz: "))
    result = calcular_raiz(numero)
    print(result)

    opcao = input("quer continuar? sim-1 nao-2: ")
    status = verifica_loop(opcao)
    print(status)

    if status == "encerrado.":
        break