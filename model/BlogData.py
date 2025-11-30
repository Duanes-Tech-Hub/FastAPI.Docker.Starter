from pydantic import BaseModel, Field, field_validator
from typing import Any, Optional
from util.sanitization import SanitizedString, StrictString,truncate_string

class BlogData(BaseModel):
    title: StrictString = Field(..., min_length=1, max_length=200)
    description: SanitizedString = Field(..., max_length=1000)
    content: SanitizedString = Field(..., max_length=100000)
    tags: StrictString = Field(..., min_length=1, max_length=100)
    author: StrictString = Field(..., min_length=1, max_length=100)

    @field_validator('title', 'description', 'tags', 'author', mode='before')
    @classmethod
    def enforce_length(cls, v: Any, info: Any) -> Optional[str]:
        """Apply truncation based on field constraints."""
        field_constraints = cls.model_fields.get(info.field_name)
        if not field_constraints:
            return v
        
        min_len = getattr(field_constraints, 'min_length', None)
        max_len = getattr(field_constraints, 'max_length', None)
        
        return truncate_string(v, min_len, max_len)