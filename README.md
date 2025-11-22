# Sistema de Gerenciamento de EPI (Equipamentos de Proteção Individual)

**Autores:** Luiz Gabriel Gazolli dos Santos / Juliana Martins 
**Projeto:** Mini Projeto Django 
**Tema:** Sistema corporativo para controle de EPIs e colaboradores  

---

## 🧩 Descrição do Projeto

Este projeto foi desenvolvido como parte da Atividade 6 da disciplina de Desenvolvimento Web com **Django**.  
O sistema tem como objetivo o **gerenciamento de Equipamentos de Proteção Individual (EPI)** em um ambiente corporativo, permitindo:

- Cadastro e controle de colaboradores (com CPF e matrícula únicos).  
- Cadastro e controle de EPIs (estoque, categoria, validade).  
- Registro de **empréstimos** e **devoluções** de EPIs.  
- Emissão de **relatórios e consultas** filtráveis (por colaborador, tipo de EPI e validade vencida).  

O sistema possui controle de autenticação e acesso via `/admin/` e `/accounts/login/`, além de uma interface moderna e intuitiva.

---

## ⚙️ Funcionalidades

| Módulo | Descrição |
|--------|------------|
| 👥 Colaboradores | CRUD completo com validação de CPF e matrícula |
| 🛡️ EPIs | Cadastro, edição e exclusão de equipamentos com validade e estoque |
| 📦 Empréstimos | Registro de retirada e devolução com controle automático de estoque |
| 📊 Relatórios | Filtros por colaborador, tipo de EPI e validade vencida |
| 🔐 Autenticação | Login e logout de usuários administrativos |
| 🎨 Interface | Layout responsivo em estilo empresarial |

---

## 🧠 Tecnologias Utilizadas

- **Python 3.10+**
- **Django 4.x**
- **HTML5 / CSS3**
- **SQLite** (banco de dados padrão Django)
- **Bootstrap-like styling (customizado)**

---

## 🧭 Estrutura de Pastas (principais)

EPI-System-Juliana/
│
├── manage.py
├── loja/ # Projeto base Django
├── colaboradores/ # App de colaboradores (já existente no projeto base)
├── epi/ # App para gerenciamento de EPIs
├── emprestimos/ # App para controle de empréstimos/devoluções
├── relatorios/ # App para relatórios e consultas
│
├── templates/
│ ├── base.html # Layout principal do sistema
│ └── registration/ # Templates de login/logout
│
└── static/
└── css/
└── style.css # Estilo corporativo


---

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório
```bash
git clone [https://github.com/JulianaMartinss/EPI-System-Juliana.git]
cd mini_projeto_django_loja
git fetch origin
git checkout epi

2️⃣ Criar e ativar ambiente virtual
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Linux/Mac

3️⃣ Instalar dependências
pip install django
# ou, se existir requirements.txt
# pip install -r requirements.txt

4️⃣ Migrar banco e criar superusuário
python manage.py migrate
python manage.py createsuperuser

5️⃣ Rodar o servidor
python manage.py runserver


Acesse:
🔗 http://127.0.0.1:8000/

📁 URLs Principais
Caminho	Descrição
/admin/	Painel administrativo Django
/epi/	Cadastro e controle de EPIs
/emprestimos/	Empréstimos e devoluções
/relatorios/colaborador/	Relatório por colaborador
/relatorios/epi/	Relatório por tipo de EPI
/relatorios/vencidos/	Relatório de EPIs vencidos
/accounts/login/	Tela de login
🧾 Padrões de Commit

Use mensagens claras e padronizadas:

feat: adicionar CRUD de EPIs
fix: corrigir carregamento de CSS estático
style: atualizar layout único

👨‍💻 Autores

Desenvolvido por Luiz Gabriel Gazolli dos Santos / Juliana Martins 

Projeto Mini Loja - EPI | 2025


