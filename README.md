# Munus - Sistema de Análise de Dados

Munus é um sistema web desenvolvido em Django para upload e análise de arquivos CSV/XLSX. Permite visualizar dados em dashboards e gerar insights a partir dos arquivos enviados.

## Tecnologias Utilizadas

- Python 3.x
- Django 4.x
- SQLite3 (banco de dados)
- HTML5/CSS3 (frontend)
- Bootstrap (opcional, para estilização)

## Como Rodar o Projeto

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
6. Crie um superusuário:
   ```bash
   python manage.py createsuperuser
   ```
7. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
8. Acesse `http://localhost:8000`

## Estrutura de Diretórios

```
munus/
├── db.sqlite3            # Banco de dados SQLite
├── manage.py             # Script de gerenciamento do Django
├── media/                # Arquivos enviados pelos usuários
│   └── uploads/          # Pasta de uploads de arquivos CSV/XLSX
├── munus/                # Configurações do projeto Django
│   ├── settings.py       # Configurações do projeto
│   ├── urls.py           # URLs principais
│   └── ...
├── pages/                # App principal
│   ├── templates/        # Templates HTML
│   │   └── pages/        # Templates específicos
│   │       ├── base.html # Template base
│   │       ├── home.html # Página inicial
│   │       ├── upload.html # Página de upload
│   │       └── ...
│   ├── models.py         # Modelos de banco de dados
│   ├── views.py          # Lógica das views
│   └── ...
└── ...
```

## Exemplos de Uso

1. Acesse a página de upload (`/upload`)
2. Selecione um arquivo CSV/XLSX
3. Visualize os dados na página de dashboard (`/dashboard`)
4. Explore diferentes visualizações e insights

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
