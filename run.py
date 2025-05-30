from flask import Flask, jsonify
from app.scraper import (
    scrape_producao_pages,
    scrape_exportacao,
    scrape_all_processamento,
    scrape_importacao,
    scrape_comercializacao_page
)

app = Flask(__name__)

@app.route('/healthz')
def health():
    return "OK", 200

@app.route('/producao')
def producao():
    dados = scrape_producao_pages()
    return jsonify(dados)

@app.route('/exportacao')
def exportacao():
    dados = scrape_exportacao()
    return jsonify(dados)

@app.route('/processamento')
def processamento():
    dados = scrape_all_processamento()
    return jsonify(dados)

@app.route('/importacao')
def importacao():
    dados = scrape_importacao()
    return jsonify(dados)

@app.route('/comercializacao')
def comercializacao():
    dados = scrape_comercializacao_page()
    return jsonify(dados)

# NÃO usar app.run() aqui — o Docker usará gunicorn para isso
