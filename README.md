# Objetivo Geral

Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções:

- Cadastrar usuário (Cliente);
- Cadastrar conta bancária.

### Desafio

Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes:

- Sacar;
- Depositar;
- Visualizar histórico.

Para esta nova versão, criar duas novas funções:

- Criar usuário (cliente do banco);
- criar conta corrente (vincular com usuário).

### Separação em funções

Criar funções para todas as operações do sistema.
Cada função terá uma regra de passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.

### Saque

A função saque deve receber os argumentos apenas por nome (**keyword only**).
Sugestão de argumentos:

- Saldo;
- Valor;
- Extrato;
- Limite;
- numero_saques;
- limite de saques

Sugestão de retorno: saldo e extrato.

### Depósito

A função depósito deve receber os arqgumentos apenas por posição (**positional only**).
Sugestão de argumentos:

- Saldo;
- Valor;
- Extrato;
  susgestão de retorno: saldo e extrato.

### Extrato

A função extrato deve receber os argumentos por posição e nome (**positional only e keyword only**).
Argumentos posicionais: Saldo.
Argumentos nomeados: extrato.

### Novas funções

Criar duas novas funções:

- Criar usuário (cliente do banco);
- criar conta corrente (vincular com usuário).

**Opcional:**

- listar contas

#### Criar usuário (cliente)

O programa deve armazenar os usuários em uma lista, um usuário é composto por:

- nome;
- data de nascimento;
- cpf (deve ser armazenado somente números);
- endereço (formato string com: logradouro, nro - bairro - cidade/UF)

**Obs.:** Não podemos cadastrar 2 usuários com o mesmo CPF.

#### Criar conta corrente

O programa deve armazenar contas em uma lista, uma conta é composta por:

- Agência (fixo: "0001");
- Número da conta;
- Usuário.

O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.

## Dica

Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.
