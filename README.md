# 🐳 Cloud System Monitor - Full-Stack & DevOps

Uma aplicação Full-Stack containerizada para monitoramento de sistema, projetada para demonstrar o ciclo de vida completo de **DevOps**: Desenvolvimento, Containerização, Infraestrutura em Nuvem (AWS) e Automação.

O projeto resolve inconsistências de ambiente ("works on my machine") e implementa práticas de observabilidade básica.

---

## 🚀 Evolução do Projeto

Este repositório representa a consolidação de três etapas práticas de engenharia:

* ✅ **Fase 1 (Dev & Docker):** Desenvolvimento da API (Python/Flask) e Frontend, orquestração com Docker Compose e persistência de dados (PostgreSQL).
* ✅ **Fase 2 (Cloud Infrastructure):** Provisionamento de servidor Linux na **AWS (EC2)**, configuração de Security Groups (Firewall) e deploy em produção.
* ✅ **Fase 3 (Automação & Ops):** Desenvolvimento de scripts em Python para *Health Checks* automáticos, agendados via **Cron** para monitoramento 24/7.

---

## 🛠️ Tech Stack

* **Linguagem:** Python 3.9 (Flask & Scripting)
* **Banco de Dados:** PostgreSQL 13
* **Frontend:** HTML5 / CSS3 (Jinja2 Templates)
* **Containerização:** Docker & Dockerfile
* **Orquestração:** Docker Compose
* **Cloud:** AWS (EC2, Security Groups)
* **OS:** Linux Ubuntu 24.04 LTS
* **Automação:** Bash & Crontab

---

## 📋 Como Executar (Localmente ou no Servidor)

### 1. Pré-requisitos
* Docker e Docker Compose instalados.

### 2. Configuração de Segurança (.env)
Este projeto segue as boas práticas do *12-Factor App*. As credenciais não estão no código.
Crie um arquivo `.env` na raiz do projeto e defina suas variáveis:

```ini
DB_NAME=monitor
DB_USER=admin
DB_PASS=sua_senha_secreta

POSTGRES_DB=monitor
POSTGRES_USER=admin
POSTGRES_PASSWORD=sua_senha_secreta
```

### 3. Subindo a Aplicação
O comando abaixo constrói a imagem, cria a rede interna e inicia os containers:

```bash
docker-compose up -d --build
```

### 4. Acessando
Abra seu navegador em: `http://localhost:8000` (ou no IP Público da sua instância AWS).

Para parar a aplicação:
```bash
docker-compose down
```

---

## 🤖 Automação de Monitoramento

O projeto inclui um agente de monitoramento (`monitor.py`) projetado para rodar no servidor.

* **Função:** Realiza requisições periódicas para validar se a API e o Banco de Dados estão respondendo corretamente.
* **Logs:** Gera um histórico de disponibilidade em `uptime.log`.
* **Agendamento:** Configurado via Crontab para execução a cada 5 minutos:
    `*/5 * * * * /usr/bin/python3 /caminho/para/monitor.py`

---

## 🏗️ Arquitetura e Conceitos

* **Microserviços:** A arquitetura desacopla a aplicação (`web`) do banco de dados (`db`).
* **Docker Networking:** Comunicação segura via DNS interno do Docker (rede bridge), sem expor o banco de dados publicamente.
* **Persistência (Volumes):** Uso de Docker Volumes para garantir a integridade dos dados mesmo se os containers forem reiniciados.
* **Security Groups:** Na AWS, o acesso SSH é restrito ao IP do administrador, enquanto a porta da aplicação (8000) é pública.

---
Desenvolvido por **Felipe Fuka** 🚀
