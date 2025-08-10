from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, status

from app.db.users.models import User
from app.pydantic_models.users import UserModel


async def get_user(user_id: str, db: AsyncSession) -> Optional[User]:
    query = select(User).filter_by(id=user_id)
    return await db.scalar(query)


async def sign_up(user_model: UserModel, db: AsyncSession) -> None:
    user = User(**user_model.model_dump())
    db.add(user)
    await db.commit()


async def sign_in(username: str, password: str, db: AsyncSession) -> str:
    user = await db.scalar(select(User).where(User.username == username))
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Користувач не знайдений")
    
    token = user.get_token(password)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Невірний пароль")

    return token

