from pydantic import BaseModel, Field
from typing import Optional, List

class Register_User(BaseModel):
    email:str=Field(...,pattern="^[a-zA-Z0-9._%#+-]+@gmail\\.com$")
    name:str=Field(...)
    age:int=Field(...,ge=18)
    password:str=Field(...,min_length=8,max_length=16)

class Login_User(BaseModel):
    email:str=Field(...,pattern="^[a-zA-Z0-9._%#+-]+@gmail\\.com$")
    password:str=Field(...,min_length=8,max_length=16)

class UserChat(BaseModel):
    message:str

class Message(BaseModel):
    role:str
    content:str

class ChatRequest(BaseModel):
    messages: List[Message]
