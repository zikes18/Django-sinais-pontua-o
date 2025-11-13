# 📚 Catálogo Gramatical de Pontuação

Um projeto Django focado no estudo e validação do uso de sinais de pontuação na língua portuguesa.

O objetivo é mapear cada sinal gráfico (ex: vírgula) à sua função gramatical específica (ex: isolar o vocativo), criando um catálogo de consulta e uma ferramenta de análise interativa. O design foi projetado para ser aconchegante e confortável para longos períodos de leitura.

![Logo do Projeto](static/img/logo.png)

## ✨ Principais Funcionalidades

* 📖 **Catálogo de Regras:** Uma lista completa com mais de 40 regras de pontuação, suas funções e exemplos de uso, com um design focado em leitura confortável.
* ✍️ **Analisador de Texto:** Uma ferramenta interativa onde o usuário pode inserir um texto e o sistema identifica quais sinais de pontuação cadastrados foram utilizados.
* 🗃️ **Banco de Dados Gramatical:** Base de dados robusta (MySQL) que mapeia Sinais ➔ Funções ➔ Estruturas Sintáticas.
* 🎨 **Tema Aconchegante:** Interface com paleta de cores sépia, tipografia serifada e logo personalizado para reduzir a fadiga ocular.
* 🔒 **Seguro:** Utiliza `python-dotenv` para manter dados sensíveis (senhas de banco de dados, `SECRET_KEY`) fora do código-fonte.

## 💻 Tecnologias Utilizadas

* **Backend:** Python 3, Django 4.x
* **Banco de Dados:** MySQL (configurado, mas pode ser trocado pelo Django ORM)
* **Frontend:** Templates HTML5/CSS3 (renderizados pelo Django)
* **Gerenciamento de Ambiente:** `python-dotenv`
* **Dependências Python:** `django`, `mysqlclient`, `python-dotenv` (veja `requirements.txt`)

---

## 🏗️ Estrutura do Projeto
catalogo_gramatical/ ├── .env # <-- ARQUIVO SECRETO DE VARIÁVEIS (NÃO VA PARA O GIT) ├── .gitignore # Ignora arquivos (como .env, venv/) ├── manage.py # Utilitário de gerenciamento do Django ├── requirements.txt # Lista de dependências Python ├── README.md # Este arquivo │ ├── catalogo_gramatical/ # Pasta principal do projeto │ ├── settings.py # Configurações do projeto (lê o .env) │ ├── urls.py # URLs globais (aponta para 'gramatica.urls') │ └── ... │ ├── gramatica/ # App "gramatica" │ ├── models.py # Define as tabelas (SinalDePontuacao, etc.) │ ├── views.py # Lógica (funções lista_regras e analisador_view) │ ├── urls.py # URLs do app (lista_regras e analisador) │ ├── admin.py # Configuração da interface /admin │ ├── migrations/ # Histórico de migrações do banco de dados │ └── fixtures/ │ └── gramatica_completa.json # Arquivo de dados iniciais │ ├── templates/ # Pasta de templates HTML │ ├── base.html # Template mestre (inclui header, footer e CSS) │ ├── partials/ │ │ ├── _header.html # Cabeçalho (com navegação e logo) │ │ └── _footer.html # Rodapé │ └── gramatica/ │ ├── lista_regras.html # Página do catálogo de regras │ └── analisador.html # Página do analisador de texto │ └── static/ # Pasta de arquivos estáticos ├── css/ │ └── style.css # Folha de estilo "aconchegante" └── img/ └── logo.png # Logo do site (fundo transparente)
---

## 🚀 Instalação e Execução

Siga estes passos para configurar e executar o projeto em seu ambiente local.

### 1. Pré-requisitos

* Python 3.8+
* Git
* Um servidor de banco de dados **MySQL** (ou MariaDB) instalado e em execução.

### 2. Clonar o Repositório

``bash
git clone https://[URL-DO-SEU-REPOSITORIO].git
cd catalogo_gramatical

### 3. Configurar o Ambiente Virtual
É altamente recomendado usar um ambiente virtual:

Bash

# Criar o ambiente
python -m venv venv

# Ativar o ambiente
# No Windows:
venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate

### 4. Instalar Dependências
O arquivo requirements.txt contém todas as bibliotecas necessárias.

Bash

pip install -r requirements.txt

### 5. Configurar as Variáveis de Ambiente (.env)

O settings.py é configurado para ler dados sensíveis de um arquivo .env.

Crie um arquivo chamado .env na pasta raiz do projeto (ao lado do manage.py).

Copie e cole o conteúdo abaixo, substituindo pelos seus dados:

Ini, TOML

# .env (Arquivo de Variáveis de Ambiente)

# Configurações do Django
SECRET_KEY=sua-secret-key-super-secreta-aqui
DEBUG=True

# Configurações do Banco de Dados
DB_NAME=sinais_pontuacao
DB_USER=seu_usuario_mysql
DB_PASSWORD=sua_senha_mysql
DB_HOST=localhost
DB_PORT=3306
### 6. Criar o Banco de Dados
Crie o banco de dados no seu servidor MySQL (o nome deve ser o mesmo que você colocou em DB_NAME no arquivo .env).

SQL

CREATE DATABASE sinais_pontuacao 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
### 7. Executar as Migrações
Este comando usará as credenciais do .env para se conectar ao MySQL e criar todas as tabelas.

Bash

python manage.py migrate

### 8. Carregar os Dados Iniciais (Fixtures)
Este comando irá popular seu banco de dados com as mais de 40 regras de pontuação.

Bash

python manage.py loaddata gramatica_completa

### 9. Criar um Superusuário
Você precisará de um superusuário para acessar a área de administração do Django.

Bash

python manage.py createsuperuser
(Siga as instruções para criar um nome de usuário e senha)

### 10. Iniciar o Servidor
Tudo pronto! Inicie o servidor de desenvolvimento:

Bash

python manage.py runserver