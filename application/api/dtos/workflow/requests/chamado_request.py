from pydantic import BaseModel

class ChamadoRequest(BaseModel):
    id: int
    titulo: str
    descricao: str
    responsavel_id: int