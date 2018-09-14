class Pessoa:
    def __init__(self, pessoa):
        self.nome = pessoa[0]
        self.idade = pessoa[1]
        self.sexo = pessoa[2]
        self.numero = pessoa[3]
        self.peso = pessoa[4]
        self.imc = 0

    def converteDicionario(self):
        pessoa = {
            'nome': self.nome,
            'idade': self.idade,
            'sexo': self.sexo,
            'numero': self.numero,
            'peso': self.peso,
            'imc': 0
        }
        return pessoa