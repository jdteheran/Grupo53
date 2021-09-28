numero = int(input('pasa el numero: '))

cont = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        cont = cont + 1

if cont == 2:
    print('el numero ', numero, ' es Primo')
else:
    print('el numero ', numero, ' NO es Primo')