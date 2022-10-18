vc = float(input('Qual o valor da casa que você deseja comprar? R$'))
sal = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar? '))
mes = anos*12
ap = vc/mes < sal*0.3
neg = vc/mes > sal*0.3
parc = vc/mes

if ap:
    print('Parabéns! Seu empréstimo foi aprovado! O valor da sua parcela será de R${:.2f}'.format(parc))
elif neg:
    print('Que pena. Seu empréstimo foi negado, pois a parcela ficou no valor de R${:.2f}, '
          'acima de 30% de seu salário...'.format(parc))