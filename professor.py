class Professor:
    def __init__(self, nome, matricula : int, subarea : str, campus_atual : str, campus_removido: str, tempo_de_ifce : int, idade, nota_concurso):
        self.nome = nome
        self.maticula = matricula
        self.subarea = subarea
        self.campus_atual = campus_atual
        self.campus_removido = campus_removido
        self.tempo_de_ifce = tempo_de_ifce
        self.idade = idade
        self.nota_concurso = nota_concurso
    
    def __repr__(self):
        return self.nome
