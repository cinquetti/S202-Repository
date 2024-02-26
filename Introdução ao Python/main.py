class Professor:
    def __init__(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        return f"O professor {self.nome} está ministrando uma aula sobre {assunto}."


class Aluno:
    def __init__(self, nome):
        self.nome = nome

    def presenca(self, nome):
        return f"O Aluno {self.nome} está presente"

class Aula:
    def __init__(self, professor, assunto, alunos):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos

    def adicionar_aluno(self, aluno):
        return self.alunos.append(aluno)

    def listar_presenca(self):
        lista_alunos = ", ".join([aluno.nome for aluno in self.alunos])
        return f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n{lista_alunos}"


#Exemplos de Uso

professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
alunosTotais = []
aula = Aula(professor, "Programação Orientada a Objetos", alunosTotais)
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
print(aula.listar_presenca())

# Presença na aula sobre Programação Orientada a Objetos, ministrada pelo professor Lucas:
# O aluno Maria está presente.
# O aluno Pedro está presente.