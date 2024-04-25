# Eel = P.∆t
# P = Potência(kW)
# ∆t = tempo de uso

import math
import os

choice = 0
if(input('load save?(y/n) ') == 'y'):
	try:
		from save import content as devices
		from save import energy_tax as energy_tax
	except:
		print("save not found.")
		input('Clique para continuar...')
		devices = {}
		energy_tax = 0.5
else:
	devices = {}
	energy_tax = 0.5



while(choice != 4):
	os.system('cls')
	#Menu
	print(
		'------Cálculo de gasto de energia por mês------\n'+
		'Taxa atual: '+str(energy_tax)+'\n'
		'0 - Atualizar taxa de energia.\n'
		'1 - Listar eletrônicos já cadastrados.\n'
		'2 - Cadastrar eletrônico.\n'
		'3 - Remover eletrônico.\n'
		'4 - Sair.'
	)
	choice = int(input())
	os.system('cls')

	if(choice == 0):
		from update_energy_tax import update_energy_tax
		energy_tax = update_energy_tax(energy_tax)

	elif(choice == 1):
		total = 0
		for key in list(devices.keys()):
			print('-', key)
			print('   Potência:        ', devices[key]['power'],'kW')
			print('   Uso/dia:         ',devices[key]['use_hours'],'horas')
			print('   Gasto energético:', devices[key]['energy_spent'],'kW/h')
			print('   Custo mensal:     R$'+str(math.ceil(devices[key]['energy_spent']*energy_tax*100)/100))
			total += math.ceil(devices[key]['energy_spent']*energy_tax*100)/100
			print()
		print('Total: R$'+str(total))
		input('Clique para continuar...')

	elif(choice == 2):
		name = input('Nome do eletrônico: ')
		if(name == 'return'):
			break
		while(choice != '1' and choice != '2'):
			choice = input('Qual a medida do valor que aparece no eletrônico?\n1- W\n2- kW/h\n')
			if(choice != '1' and choice != '2'):
				print('insira uma opção válida.\n\n')
		
		if(choice == '1'):
			power = math.ceil(float(input('Potência (em W):'))*100)/100
			power = power/1000
			use_hours = float(input('Uso por dia (em horas):'))
			energy_spent = float(math.ceil(power*(use_hours*31)*100)/100)
		elif(choice == '2'):
			energy_spent = (math.ceil(float(input('Gasto energético (em kW/h):'))*100)/100)
			use_hours = float(input('Uso por dia (em horas):'))
			power = float(math.ceil((energy_spent/(use_hours*31))*100)/100)

		print('Nome:            ', name)
		print('Potência:        ', power, 'kW')
		print('Uso/dia:         ', use_hours, 'horas')
		print('Gasto energético:', energy_spent, 'kW/h')
		print()
		while(choice != 's' and choice != 'n'):
			choice = input('Confirmar? (s/n): ')
			if(choice == 's'):
				devices[name] = {'power': power, 'use_hours':  use_hours, 'energy_spent': energy_spent}
			elif(choice == 'n'):
				print('Retornando...')

	elif(choice == 3):
		name = input('informe o nome do eletrônico que deseja remover: ')
		if(name in devices):
			devices.pop(name)
			print('Removido com sucesso.')
		else:
			print('Eletrônico não encontrado.')
		input('Clique para continuar...')

	elif(choice == 4):
		print('Salvando e finalizando...')
		file = open('./save.py', 'w', encoding='utf8')
		file.write('content = '+str(devices)+'\nenergy_tax = '+str(energy_tax))
		file.close()
	else:
		print('Escolha uma opção válida.')
	
	print('\n')






# potencia = float(input('Potencia (em W):'))
# uso_por_dia = float(input('uso por dia (em horas): '))

# Eel = (potencia/1000)*(uso_por_dia*30)

# # Em 11/2023 estava 0.39959
# taxa_kwh = float(input('Taxa de energia (em kWh):'))
# custo = Eel*taxa_kwh

# print('custo:', custo)