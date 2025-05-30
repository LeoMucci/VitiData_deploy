from fastapi import APIRouter, Request
from app.schemas.vinho import VinhoEntrada
from pydantic import ValidationError
from app.state.validados import dados_validados

router = APIRouter()

@router.post("/vinhos")
async def receber_vinho(request: Request):
    payload = await request.json()
    try:
        vinho = VinhoEntrada(**payload)
        return {"status": "ok", "data": vinho.dict()}
    except ValidationError as e:
        return {"status": "erro", "detalhes": e.errors()}

@router.get("/dados-validos")
def get_dados_validados():
    retorno = {}
    for chave, lista in dados_validados.items():
        retorno[chave] = [item.dict() for item in lista]
    return retorno
