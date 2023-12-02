from pydantic import BaseModel


class MlRequest(BaseModel):
    description: str


class MlResponse(BaseModel):
    economy: str
    business_model: str
    competitors: str
    development_plan: str
    team: str
    value_proposition: str

