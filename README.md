# Projeto Django: Estrutura Padrão com Dependências Gerenciadas

## 🔬 Descrição Científica

Este repositório contém a estrutura básica de um projeto Python com Django, incluindo gerenciamento de dependências via Poetry e ambiente virtual isolado. O objetivo é fornecer uma base reprodutível e organizada para aplicações web, facilitando a extensão e manutenção do código em contextos de pesquisa, ensino e desenvolvimento profissional.

## 🗂️ Estrutura de Diretórios

- `manage.py`: Script de gerenciamento do Django.
- `db.sqlite3`: Banco de dados SQLite local.
- `.gitignore`: Arquivos ignorados pelo Git.
- `poetry.lock` e `pyproject.toml`: Gerenciamento de dependências com o Poetry.
- `requirements.txt`: Alternativa de instalação via pip.
- `.venv/`: Ambiente virtual contendo os pacotes instalados.

## 🧪 Principais Bibliotecas Instaladas

- `Django`
- `asgiref`, `anyio`, `cffi`, `certifi`, `charset_normalizer`, entre outras.

Essas bibliotecas são utilizadas tanto para a execução do servidor quanto para manipulação de rede, codificação de caracteres, segurança e compatibilidade assíncrona.

## 🧰 Ambiente Virtual

O projeto utiliza um ambiente virtual localizado na pasta `.venv/`. O uso de um ambiente isolado garante que os pacotes utilizados não entrem em conflito com outros projetos ou com a instalação global do Python.

## 🧬 Reprodutibilidade

Para garantir a reprodutibilidade do ambiente, recomenda-se utilizar:

pip install -r requirements.txt


Acesse o site original aqui: [CCM-TJAL](http://ccm-tjal-app.nucleozero.app)