def getLimitedInput(inputMsg, validOptions, clearOnFail = False):
	if(not (isinstance(inputMsg, str) and isinstance(inputMsg, list) and isinstance(clearOnFail, bool))):
		print('Incorrect parameter types')
		input()
		return -1

	inputValue = 'invalid answer'
	while(inputValue not in validOptions):
		inputValue = input(inputMsg)
		if(inputValue not in validOptions):
			print("Insira uma opção válida.\n")
	
	return inputValue


def update_energy_tax(energy_tax):
	input_value = float(input('Valor da taxa (em kWh):'))
	if(input_value != 'v'):
		energy_tax = input_value
		print('Taxa atualizada.')
	else:
		print('Retornando...')

	return energy_tax