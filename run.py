from fastapi import FastAPI, BackgroundTasks
from typing import List
from app.scraper import (
    scrape_producao_pages,
    scrape_exportacao,
    scrape_all_processamento,
    scrape_importacao,
    scrape_comercializacao_page
)
from app.routes import routes
from app.schemas.vinho import ComercioEntrada, VinhoEntrada
import pandas as pd

app = FastAPI(title="VitiData API")
app.include_router(routes.router)

@app.get("/healthz", summary="Health Check", description="Verifica se a API está no ar.")
def health():
    return {"status": "OK"}

# Função auxiliar para salvar CSV em background
def salvar_csv(nome_arquivo: str, dados: List[dict]):
    df = pd.DataFrame(dados)
    df.to_csv(nome_arquivo, index=False)

@app.get("/producao", response_model=List[VinhoEntrada], summary="Dados de Produção")
def producao(background_tasks: BackgroundTasks):
    dados = scrape_producao_pages()
    background_tasks.add_task(salvar_csv, "dadosProducao.csv", dados)
    return dados

@app.get("/exportacao", response_model=List[ComercioEntrada], summary="Dados de Exportação")
def exportacao(background_tasks: BackgroundTasks):
    dados = scrape_exportacao()
    background_tasks.add_task(salvar_csv, "dadosExportacao.csv", dados)
    return dados

@app.get("/processamento", response_model=List[ComercioEntrada], summary="Dados de Processamento")
def processamento(background_tasks: BackgroundTasks):
    dados = scrape_all_processamento()
    background_tasks.add_task(salvar_csv, "dadosProcessamento.csv", dados)
    return dados

@app.get("/importacao", response_model=List[ComercioEntrada], summary="Dados de Importação")
def importacao(background_tasks: BackgroundTasks):
    dados = scrape_importacao()
    background_tasks.add_task(salvar_csv, "dadosImportacao.csv", dados)
    return dados

@app.get("/comercializacao", response_model=List[ComercioEntrada], summary="Dados de Comercialização")
def comercializacao(background_tasks: BackgroundTasks):
    dados = scrape_comercializacao_page()
    background_tasks.add_task(salvar_csv, "dadosComercializacao.csv", dados)
    return dados
