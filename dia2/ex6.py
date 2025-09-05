import math

class animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        #funcao para retornar dados de um animal(apresentar ele)
        return f"{self.nome} - {self.idade}"
    def falar(self):
        #funcao para retornar o som do animal selecionado
        return "algum som"

class gato(animal):
    #crio a classe gato e variaveis
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def falar(self):
        return "Miau"

class cachorro(animal):
    #crio a classe cachorro e variaveis
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def falar(self):
        return "Auau"

class zoo:
    #classe zoo para add e listar animais
    def __init__(self):
        self.animais = []
    
    def add_animal(self, animal):
        self.animais.append(animal)
    
    def list_animal(self):
        list = []
        for animal in self.animais:
            info = f"{animal.apresentar()} som {animal.falar()}"
            list.append(info)
        return list
    def filtrar_tipo(self, tipo):
        list = []
        for animal in self.animais:
            if isinstance(animal, tipo):
                info = f"{animal.apresentar()} - {animal.falar()}"
                list.append(info)
        return list

def main():
    zoo_instance = zoo()

    #crio animais
    gato1 = gato("lusca", 2)
    gato2 = gato("fantasmatico", 3)
    cachorro1 = cachorro("dogao", 1)
    cachorro2 = cachorro("patinha", 2)

    #add animais
    zoo_instance.add_animal(gato1)
    zoo_instance.add_animal(gato2)
    zoo_instance.add_animal(cachorro1)
    zoo_instance.add_animal(cachorro2)

    # listagem
    print("Todos os animais")
    for info in zoo_instance.list_animal():
        print(info)
    print("\nSomente cachorros")
    for info in zoo_instance.filtrar_tipo(cachorro):
        print(info)
    print("\nSomente gatos")
    for info in zoo_instance.filtrar_tipo(gato):
        print(info)

if __name__ == "__main__":
    main()
