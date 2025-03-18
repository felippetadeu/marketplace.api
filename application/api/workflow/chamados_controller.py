from configuration import Configuration
from typing import List
from application.api.dtos.workflow.requests.criar_chamado_request import CriarChamadoRequest
from application.api.dtos.workflow.requests.chamado_request import ChamadoRequest


@Configuration.app.get("/chamados", tags=["Chamados"], response_model=List[ChamadoRequest], description="Retorna a lista de chamados")
async def chamados():
    retorno = [
        ChamadoRequest(id=1, titulo="Chamado 1", descricao="Descrição do chamado 1"),
        ChamadoRequest(id=2, titulo="Chamado 2", descricao="Descrição do chamado 2")
    ]
    return retorno

@Configuration.app.post("/chamado", tags=["Chamados"], response_model=ChamadoRequest, description="Retorna o chamado criado")
async def criar_chamados(chamado: CriarChamadoRequest):
    retorno = ChamadoRequest(id=2, titulo=chamado.titulo, descricao=chamado.descricao, responsavel_id=chamado.responsavel_id)
    return retorno