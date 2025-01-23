# Munus - Plataforma de Análise de Dados

Munus é uma plataforma web para análise e visualização de dados, desenvolvida em Django. Permite o upload de arquivos CSV/XLSX, análise de dados e geração de insights através de um painel interativo.

## Funcionalidades Principais

- Autenticação de usuários (cadastro, login, recuperação de senha)
- Upload de arquivos CSV/XLSX
- Visualização e análise de dados
- Painel de análise com gráficos e métricas
- Gerenciamento de perfil do usuário
- Interface totalmente em português

## Requisitos do Sistema

- Python 3.10+
- Django 4.2+
- SQLite3 (ou outro banco de dados suportado pelo Django)
- Bibliotecas listadas em requirements.txt

## Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/munus.git
   cd munus
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

5. Crie um superusuário:
   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

## Guia de Uso Básico

1. Acesse http://localhost:8000
2. Crie uma conta ou faça login
3. Navegue até a página de upload para enviar seus arquivos
4. Acesse o painel de análise para visualizar seus dados
5. Utilize o menu de navegação para acessar outras funcionalidades

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

[MIT License](LICENSE)
