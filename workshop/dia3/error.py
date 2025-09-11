#print("Olá, mundo!"
print("Olá, mundo!")
#SyntaxError: '(' was never closed
#Aconteceu pois não houve o fechamento do parentese

#print(nome)
nome = "leo"
print(nome)
#NameError: name 'nome' is not defined. Did you mean: 'None'?
#Ocorreu pois não foi definido o valor de "nome"

#def somar(a, b):
#    return a + b
#resultado = somar(10, "5")
#print(resultado)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#Ocorreu pois houve uma tentativa de somar um número inteiro com uma string
#def somar(a, b) -> :
    #return a + b
#resultado = somar(10, "5")
#print(resultado)

def somar(a, b) -> float:
    try:
        return float(a) + float(b)
    except TypeError as e:
        raise ValueError(f"error: {e} str não compativel com soma a inteiro")

def somar_ex() -> float:
    result = somar(10, "5")
    print(f"execução - resultado da soma {result}")
    return result

somar_ex()

# error unsupported operand type(s) for +: 'int' and 'str'
# nao da para somar int + str, capturo o erro e faço a conversão em float para continuar a chamada 10, "5"

#def dividir(a, b):
    #return a / b

#num1 = input("Digite o primeiro número: ")
#num2 = input("Digite o segundo número: ")

#resultado = dividir(int(num1), int(num2))
#print(f"Resultado: {resultado}")

def dividir(a, b):
    return a / b

while True:
    try:
        n1 = input("digite um numero: ")
        n2 = input("digite outro numero: ")
        
        result = dividir(int(n1), int(n2))
        print(f"result: {result}")
        break
    except ValueError:
        print(f"apresente numeros validos(1,2,3...10).")
    except ZeroDivisionError:
        print(f"nao é possivel dividir por 0")
    except TypeError:
        print(f"tipagem invalida")
        break
# possiveis erros:
# valueerror - usuário apresenta números inválidos(textos em vez de núemros)
# zerodivisionerror - não é possivel dividir por zero
# typerror - tipagem inserida não esperada
# a solução foi converte para inteiro, fazer a captura do erro e fazer com que o usuário insira
# valores corretos.

#dados = {
    #"nome": "Isaac ",
    #"idade": 25,
    #"cidade": "São Paulo"
#}

#chave = input("Digite a chave que deseja acessar: ")

#print(f"O valor da chave '{chave}' é: {dados[chave]}")

dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}
print("chaves a serem acessadas: [nome], [idade], [cidade]")
chave = input("digite a chave que deseja acessar: ")

try:
    print(f"o valor da chave é: {dados[chave]}")
except KeyError:
    valor = dados.get(chave, f"a chave '{chave}' não existe, use alguma destas: {list(dados.keys())}")
    print(valor)

# Quando o usuário acessar uma chave inexistente vai gerar um key error
# tratei usando um except key e usando o metodo get evita o erro e retorna as chaves válidas.