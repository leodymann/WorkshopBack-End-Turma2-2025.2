import math

class FiguraGeo:
    def area_circulo(self, raio):
        return math.pi * math.pow(raio,2)

    def area_triangulo(self, base, altura):
        return (base * altura) / 2

    def calc_hipotenusa(self, cateto1, cateto2):
        return math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))

def calcular_area_circulo(fig, raio):
    return fig.area_circulo(raio)
def calcular_area_triangulo(fig, base, altura):
    return fig.area_triangulo(base, altura)
def calcular_hipotenusa(fig, c1, c2):
    return fig.calc_hipotenusa(c1, c2)

def menu(opcao, fig, valores):
    print("opcao 1 = circulo, 2 = triangulo, 3 = hipotenusa")

    if opcao == 1:
        return calcular_area_circulo(fig, valores[0])
    elif opcao == 2:
        return calcular_area_triangulo(fig, valores[0], valores[1])
    elif opcao == 3:
        return calcular_hipotenusa(fig, valores[0], valores[1])
    elif opcao == 0:
        return none
    else:
        return "opcao invalida"

def main():
    fig = FiguraGeo()

    while True:
        print("\n escolha a opção:")
        print("1 - area do circulo")
        print("2 - area do triangulo")
        print("3 - hipotenusa")
        print("0 - sair")

        try:
            opcao = int(input("digite a opcao: "))
        except ValueError:
            print("opcao invalida.")
            continue
        
        if opcao == 1:
            raio = float(input("digite o raio do circulo: "))
            result = menu(opcao, fig, (raio,))
            print(f"area do circulo: {result:.2f}")
        elif opcao == 2:
            base = float(input("digite a base do triangulo"))
            altura = float(input("digite a altura do triangulo"))
            result = menu(opcao, fig, (base, altura))
            print(f"area do triangulo: {result:.2f}")
        elif opcao == 3:
            c1 = float(input("digite o primeiro cateto: "))
            c2 = float(input("digite o segundo cateto: "))
            result = menu(opcao, fig, (c1, c2))
            print(f"hipotenusa: {result:.2f}")
        elif opcao == 0:
            print("encerrando.")
            break
        else:
            print("opcao invalida")
main()