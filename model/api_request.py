from pydantic import BaseModel,constr
from typing import List, Optional


class ApiRequestModel(BaseModel):
	batchid: constr(min_length=6)
	payload: Optional[List[List[int]]] = None

