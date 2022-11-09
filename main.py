from fila_de_prioridade import FilaPrioridade
from professor import Professor

prof1 = Professor('João', 20201143000020, 'Metodologia e Técnicas de Computação', 'Jaguaribe', 'Cedro', 720, 26, 9.74)
prof2 = Professor('Francisco', 20211143000027, 'Sistemas de Computação', 'Cedro', 'Caninde', 400, 24, 9.5)
prof3 = Professor('Marina', 20201143000042, 'Administração de SIstemas Abertos', 'Caninde', 'Nenhum', 1080, 29, 10)
prof4 = Professor('Heitor', 20201143000083, 'Administração de SIstemas Abertos', 'Caninde', 'Nenhum', 5600, 31, 10.5)
fila1 = FilaPrioridade()


fila1.push(prof3)
fila1.push(prof2)
fila1.push(prof1)
fila1.push(prof4)
fila1.pop()
print(fila1)
print(fila1.empty())
print(fila1.lengh())

