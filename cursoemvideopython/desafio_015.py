usuario = input('Informe o seu nome: ')
carro = input('Qual carro foi alugado? ')
km = float(input('Informe a kilometragem total percorrida: '))
diarias = int(input('Informe a quantidade de diárias do veículo: '))
vdiarias = (diarias * 60.00)
vkm = (km * 0.15)
print('Prezado {}!'.format(usuario))
print('O veículo {} foi alugado por um total de {} dias, totalizando {:.2f} kilometros percorridos.'.format(carro, diarias, km))
print('Considerando o valor de R$ 60,00 a diária e R$ 0,15 por kilometro percorrido, segue o valor total a pagar:')
print('Valor total: R$ {:.2f}'.format(vkm + vdiarias))