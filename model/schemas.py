from pydantic import BaseModel, Field, EmailStr
from util.sanitization import SanitizedString, StrictString

class UserInput(BaseModel):
    # STRICT: "admin; DROP TABLE" -> "admin DROP TABLE"
    username: StrictString = Field(..., min_length=3, max_length=50)
    
    email: EmailStr
    
    # PERMISSIVE: "I love coding;" remains "I love coding;"
    # But "<script>" is removed.
    bio: SanitizedString = Field(default="", max_length=300) 

class APIResponse(BaseModel):
    message: str
    data: dict | None = None