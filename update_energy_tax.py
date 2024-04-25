def update_energy_tax(energy_tax):
	input_value = float(input('Valor da taxa (em kWh):'))
	if(input_value != 'v'):
		energy_tax = input_value
		print('Taxa atualizada.')
	else:
		print('Retornando...')

	return energy_tax