class animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Nome: {self.nome}, Idade: {self.idade} anos"

    def falar(self):
        return "O animal faz algum som"

class gato(animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def falar(self):
        return "Miau"
class cachorro(animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def falar(self):
        return "AuAu"

def main():
    animais = [gato("Fantasmatico", 1), cachorro("Cesar", 3)]

    for animal in animais:
        print(animal.apresentar())
        print(animal.falar())

if __name__ == "__main__":
    main()