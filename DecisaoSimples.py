nome=input('Digite o nome: ')
idade=int(input('Digite a Idade: '))
prioridade='NAO'
if idade>=65:
    prioridade='SIM'
print('O paciente '+ nome + ' possui atendimento prioritario? '+prioridade)