from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenClientSecret(BaseModel):
    grant_type: str
    client_id: str
    client_secret: str

class TokenData(BaseModel):
    email: str
