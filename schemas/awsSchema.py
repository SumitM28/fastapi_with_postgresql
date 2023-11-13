from pydantic import BaseModel
class Tenant(BaseModel):
    cost:int
    month:str
    tenantName:str
    owner:str
    Department:str
    costCenter:str
    another_cost:float
    Forecasted:str

class Costs(BaseModel):
    azure: float
    gcp: float
    aws: float
