from pydantic import BaseModel, Field, ConfigDict, field_validator


class UserModel(BaseModel):
    username: str = Field(...,
                    title="Ім'я користувача",
                    description="Унікальне ім'я користувача для входу в систему",
                    max_length=50,
                    min_length=3,
                    example="user123"
                    )                  
    email: str = Field(...,
                    title="Email користувача", 
                    description="Email адреса користувача для реєстрації та відновлення пароля",
                    max_length=100,
                    min_length=5,
                     example="namesurname@gmail.com"
                    )
    password: str = Field(...,
                    title="Пароль користувача",
                    description="Пароль для входу в систему, повинен містити не менше 8 символів",
                    min_length=8,
                    example="password123"
                    )
    
    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        if len(value) < 3 or len(value) > 50:
            raise ValueError("Ім'я користувача повинно бути від 3 до 50 символів")
        return value


class UserModelResponse(BaseModel):
    id: str = Field(...,
                    title="ID користувача",
                    description="Унікальний ідентифікатор користувача",
                    example="user_12345"
                    ) 
    username: str = Field(...,
                    title="Ім'я користувача",
                    description="Унікальне ім'я користувача для входу в систему",
                    max_length=50,
                    min_length=3,
                    example="user123"
                    )
    email: str = Field(...,
                    title="Email користувача", 
                    description="Email адреса користувача для реєстрації та відновлення пароля",
                    max_length=100,
                    min_length=5,
                    example="namesurname@gmail.com"
                    )
    is_active: bool = Field(...,
                    title="Активність користувача",
                    description="Показує, чи активний користувач",
                    example=True
                    )
    
    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if "@" not in value or "." not in value:
            raise ValueError("Email повинен містити '@' та '.'")
        return value
