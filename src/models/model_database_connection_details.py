from pydantic import BaseModel, Field


class SchemaConnectionDetails(BaseModel):
    SSH_TOGGLE: bool = False  # Indicates whether SSH is enabled
    MONGO_HOST: str | None = Field(None, title="MongoDB Host")
    MONGO_PORT: str | None = Field(None, title="MongoDB Port")
    MONGO_USER: str | None = Field(None, title="MongoDB Username")
    MONGO_PASSWORD: str | None = Field(None, title="MongoDB Password")
    MONGO_DB_NAME: str | None = Field(None, title="MongoDB Database Name")
    MONGO_AUTH_DB: str | None = Field(None, title="MongoDB Authentication Source")
    SSH_HOST: str | None = Field(None, title="SSH Host")
    SSH_PORT: str | None = Field(None, title="SSH Port")
    SSH_USERNAME: str | None = Field(None, title="SSH Username")
    SSH_PASSWORD: str | None = Field(None, title="SSH Password")
    AUTH_TYPE: str | None = Field(None, title="Authentication Type")

    class Config:
        validate_assignment = True
