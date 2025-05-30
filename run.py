from fastapi import FastAPI
from app.scraper import (
    scrape_producao_pages,
    scrape_exportacao,
    scrape_all_processamento,
    scrape_importacao,
    scrape_comercializacao_page
)
from app.routes import routes  

app = FastAPI(title="VitiData API")

app.include_router(routes.router)  

@app.get("/healthz")
def health():
    return {"status": "OK"}

@app.get("/producao")
def producao():
    return scrape_producao_pages()

@app.get("/exportacao")
def exportacao():
    return scrape_exportacao()

@app.get("/processamento")
def processamento():
    return scrape_all_processamento()

@app.get("/importacao")
def importacao():
    return scrape_importacao()

@app.get("/comercializacao")
def comercializacao():
    return scrape_comercializacao_page()
