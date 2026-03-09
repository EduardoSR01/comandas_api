#EDUARDO DA SILVA RAMOS

from decimal import Decimal
from pydantic import BaseModel
from typing import Optional

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    descricao: str
    foto: Optional[bytes] = None
    valor_unitario: Decimal