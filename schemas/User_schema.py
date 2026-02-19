from pydantic import BaseModel

class UserSchema(BaseModel):
    email:str
    password:str

class UserUpdateApiKey(BaseModel):
    api_key:str

    