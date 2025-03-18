from configuration import Configuration
from pydantic import BaseModel, Field
from typing import List, Optional

class Usuario(BaseModel):
    id: int
    nome: str
    email: str

class Chamado(BaseModel):
    id: int = Field(description="Identificador do chamado")
    titulo: str
    descricao: str
    responsavel: Optional[Usuario] = Field(description="Responsável pelo chamado", default=None)

@Configuration.app.get("/chamados", tags=["Chamados"], response_model=List[Chamado], description="Retorna a lista de chamados")
async def chamados():
    retorno = [
        Chamado(id=1, titulo="Chamado 1", descricao="Descrição do chamado 1"),
        Chamado(id=2, titulo="Chamado 2", descricao="Descrição do chamado 2")
    ]
    return retorno