class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False, falando=False, dormindo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.dormir = dormindo

    def apresentar(self):
        print(f'Olá sou {self.nome} tenho {self.peso} KG e tenho {self.idade} anos.')

    def comer(self):
        if self.comendo == True:
            print(f'{self.nome} Não pode comer pois já está comendo')
        elif self.dormindo == True:
            print(f'{self.nome} não pode comer pois está dormindo')
        elif self.falando == True:
            print(f'{self.nome} não pode comer pois está falando')
        else:
            print(f'{self.nome} começou a comer')
            self.comendo = True

    def parar_comer(self):
        if self.comendo == True:
            print(f'{self.nome} parou de comer')
            self.comendo = False
        else:
            print(f'{self.nome} não está comendo')

    def falar(self):
        if self.comendo == True:
            print(f'{self.nome} Não pode falar pois está comendo')
        elif self.dormindo == True:
            print(f'{self.nome} não pode falar pois está dormindo')
        elif self.falando == True:
            print(f'{self.nome} não pode falar pois já está falando')
        else:
            print(f'{self.nome} começou a falar')
            self.falando = True

            def parar_falar(self):
                if self.falando == True:
                    print(f'{self.nome} parou de falar')
                    self.falando = False
                else:
                    print(f'{self.nome} não está falando')

            def dormir(self):
                if self.comendo == True:
                    print(f'{self.nome} Não pode dormir pois está comendo')
                elif self.dormindo == True:
                    print(f'{self.nome} não pode dormir pois já está dormindo')
                elif self.falando == True:
                    print(f'{self.nome} não pode dormir pois está falando')
                else:
                    print(f'{self.nome} começou a dormir')
                    self.dormindo = True

            def parar_dormir(self):
                if self.dormindo == True:
                    print(f'{self.nome} parou de dormir')
                    self.dormindo = False
                else:
                    print(f'{self.nome} não está dormindo')