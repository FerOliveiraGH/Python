from oo.conta import Conta
from oo.cliente import Cliente

cliente = Cliente('Fernando Oliveira', '123')
conta = Conta(123, cliente, 100, 1000)
print('Titular:', conta.titular)
print(conta.extrato(), end='\n\n')

cliente2 = Cliente('Fulano da Silva', '456')
conta2 = Conta(456, cliente2, 50, 1000)
print('Titular:', conta2.titular)
print(conta2.extrato(), end='\n\n')

transferir = 20
print(f'Transferir R$ {transferir} da conta {conta.numero} para conta {conta2.numero}')
conta.transferir(transferir, conta2)
print(conta.extrato())
print(conta2.extrato(), end='\n\n')

sacar = 100
print('Sacar da conta {} o valor de {}'.format(conta.numero, sacar))
conta.sacar(sacar)
print(conta.extrato(), end='\n\n')

sacar = 980.01
print('Sacar da conta {} o valor de {}'.format(conta.numero, sacar))
conta.sacar(sacar)
print(conta.extrato(), end='\n\n')

sacar = 980
print('Sacar da conta {} o valor de {}'.format(conta.numero, sacar))
conta.sacar(sacar)
print(conta.extrato(), end='\n\n')

print('Código banco estático:', Conta.codigo_banco())
