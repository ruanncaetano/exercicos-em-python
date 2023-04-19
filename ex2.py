salario=float(input('Digite seu salario\n'))
pres=float(input('Digite o valor da prestação\n'))
valPres=salario*30/100

if valPres<pres:
    print('O emprestimo  não pode ser condedido')
else:
    print('O emprestimo pode ser condedido')