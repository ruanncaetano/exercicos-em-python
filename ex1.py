peso=float(input('Digite seu Peso\n'))
altura=float(input('Digite sua altura\n'))

imc=peso/altura**2

print('Seu IMC é de %.2f' %(imc))

if imc< 18.5:
    print('Abaixo do peso\n')
elif  imc<25:
    print('Peso normal\n')
elif imc< 30:
    print('Acima do peso\n')
elif imc>=30:
    print('Obeso\n')