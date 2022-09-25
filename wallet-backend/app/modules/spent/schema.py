from fastapi_camelcase import CamelModel
from typing import List, Optional


class GetSpentSchema(CamelModel):
    uuid: str = "236f00dea2c34db9b719410482c7655a"
    div: str = "Despesas Fixas"
    lemmatized: str = "despes fix"
    haveChildren: bool = True
    is_raiz: bool = True
    base: bool = True


class GetSubSpendingSchema(CamelModel):
    spent: GetSpentSchema
    sub_spending: Optional[List[GetSpentSchema]]
