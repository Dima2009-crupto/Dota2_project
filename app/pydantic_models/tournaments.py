from pydantic import BaseModel, Field, ConfigDict, field_validator

from app.db.tournaments.db_actions import Vote
from app.db.tournaments.models import Tournament
from app.db.teams.models import Team


class TournamentModel(BaseModel):
    name: str = Field(...,
                        title="Назва турніру",
                        description="Назва турніру, яка буде відображатися в інтерфейсі",
                        max_length=100,
                        min_length=1,
                        example="Ea Sports Tournament"
                    )
    exp_days: int = Field(7,
                        title="Кількість днів для турніру",
                        description="Кількість днів, протягом яких буде проходити турнір",
                        ge=1,
                        le=30,
                        example=7
                        )
    description: str = Field(...,
                        title="Опис турніру",
                        description="Опис турніру, який буде відображатися в інтерфейсі",
                        max_length=500,
                        min_length=1,
                        example="Цей турнір присвячений грі FIFA 24"
                        )
    
    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if len(value) < 1 or len(value) > 100:
            raise ValueError("Назва турніру повинна бути від 1 до 100 символів")
        return value


class TournamentModelResponse(BaseModel):
    id: str = Field(...,
                    title="ID турніру",
                    description="Унікальний ідентифікатор турніру",
                    example="tournament_12345"
                    )
    
    @field_validator("id")
    @classmethod
    def validate_id(cls, value: str) -> str:
        if not value.startswith("tournament_"):
            raise ValueError("ID турніру повинен починатися з 'tournament_'")
        return value


class VoteModel(BaseModel):
    team_id: str = Field(...,
                        title="ID команди",
                        description="ID команди, яка голосує",
                        example="team_12345"
                        )
    tournament_id: str = Field(...,
                        title="ID турніру",
                        description="ID турніру, в якому команда голосує",
                        example="tournament_12345",
                        )
    
    vote: Vote = Field(...,
                        title="Голос",
                        description="Голос команди в турнірі",
                        )
    
    @field_validator("team_id")
    @classmethod
    def validate_team_id(cls, value: str) -> str:
        if not value.startswith("team_"):
            raise ValueError("ID команди повинен починатися з 'team_'")
        return value


class ResultModel(BaseModel):
    team_name: str = Field(...,
                           title="Назва команди",
                           description="Назва команди, яка додає результат",
                           max_length=100,
                           min_length=1,
                           example="Team A"
                           )
    tournament_name: str = Field(...,
                            title="Назва турніру",
                            description="Назва турніру, в якому команда додає результат",
                            max_length=100,
                            min_length=1,
                            example="Ea Sports Tournament"
                            )
    result: float = Field(...,
                            title="Результат",
                            description="Результат команди в турнірі",
                            ge=0.0,
                            le=100.0,
                            example=85.5
                            )
    vote_result: int = Field(...,
                             title="Результат голосування",
                            description="Результат голосування команди в турнірі",
                            ge=0,
                            le=100,
                            example=75
                            )
    
    @field_validator("team_name")
    @classmethod
    def validate_team_name(cls, value: str) -> str:
        if len(value) < 1 or len(value) > 100:
            raise ValueError("Назва команди повинна бути від 1 до 100 символів")
        return value