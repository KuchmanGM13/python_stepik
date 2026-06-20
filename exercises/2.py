from fastapi import FastAPI

from pydantic import BaseModel, Field, EmailStr, ConfigDict

#https://www.youtube.com/watch?v=zTSRygNQ_Fw
#Day 1 of learning pydantic and dictionary


app = FastAPI()


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


data = {
    "email": "abc@example.com",
    "bio" : None,
    "age": 25
}

data_wo_age = {
    "email": "cab@example.com",
    "bio" : None,
    "gender": "female",
    "birthday": "1998-01-01"
}



class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=1000, description="A short biography of the user")

    #model_config = ConfigDict(extra="forbid")
 
user = []

@app.post("/users")
def add_user(user: UserSchema):
    user.append(user)
    return {"ok": True, "message": "User added successfully"}


@app.get("/users")
def get_users():
    return user


class UserAgeSchema(UserSchema):
    age: int = Field(ge=0, le=120, description="The age of the user")\
    
user1 = UserAgeSchema(**data)
print(repr(user1))    

user2 = UserSchema(**data_wo_age)
print(repr(user2))