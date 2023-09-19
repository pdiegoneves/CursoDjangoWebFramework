# Criando Venv
python -m venv venv

## para usar
source venv/bin/activate

## para desativar
deactivate

# Instalar dependências na venv
pip install pytest
pip install django

# vscode
CTRL + SHIFT + P -> select interpreter -> selecionar python da venv

pip install pip --upgrade => para atualizar o pip
pip install setuptools wheel --upgrade

# iniciar um projeto
python -m pip install pip setuptools wheel --upgrade

criar ambiente virtual
python -m venv venv 
source venv/bin/activate
pip install django

# configurar git

```
git config --global user.name "Diego Neves"
git config --global user.email "pdcassiano@gmail.com"
git config --global init.defaultBranch main
git init
```
## Criar chave ssh
```
ssh-keygen
```

Repositório padrão
https://github.com/luizomf/curso-django-projeto1

# criar projeto django
django-admin startproject projeto .

O . no final indica que o django deve jogar os arquivos na pasta projeto

## instalar pelo arquivo requirements
pip install -r requirements.txt

# Entendendo um projeto django




# Adicionando caminhos staticos
no settings.py adicionar
```
STATICFILES_DIRS = [
    BASE_DIR / 'base_static',
]

STATIC_ROOT = BASE_DIR / 'static'
```

no terminal
```
python.exe .\manage.py collectstatic
```


# Testes

Vamos usar o pytest com runner

instalar
```
pip install pytest pytest-django
```

criar o pytest.ini na raiz

```
[pytest]
DJANGO_SETTINGS_MODULE = project.settings
python_files = test.py tests.py test_*.py tests_*.py *_test.py *_tests.py
addopts =
    --doctest-modules
    --strict-markers
markes =
    slow: Run tests that are slow
    fast: Run fast tests
```