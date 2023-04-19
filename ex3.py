apagar=float(input('Digite o valor a pagar\n'))
esc=float(input('Escolha a forma de pagamento\n1- À vista em dinheiro ou cheque\n2- À vista cartã de crédito\n3- Em 2 vezes\n4- Em 3 vezes\n500'))

if esc==1:
    porct = (apagar) - (apagar * 10 / 100)
elif esc==2:
    porct=(apagar)-(apagar*5/100)
elif esc==3:
    porct=apagar/2
elif esc==4:
    porct = (apagar * 10 / 100)/3

print("devera pagar %.2f"%(porct))