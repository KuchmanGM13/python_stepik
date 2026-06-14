import numpy as np

from pydantic import BaseModel, Field, EmailStr


#Day 1 of learning pydantic and dictionary
user = {
    "name": "Alice",
    "age": 30,  
    "email": 'alice@example.com'
}

class User(BaseModel):
    name: str = Field(..., description="The name of the user")
    age: int = Field(..., description="The age of the user", ge=0, le=120)
    email: EmailStr = Field(..., description="The email address of the user")

user = User(**user)
print(user) 