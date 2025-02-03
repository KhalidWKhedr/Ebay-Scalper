from pydantic import BaseModel, Field


class SchemaConnectionDetails(BaseModel):
    use_ssh: bool = False
    host: str | None = Field(None, title="Database Host")
    port: int | None = Field(None, title="Database Port")
    user: str | None = Field(None, title="Username")
    password: str | None = Field(None, title="Password")
    db_name: str | None = Field(None, title="Database Name")
    auth_source: str | None = Field(None, title="Authentication Source")
    ssh_host: str | None = Field(None, title="SSH Host")
    ssh_port: int | None = Field(None, title="SSH Port")
    ssh_username: str | None = Field(None, title="SSH Username")
    ssh_password: str | None = Field(None, title="SSH Password")
    auth_type: str | None = Field(None, title="Authentication Type")

    class Config:
        validate_assignment = True
