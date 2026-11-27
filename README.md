# CEAL / LUZ — Sistema de gestão institucional

Fundação Django 5.2 LTS + SQLite, Python 3.12 ou 3.13 recomendado.
Documentação de domínio preservada em [docs](docs/).

## Executar no Windows (PowerShell)

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py test config
.\.venv\Scripts\python.exe manage.py runserver
```

Se tiver Python 3.12, substitua `-3.13` por `-3.12`.
Abra http://127.0.0.1:8000/ para login e http://127.0.0.1:8000/admin/ para administração.
O servidor de desenvolvimento é somente local. Use dados fictícios nesta etapa.
A base SQLite, ambiente virtual e segredos não devem ser versionados.

## Escopo

Sprint 0: autenticação, administração, SQLite, página inicial e testes de acesso.
Cadastro de Pessoa, Sócio, Atividade, Grupo e Participação serão implementados nas próximas etapas; permissões institucionais ainda não estão configuradas.
O protótipo React anterior fica no histórico Git; seus arquivos não são necessários nesta versão.

Antes da produção: revisar LGPD, controle de acesso, HTTPS, backups, segredos e banco para concorrência. Não usar o servidor de desenvolvimento em produção.
