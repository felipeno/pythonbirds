class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'

    @staticmethod
    def estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    matheus = Pessoa(nome='Matheus')
    felipe = Pessoa(matheus, nome='Felipe')
    print(Pessoa.cumprimentar(felipe))
    print(felipe.cumprimentar())
    print(felipe.nome)
    print(felipe.idade)

    for filho in felipe.filhos:
        print(filho.nome)

    felipe.sobrenome = 'Nogueira'
    print(felipe.sobrenome)
    del felipe.filhos
    print(felipe.__dict__)
    print(matheus.__dict__)
    print(felipe.olhos)
    print(id(felipe.olhos), id(matheus.olhos))

    print(felipe.estatico())
    print(felipe.nome_e_atributos_de_classe())
