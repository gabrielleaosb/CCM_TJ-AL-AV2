
# Guia de Setup para Desenvolvimento

## Clonando o repositório

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

## Criando o ambiente virtual

```bash
python -m venv venv
```

### Ativando o ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

## Instalando dependências do Python

```bash
pip install -r requirements.txt
```

## Instalando o Tailwind CSS CLI

```bash
npm install -D @tailwindcss/cli
```

## Gerando o CSS com Tailwind

Deixe esse comando rodando em um terminal separado:

```bash
npx tailwindcss -i ./ccmtj/static/css/input.css -o ./ccmtj/static/ccmtj/css/output.css --watch
```

## Aplicando as migrações

```bash
python manage.py migrate
```

## Rodando o servidor

```bash
python manage.py runserver
```
