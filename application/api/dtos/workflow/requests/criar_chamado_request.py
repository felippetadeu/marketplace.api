from pydantic import BaseModel

class CriarChamadoRequest(BaseModel):
    titulo: str
    descricao: str
    responsavel_id: int