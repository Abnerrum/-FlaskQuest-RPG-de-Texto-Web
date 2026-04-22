# ⚔️ FlaskQuest: RPG de Texto Web

O **FlaskQuest** é um simulador de RPG de texto estilo *Dungeon Crawler*. O projeto foi desenvolvido para demonstrar a integração entre um back-end dinâmico em Python e um banco de dados relacional leve.

Este projeto faz parte dos meus estudos de nível **Intermediário** em Python.

## 🚀 Funcionalidades
* **Persistência de Dados:** O progresso do jogador (Vida, Ouro, Nome) não se perde ao fechar o navegador, graças ao SQLite.
* **Sistema de Sessão:** Gerenciamento de estado do utilizador através de `flask.session`.
* **Lógica de Eventos:** Encontros aleatórios processados no servidor (Back-end).
* **Interface Dinâmica:** O HTML altera-se automaticamente com base na saúde (HP) do jogador.

## 🛠️ Tecnologias
* **Python 3**
* **Flask** (Framework Web)
* **SQLite3** (Base de dados)
* **Jinja2** (Engine de templates HTML)

## 📂 Estrutura do Projeto
```text
.
├── app.py              # Lógica principal e rotas Flask
├── game.db             # Base de dados SQLite (gerada automaticamente)
└── templates/
    └── index.html      # Interface do jogo

⚙️ Como Instalar e Rodar
Clonar o repositório:
git clone [https://github.com/teu-utilizador/nome-do-repo.git](https://github.com/teu-utilizador/nome-do-repo.git)
Instalar o Flask:

Bash
pip install flask
Executar a aplicação:

Bash
python app.py
Aceder ao jogo:
Abra o navegador em: http://127.0.0.1:5000

🧠 Conceitos Aplicados
Arquitetura Web: Comunicação entre rotas (routes) e templates.

SQL: Comandos de INSERT, SELECT e UPDATE para manipular dados do herói.

Segurança de Estado: Validação de ações no lado do servidor para evitar manipulação de dados no cliente.
