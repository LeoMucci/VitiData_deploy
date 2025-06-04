# 🍇 VitiData API - Sistema de Análise de Dados Vitivinícolas

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Deploy](https://img.shields.io/badge/Deploy-Render-purple.svg)](https://render.com)

> **Tech Challenge - Fase 1 | Machine Learning Engineering**  
> Solução desenvolvida para democratizar o acesso aos dados oficiais de vitivinicultura brasileira da Embrapa

---

## 📋 Sobre o Projeto

O **VitiData API** é uma API RESTful robusta e documentada que automatiza a extração e disponibilização de dados históricos de vitivinicultura do portal [Embrapa VitiBrasil](http://vitibrasil.cnpuv.embrapa.br). 

Desenvolvida como solução para o **Tech Challenge da FIAP**, esta API transforma dados dispersos em endpoints estruturados, prontos para alimentar modelos de Machine Learning, sistemas de BI e análises estratégicas do setor vitivinícola brasileiro.

---

## 🎯 Problema e Contexto

### 📌 O Desafio
A vitivinicultura brasileira possui um rico acervo de dados históricos desde 1970 no portal da Embrapa, abrangendo:
- **Produção** por região e tipo de uva
- **Processamento** de vinhos e derivados  
- **Comercialização** no mercado interno
- **Importação** de produtos vitivinícolas
- **Exportação** para mercados internacionais

**Problema**: Esses dados não são expostos via API pública, dificultando integração com sistemas analíticos e modelos de ML.

### 🚀 Nossa Solução
Uma API RESTful que:
- ✅ **Automatiza** a extração de dados via web scraping
- ✅ **Padroniza** os dados em formato JSON estruturado
- ✅ **Documenta** todos os endpoints com Swagger/OpenAPI
- ✅ **Disponibiliza** acesso público e gratuito

---


### 🧱 Componentes da Arquitetura

| Camada | Tecnologia | Responsabilidade |
|--------|------------|------------------|
| **Extração** | Selenium + BeautifulSoup | Web scraping automatizado |
| **Processamento** | Pandas | Limpeza e estruturação de dados |
| **Validação** | Pydantic | Garantia de qualidade dos dados |
| **API** | FastAPI | Interface REST documentada |
| **Deploy** | Docker + Render | Containerização e hospedagem |

---

## ⚙️ Stack Tecnológica Completa

### Backend & Core
- **Python 3.11** - Linguagem principal
- **FastAPI** - Framework web moderno e performático
- **Uvicorn** - Servidor ASGI de alta performance
- **Pydantic** - Validação de dados e serialização

### Web Scraping & Data
- **Selenium WebDriver** - Automação de navegador
- **BeautifulSoup4** - Parser HTML/XML
- **Pandas** - Manipulação e análise de dados
- **Requests** - Cliente HTTP

### DevOps & Deploy
- **Docker** - Containerização da aplicação
- **Render** - Plataforma de deploy em nuvem


---

## 📊 Endpoints da API

### 🌐 Base URL
**Produção**: `https://vitidata-api.onrender.com`  
**Local**: `http://localhost:8000`

### 📋 Lista Completa de Endpoints

| Método | Endpoint | Descrição | Dados Retornados |
|--------|----------|-----------|------------------|
| `GET` | `/` | 🏠 Página inicial | Informações da API |
| `GET` | `/healthz` | 💚 Health check | Status da aplicação |
| `GET` | `/producao` | 🍇 Dados de produção | Produção por região/ano/tipo |
| `GET` | `/processamento` | ⚙️ Processamento | Volume processado por tipo |
| `GET` | `/comercializacao` | 🛒 Comercialização | Vendas mercado interno |
| `GET` | `/importacao` | 📥 Importação | Produtos importados por país |
| `GET` | `/exportacao` | 📤 Exportação | Produtos exportados |
| `GET` | `/docs` | 📚 Documentação Swagger | Interface interativa |
| `GET` | `/redoc` | 📖 Documentação ReDoc | Documentação alternativa |

### 📄 Exemplo de Resposta JSON

```json
{
  "success": true,
  "data": [
    {
      "ano": 2023,
      "produto": "Vinho de Mesa Tinto",
      "quantidade": 123456789,
      "unidade": "litros",
      "regiao": "Rio Grande do Sul"
    },
    {
      "ano": 2023,
      "produto": "Vinho Fino Branco", 
      "quantidade": 45678901,
      "unidade": "litros",
      "regiao": "Vale dos Vinhedos"
    }
  ],
  "total_records": 150,
  "source": "Embrapa VitiBrasil",
  "extracted_at": "2024-03-15T10:30:00Z",
  "api_version": "1.0.0"
}
```

---

## 🚀 Guia de Instalação

### 💻 Instalação Local

#### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/luccamenezes/VitiData.git
cd VitiData
```

#### 2️⃣ Configure Ambiente Virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows
venv\Scripts\activate
# Linux/Mac  
source venv/bin/activate
```

#### 3️⃣ Instalar Dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4️⃣ Executar a Aplicação
```bash
# Modo desenvolvimento (com reload)
uvicorn run:app --reload --host 0.0.0.0 --port 8000

# Modo produção
uvicorn run:app --host 0.0.0.0 --port 8000
```

#### 5️⃣ Acessar a API
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **Health Check**: [http://localhost:8000/healthz](http://localhost:8000/healthz)


---

## 🧪 Testes e Validação

### 🌐 Testes Manuais da API

#### Health Check
```bash
curl -X GET "https://vitidata-api.onrender.com/healthz"
```

#### Dados de Produção
```bash
curl -X GET "https://vitidata-api.onrender.com/producao" \
  -H "accept: application/json"
```

#### Usando Python
```python
import requests

# Testar endpoint de produção
response = requests.get("https://vitidata-api.onrender.com/producao")
data = response.json()
print(f"Status: {response.status_code}")
print(f"Records: {len(data.get('data', []))}")
```

---

# 🗂️ Estrutura do Projeto

```
VITIDATA_DF.../
├── 📁 app/
│   ├── 📁 __pycache__/
│   │   └── 📄 __init__.cpython-313.pyc
│   └── 📁 routes/
│       ├── 📁 __pycache__/
│       └── 📄 routes.py
├── 📁 schemas/
│   └── 📄 vinho.py
├── 📁 scraper/
│   ├── 📄 __init__.py
│   ├── 📄 comercializacao.py
│   ├── 📄 exportacao.py
│   ├── 📄 importacao.py
│   ├── 📄 processamento.py
│   └── 📄 producao.py
├── 📁 static/
│   ├── 📄 __init__.py
│   ├── 📄 auth.py
│   └── 📄 models.py
├── 📄 Dockerfile
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 run.py
```

---

<<<<<<< HEAD
## 🌐 Deploy e Produção

### ☁️ Plataforma de Deploy
A aplicação está hospedada no **Render** com as seguintes configurações:

**URL de Produção**: `https://vitidata-api.onrender.com`

=======
## 👨‍💻 Autores
- Lucas Cardoso de Menezes - rm361695
- Leonardo Capra Mucci - rm363577
- Allyson Vinicius Lourenço de Jesus - rm364208
- Nathan Ballaré Lima - rm364060
>>>>>>> b7e55736661a5c29b800087da45717a71c075cbe
---

## 👨‍💻 Equipe de Desenvolvimento

### 🎓 Desenvolvedores

| Nome | RM | GitHub | LinkedIn |
|------|----|---------|-----------| 
| **Lucas Cardoso de Menezes** | RM361695 | [@luccamenezes](https://github.com/luccamenezes) | [LinkedIn](https://linkedin.com/in/luccamenezes) |
| **Leonardo Capra Mucci** | RM363577 | [@leonardocapra](https://github.com/leonardocapra) | [LinkedIn](https://linkedin.com/in/leonardocapra) |
| **Allyson Vinicius Lourenço de Jesus** | RM364208 | [@allysonvinicius](https://github.com/allysonvinicius) | [LinkedIn](https://linkedin.com/in/allysonvinicius) |
| **Nathan Ballaré Lima** | RM364060 | [@nathanballare](https://github.com/nathanballare) | [LinkedIn](https://linkedin.com/in/nathanballare) |

### 🏫 Instituição
**FIAP - Faculdade de Informática e Administração Paulista**  
**Curso**: Pós-Tech em Machine Learning Engineering  
**Disciplina**: Tech Challenge - Fase 1

---



## 📜 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes completos.

```
MIT License

Copyright (c) 2024 VitiData Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```


---


<div align="center">


**[⬆ Voltar ao topo](#-vitidata-api---sistema-de-análise-de-dados-vitivinícolas)**

</div>
