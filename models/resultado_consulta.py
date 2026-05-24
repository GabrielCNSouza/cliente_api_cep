from dataclasses import dataclass
from models.endereco import Endereco


@dataclass
class ResultadoConsulta:
    dados: Endereco | None
    erro: str | None