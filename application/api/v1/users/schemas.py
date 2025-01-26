from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    username: str


class UserSchema(UserBaseSchema):
    id: int


class UserCreateSchema(UserBaseSchema):
    pass
