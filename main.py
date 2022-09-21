# Desafio simples de estudo em Python com sets
# Aqui criarei um mini programa que gera 3 listinhas conforme a necessidade abaixo:
# Primeira Lista 'l1' = Funcinarios que possuem carro e trabalham no horario da noite
# Segunda Lista 'l2' = Funcinarios que possuem carro e trabalham no horario do dia
# Terceira Lista 'l3' = Funcinarios que não possuem carro 
# Quarta Lista 'l4' = Funcionarios que vão de Bus


funcionarios = ['Valdir','Pedro','Lorrayne','Patrick', 'Jorge','Thiago','Bruna']
turno_dia = ['Valdir','Pedro','Lorrayne','Jorge']
turno_noite=['Patrick','Thiago','Bruna']
tem_carro = ['Valdir','Pedro','Bruna']
vai_de_bus = ['Lorrayne','Patrick','Jorge','Thiago']


# Primeira lista 
l1 = set(tem_carro).intersection(turno_noite)
print(l1)

# Segunda lista 
l2 = set(tem_carro).intersection(turno_dia)
print(l2)

# terceira lista
l3 = set(funcionarios).difference(tem_carro)
print(l3)

# Quarta Lista 
l4 = set(vai_de_bus).intersection(turno_noite)
print(l4)

# Quinta Lista 
l5 = set(vai_de_bus).intersection(turno_dia)
print(l5)

# Final do exercicio simples em Python para prática de linguagem usando sets