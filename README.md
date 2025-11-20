# 🐳 System Monitor - Dockerized Python & PostgreSQL App

Uma aplicação Full-Stack containerizada para monitoramento de sistema, utilizando a integração entre **Python (Flask)** e **PostgreSQL** utilizando **Docker** e **Docker Compose**.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.9
* **Framework Web:** Flask
* **Banco de Dados:** PostgreSQL 13
* **Containerização:** Docker & Dockerfile
* **Orquestração:** Docker Compose
* **Driver de Banco:** Psycopg2

## 📋 Pré-requisitos

Para rodar este projeto localmente, você precisa apenas ter o Docker instalado:

* [Docker Desktop](https://www.docker.com/products/docker-desktop) (Windows/Mac) ou Docker Engine (Linux)
* Docker Compose

## 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/FeFuka/system-monitor-docker.git](https://github.com/FeFuka/system-monitor-docker.git)
    cd system-monitor-docker
    ```

2.  **Suba os containers:**
    O comando abaixo irá construir a imagem da aplicação, baixar a imagem do banco de dados e iniciar a rede.
    ```bash
    docker-compose up --build
    ```

3.  **Acesse a aplicação:**
    Abra seu navegador no endereço:
    [http://localhost:8000](http://localhost:8000)

    **Resultado esperado (JSON):**
    ```json
    {
      "database": "PostgreSQL 13.23 ...",
      "status": "Online"
    }
    ```

4.  **Para parar a aplicação:**
    Pressione `Ctrl+C` no terminal ou rode:
    ```bash
    docker-compose down
    ```

## 🏗️ Arquitetura e Conceitos Aplicados

* **Microserviços:** A aplicação é dividida em dois serviços (`web` e `db`) que rodam em containers isolados.
* **Docker Networking:** A comunicação entre a API e o Banco não usa `localhost`, mas sim o DNS interno do Docker, garantindo isolamento da rede do host.
* **Persistência de Dados (Volumes):** Utilização de Docker Volumes (`postgres_data`) para garantir que os dados do banco não sejam perdidos quando o container é reiniciado.
* **Variáveis de Ambiente:** Configuração sensível (senhas, hosts) injetada via `docker-compose.yml`, desacoplando a configuração do código fonte.


