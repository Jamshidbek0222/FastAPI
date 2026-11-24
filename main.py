# API

# FastApi
# print("Hello")

from fastapi import FastAPI
from pydantic import BaseModel, Field

# Field - bu busines standartlar(masalan ism qisqa yoki uzun bo'lib ketmasligi)
# Ellipses degani ham bor ekan. bu 3 ta nuqta ekan. bu degani malumot kiritilishi shart degani

app = FastAPI()


class User(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(gt=0, lt=150)
    is_active: bool = True
    
    # ge - greater or equal
    # le - lesser or equal
    
f1 = User(name="Vali", age=25)
print(f1)
# f2 = User(name="Vali", age=-25) #bunda error beradi
# print(f2)
    
# user = User(name="Otabek", age=25, is_active=True)
# print(user)    
# user = User(name="Otabek", age="Yigirma besh", is_active=True)   #Error beradi
# print(user) 
user = User(name="Otabek", age="25", is_active=True)   #Lekin bu ko'rinishda ishlashiga pydantic aqli yetadi
print(user)
print(user.age)
print(type(user.age)) 
    
    
@app.get("/")
def read_root():
    return {"Hello: learner"}

@app.get("/items/item_id")
def read_item(item_id: int, q:str | None = None):
    return {"item_id": item_id, "q": q}



class Product(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    description: str = Field(default="Tavsif yo'q", max_length=500)
    
p1 = Product(name="Phone", price = 1500)
print(p1.description)





# Serialization - serializatsiya
# Deserialization - deserializatsiya

# JSON


# user = User(name = "Ali", age = 24)  #Pydantic object
# data = user.model_dump()   #Python object  - V2 Pydantic
# print(data)

user = User(name = "Ali", age = 24)  #Pydantic object
data = user.model_dump_json()   # JSON string
print(data)