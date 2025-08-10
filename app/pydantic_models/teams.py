from pydantic import BaseModel, Field, ConfigDict, field_validator


class TeamModel(BaseModel):
    name: str = Field(...,
                    title="Назва команди",
                    description="Назва команди, яка буде відображатися в інтерфейсі",
                    max_length=100,
                    min_length=1,
                    example="Team A"
                    ) 
    private: bool = Field(...,
                    title="Приватність команди",
                    description="Приватна команда не буде відображатися в загальному списку команд",
                    example=False
                    )
    
    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if len(value) < 1 or len(value) > 100:
            raise ValueError("Назва команди повинна бути від 1 до 100 символів")
        return value


class TeamModelResponse(TeamModel):
    id: str = Field(...,
                    title="ID команди",
                    description="Унікальний ідентифікатор команди",
                    example="team_2705"
                    )
    
    @field_validator("id")
    @classmethod
    def validate_id(cls, value: str) -> str:
        if not value.startswith("team_"):
            raise ValueError("ID команди повинен починатися з 'team_'")
        return value    