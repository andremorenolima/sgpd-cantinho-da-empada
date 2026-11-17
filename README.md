# SGPD — Sistema de Gestão de Processos Digitais
## Cantinho da Empada & Café

Sistema de Gestão de Processos Digitais desenvolvido como Minimum Viable Product (MVP) para otimizar o atendimento de balcão e o fluxo de produção na cozinha do estabelecimento **Cantinho da Empada & Café**, substituindo o uso de cadernos físicos e mensagens dispersas.

---

## 🚀 Sobre o Projeto

O SGPD foi projetado para eliminar os gargalos operacionais do dia a dia, garantindo rastreabilidade, agilidade e controle rigoroso dos pedidos. A solução contempla três telas principais integradas:
1. **Tela de Login:** Autenticação segura com proteção de credenciais.
2. **Tela de Cadastro de Encomendas (Balcão):** Registro estruturado de pedidos com validação de campos e proteção contra entradas maliciosas.
3. **Painel de Produção da Cozinha:** Visualização em tempo real (Kanban) com codificação redundante de status (texto, ícone e cor) para mitigar a fadiga sob pressão, alinhado ao **ODS 8 (Trabalho Decente e Crescimento Econômico)**.

---

## 🛠️ Tecnologias Utilizadas

O projeto adota uma arquitetura MVC limpa e segura:
* **Linguagem:** Python 3.12
* **Framework Web:** Flask 3.0
* **Banco de Dados:** SQLite com ORM SQLAlchemy
* **Segurança:** Hashing seguro de senhas (Argon2/bcrypt), consultas parametrizadas e escape Jinja2 contra XSS.
* **Front-end & Acessibilidade:** HTML5, CSS3 responsivo, diretrizes de usabilidade tátil (alvos mínimos de $48\times48$ pixels) e contraste WCAG 2.1 AA.

---

## 📁 Estrutura do Repositório

```text
sgpd-cantinho-da-empada/
├── app.py                 # Arquivo principal da aplicação Flask
├── models.py              # Definição das entidades e banco de dados (SQLAlchemy)
├── requirements.txt       # Dependências e bibliotecas do projeto
├── static/                # Arquivos estáticos (CSS, imagens e scripts JS)
└── templates/             # Templates HTML (Login, Balcão e Cozinha)
```

---

## ⚙️ Instruções de Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local (recomendado Linux/Ubuntu):

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/sgpd-cantinho-da-empada.git
   cd sgpd-cantinho-da-empada
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```bash
   python app.py
   ```

5. **Acesse no navegador:**
   Abra o endereço `http://127.0.0.1:5000` para interagir com o sistema.

---

## 📋 Validação Prática e Métricas

O projeto conta com um plano estruturado de validação externa com o sócio-gerente do estabelecimento, contemplando:
* **Taxa Mínima de Sucesso:** 100% de conclusão nas tarefas operacionais.
* **Eficiência (Tempo Máximo):** Até 120 segundos para a execução do fluxo central de balcão.
* **Satisfação:** Nota mínima de 4 em escala Likert (1 a 5).

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos e práticos no âmbito de engenharia de software e desenvolvimento web.