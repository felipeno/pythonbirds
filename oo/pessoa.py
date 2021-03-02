
class Pessoa:
    def __init__(self, *filhos, nome = None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    matheus = Pessoa(nome='Matheus')
    felipe = Pessoa(matheus, nome='Felipe')
    print(Pessoa.cumprimentar(felipe))
    print(felipe.cumprimentar())
    print(felipe.nome)
    print(felipe.idade)
    for filho in felipe.filhos:
        print(filho.nome)