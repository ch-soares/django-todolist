# Projeto de aplicação Django do curso [DevPro](https://www.dev.pro.br/)

### Objetiva realizar um CRUD: Create, Read, Update e Delete. Funções básicas para qualquer tipo de aplicação.

[![Aplicação Django](https://github.com/ch-soares/django-todolist/actions/workflows/django.yml/badge.svg)](https://github.com/ch-soares/django-todolist/actions/workflows/django.yml)
[![codecov](https://codecov.io/gh/ch-soares/django-todolist/branch/main/graph/badge.svg?token=8EKW2SB2KC)](https://codecov.io/gh/ch-soares/django-todolist)

## Para Instalar:
Supondo que tenha Git e Python (versao: > 3.11) devidamente instalados, no terminal dê os comandos:

```commandline
git clone https://github.com/ch-soares/curso-django.git
cd django-todolist
cp contrib/env-sample .env
python -m pip install pipenv
pipenv install -d
```
Garanta que esteja no diretório raiz e ative o ambiente virtual:

```commandline
pipenv shell
```

Rode as migrações:

```commandline
python manage.py migrate
```

Rodando o servidor local:

```commandline
python manage.py runserver
```

## O projeto

Consiste em realizar um todolist em que no topo da página possui um campo para inserção de tarefas.

![Captura de tela de 2023-06-13 16-25-49](https://github.com/ch-soares/django-todolist/assets/65301099/d913b756-10c9-4ab6-822c-00a10fa97977)

Ao criar uma nova tarefa, esta é listada logo abaixo do título: Tarefas Pendentes, que possui um botão para marcar esta tarefa como feita.

![Captura de tela de 2023-06-14 14-57-27](https://github.com/ch-soares/django-todolist/assets/65301099/6cd40fdf-d638-409b-a02a-7c4d3533f61b)

Em realizado esta operação, a tarefa é listada logo abaixo do título: Tarefas Concluídas, que, por sua vez, possui um botão para marcá-la como pendente e um botão à esquerda para apagar a tarefa.

![Captura de tela de 2023-06-14 14-55-37](https://github.com/ch-soares/django-todolist/assets/65301099/70d628ae-1dba-4f41-94fd-b9776a50fb3a)

Clicando no botão "Marcar como Feita" a tarefa volta ao status original de sua criação, isto é: pendente. Se clicado no de "Apagar", a tarefa é excluída.

A página foi criada com o auxílio do Bootstrap5, cuja vantagem é o desenvolvimento rápido, funcional e seguro para aplicações frontend. 

Neste projeto, foram abordados e colocados em prática temas caros para o melhor desenvolvimento de software, a saber:
- Biblioteca Python Decouple, para gerenciar variáveis de ambientes;
- TDD - Testes Automáticos: utilizando-se do pytest-django para tanto, visando dar confiabilidade e segurança ao código;
- Coberturas de testes utililizando-se da plataforma Codecov, no qual fornece relatórios intuitivos e apresentáveis da cobertura de testes da aplicação;
- Legibilidade: utilizando a biblioteca flake8 que verifica o código Python em busca de possíveis problemas ou inconsistências;
- Integração contínua com o Github Actions, garantindo que o código novo só entre na branch principal se validados todos os testes e se o código não possui inconsistências.

## Licença
- MIT License: Sinta-se à vontade para utilizar o código da maneira que desejar.

## Divirta-se!
