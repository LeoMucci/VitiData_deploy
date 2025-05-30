from fastapi import FastAPI
from typing import List
from app.scraper import (
    scrape_producao_pages,
    scrape_exportacao,
    scrape_all_processamento,
    scrape_importacao,
    scrape_comercializacao_page
)
from app.routes import routes
from app.schemas.vinho import ComercioEntrada  # usado para todos os retornos

app = FastAPI(title="VitiData API")

app.include_router(routes.router)

@app.get("/healthz", summary="Health Check", description="Verifica se a API está no ar.")
def health():
    return {"status": "OK"}

@app.get("/producao", response_model=List[ComercioEntrada], summary="Dados de Produção", description="Retorna dados da aba 'Produção'.")
def producao():
    return scrape_producao_pages()

@app.get("/exportacao", response_model=List[ComercioEntrada], summary="Dados de Exportação", description="Retorna dados da aba 'Exportação'.")
def exportacao():
    return scrape_exportacao()

@app.get("/processamento", response_model=List[ComercioEntrada], summary="Dados de Processamento", description="Retorna dados da aba 'Processamento'.")
def processamento():
    return scrape_all_processamento()

@app.get("/importacao", response_model=List[ComercioEntrada], summary="Dados de Importação", description="Retorna dados da aba 'Importação'.")
def importacao():
    return scrape_importacao()

@app.get("/comercializacao", response_model=List[ComercioEntrada], summary="Dados de Comercialização", description="Retorna dados da aba 'Comercialização'.")
def comercializacao():
    return scrape_comercializacao_page()
