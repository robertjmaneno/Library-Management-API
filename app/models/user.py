from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class User(SQLModel, table=True):
    id : Optional[int] = Field(default=True,  primary_key=True)
    first_name: str = Field(max_length=50, index=True)
    last_name: str = Field(max_length=50, index=True)
    email: str = Field(unique=True, index=True)
    password: str 
    confirm_password: str 


