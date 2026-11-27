# Decisão tecnológica — Sprint 0

Adotar Django 5.2 LTS com templates HTML e SQLite para desenvolvimento local e MVP. Preservar os conceitos de Pessoa, Usuário, Sócio, Atividade, Grupo e Participação descritos em arquitetura.md. O usuário de autenticação Django não representa automaticamente uma Pessoa; o vínculo será modelado na etapa de cadastros. A divergência de papéis entre domínio.md e arquitetura.md deve ser resolvida usando a separação entre condição de sócio, tipo de participação e função, após validação de negócio.

O código React inicial era um scaffold e é preservado no histórico. Não introduzir SPA, API separada ou dependências frontend nesta fundação. Avaliar PostgreSQL antes de uso simultâneo em produção. Dados reais e segredos não devem entrar no Git.
