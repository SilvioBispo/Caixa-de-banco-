import sys

from cadastro import cadastro
from conta import conta
from saldo import saldo

n = input('ja possui conta ?')

if (n == 'nao'):
    nome = input('nome:')
    cpf = input('cpf:')
    cd = cadastro(nome,cpf)

    dpinicial = input('deposito inicial:')
    opinicial = 'deposito'
    idp = input('conta:')
    sldinicial = saldo(idp,dpinicial,opinicial)

else:
    opsn = input('deseja realizar uma operação ?')

    if(opsn == 'sim'):

        opc = input('deposito ou saque ?')
        id = input('numero da conta:')
        cnt = conta(id)
        vlr = int(input('valor:'))
        saldo(id,vlr,opc)

    else:
       sys.exit()

