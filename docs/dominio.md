# Domínio do Sistema CEAL/LUZ

## Conceito central

O sistema será baseado em pessoas.

Uma mesma pessoa pode ter diferentes papéis no centro, dependendo do contexto.

Exemplo:

- Aless é uma pessoa.
- Aless pode fazer login no sistema.
- Aless pode ser IDE em um grupo de atendimento.
- Aless pode ser sócio atuando como operador em outro grupo.

## Entidades iniciais

### Pessoa

Representa qualquer pessoa cadastrada no sistema.

Pode ser:

- IDE
- Sócio
- Usuário do sistema
- Mais de um desses ao mesmo tempo

### Usuário

Representa uma pessoa que pode acessar o sistema com login e senha.

O usuário terá permissões diferentes conforme seu papel no sistema.

### Grupo

Representa uma atividade organizada em dia e horário específicos.

Exemplos:

- PSE-SEGUNDA-19h30
- SAUDE-QUARTA-21h
- AUTOCON-SABADO-9h30

### Participação no grupo

Representa a relação entre uma pessoa e um grupo.

Exemplos:

- Pessoa como IDE atendido
- Pessoa como sócio operador
- Pessoa como sócio dirigente
- Pessoa como sócio facilitador

## Exemplo prático

Pessoa: Aless

Participações:

1. PSE-SEGUNDA-19h30
   - Tipo: IDE
   - Função: Atendido

2. SAUDE-QUARTA-21h
   - Tipo: IDE
   - Função: Atendido

3. AUTOCON-SABADO-9h30
   - Tipo: Sócio
   - Função: Operador

## Modelo conceitual inicial

- pessoas
- usuarios
- grupos
- participacoes_grupo

## Futuro

Possíveis módulos futuros:

- mensalidades de sócios
- histórico de atendimentos
- inscrições em grupos
- reserva de livros
- controle de presença
- relatórios
