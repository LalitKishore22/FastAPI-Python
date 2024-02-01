from pydantic import BaseModel, Field, EmailStr
import uuid
from typing import Optional

class usermodel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4,alias="_id")
    name: str = Field()
    age: int = Field(ge=20,le=60)
    ph_no: str = Field(min_length=10)
    email: EmailStr = Field()

class updatemodel(BaseModel):
    name: str | None = None
    age: int | None = Field(default=None,ge=20,le=60)
    ph_no: str = Field(min_length=10,max_length=10)
    email: EmailStr | None = None

class deletemodel(BaseModel):
    ph_no: str = Field(min_length=10,max_length=10)