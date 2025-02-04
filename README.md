# Sistema de Operações de Caixa de Banco em Python
Este projeto simula as operações de um caixa de banco básico, utilizando Python para a lógica de negócios e MySQL como banco de dados para armazenar as informações das contas e transações. A aplicação implementa um CRUD (Create, Read, Update, Delete) para gerenciar as contas bancárias e as transações realizadas.

Funcionalidades
+ Criar conta: Permite a criação de novas contas bancárias.
+ Consultar saldo: Exibe o saldo atual de uma conta.
+ Depositar: Realiza o depósito de um valor na conta do cliente.
+ Sacar: Realiza o saque de um valor, com verificação se o saldo é suficiente.

Tecnologias Utilizadas:
+ Python: Para a lógica de implementação.
+ MySQL: Para o armazenamento persistente de contas bancárias e transações.
+ MySQL Connector: Para conectar o Python ao banco de dados MySQL.

Banco de Dados:

O sistema utiliza um banco de dados MySQL para armazenar as informações. As principais tabelas são:
+ contas: Armazena as informações das contas bancárias (id, nome do titular, saldo).
+ transacoes: Registra as transações realizadas (tipo de transação, valor, data, id da conta).
