n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digte o terceiro numero: '))


menor = n1


if menor > n2:
	menor = n2

if menor > n3:
	menor = n3


print ("o menor numero é {}".format(menor))
