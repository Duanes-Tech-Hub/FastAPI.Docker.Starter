from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # 1. Variables from your uploaded .env files
    TEST_VARIABLE: str = "default_value"

    # 2. App settings (with defaults for safety)
    APP_NAME: str = "ProductionAPI"
    DEBUG: bool = False
    VERSION: str = "1.0.0"
    
    # Rate Limiting
    DEFAULT_RATE_LIMIT: str = "100/minute"
    
    # Security: PROXY_IP is critical for Rate Limiting.
    # If not set in your .env.production, we default to localhost
    # but you should update this to your Nginx container IP in prod.
    PROXY_IP: str = "127.0.0.1" 

    # We remove the hardcoded 'env_file' argument because Docker 
    # injects these as system environment variables.
    model_config = SettingsConfigDict(extra="ignore")

settings = Settings()