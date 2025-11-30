import bleach
import re
from pydantic import BeforeValidator, GetCoreSchemaHandler
from pydantic_core import core_schema
from typing import Annotated, Optional, Any

def sanitize_text(v: str) -> str:
    """
    XSS PROTECTION:
    Strips HTML tags and cleans whitespace.
    Allows punctuation (semicolons, quotes) for grammar.
    """
    if v is None:
        return v
    
    # bleach.clean removes HTML tags (e.g. <script>). 
    # strip=True removes the content inside tags entirely.
    cleaned = bleach.clean(v, tags=[], strip=True)
    return cleaned.strip()

def sanitize_injection_chars(v: str) -> str:
    """
    INJECTION PROTECTION (Strict):
    Removes characters commonly used in SQL or Command Injection.
    Useful for IDs, Usernames, Keys, etc.
    
    Removes: ; ' " ` -- /* */
    """
    if v is None:
        return v
    
    # 1. Run standard HTML cleaning first
    v = sanitize_text(v)
    
    # 2. Remove specific dangerous characters/patterns
    # Note: This will turn "O'Connor" into "OConnor". 
    # Only use this for fields where punctuation is not expected.
    v = re.sub(r"[;\"'`]", "", v)
    
    # 3. Remove SQL comment sequences
    v = v.replace("--", "").replace("/*", "").replace("*/", "")
    
    return v.strip()

def truncate_to_32(v: str) -> str:
    if isinstance(v, str) and len(v) > 32:
        return v[:32]
    return v

def truncate_string(value: Optional[str], min_length: Optional[int] = None, max_length: Optional[int] = None) -> Optional[str]:
    """
    Enforce length constraints on a string.
    - Returns None if value is shorter than min_length
    - Truncates if longer than max_length
    """
    if not value or not isinstance(value, str):
        return value
    
    # Check minimum length
    if min_length is not None and len(value) < min_length:
        return None
    
    # Truncate if exceeds maximum
    if max_length is not None and len(value) > max_length:
        return value[:max_length]
    
    return value

# Type 1: Safe for Bios, Comments, Descriptions (Allows grammar, blocks XSS)
SanitizedString = Annotated[str, BeforeValidator(sanitize_text)]

# Type 2: Safe for Usernames, IDs, Codes (Blocks XSS + SQLi chars)
StrictString = Annotated[str, BeforeValidator(sanitize_injection_chars)]

# Type 3: String truncated to max 32 characters for transaction IDs
TruncatedStr32 = Annotated[str, BeforeValidator(truncate_to_32)]