from pydantic import BaseModel, Field, ConfigDict, field_validator


class TokenModel(BaseModel):
    access_token: str = Field(...,
                            title="Access Token",
                            description="Токен доступу, який використовується для авторизації",
                            example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJz"
                            )
    token_type: str = "Bearer"

    @field_validator("access_token")
    @classmethod
    def validate_access_token(cls, value: str) -> str:
        if not value:
            raise ValueError("Access token не може бути порожнім")
        return value
