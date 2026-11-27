# Cadastro de pessoas — Sprint 1

Campos iniciais propostos: nome obrigatório, e-mail, telefone e nascimento opcionais, situação ativa/inativa e timestamps. Não se exige CPF nem se armazenam dados clínicos ou religiosos neste módulo. Pessoas não são automaticamente usuários, sócios ou participantes. Esses vínculos serão modelados depois.

Acesso por permissões Django view/add/change; superusuário já possui acesso. Inativar ou reativar exige POST e permissão de alteração. Exclusão física não é oferecida pela interface ou admin. Busca e filtro de situação com paginação. Dados fictícios somente até revisão de segurança e LGPD.

Após atualizar a branch: python manage.py migrate; python manage.py test config pessoas; python manage.py runserver.
