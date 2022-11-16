nome=input('Digite o nome: ')
idade=int(input('digite a idade: '))
doenca_infectocontagiosa=input('Suspeita de doenca infecto-contagiosa: ').upper()
if idade>=65:
    print('O paciente '+nome+" POSSUI atendimento prioritario!")
elif doenca_infectocontagiosa=='SIM':
    print('O paciente '+nome+ ' deve ser direcionado para a sala de espera reservada.')
else:
    print('O paciente '+nome+ ' NAO possui atendimento prioritario e pode aguardar na sala comum!oGui')