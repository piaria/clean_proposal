from dataclasses import dataclass
from pydantic import BaseModel


@dataclass(init=True)
class UserDetailDTO:
    id: int
    first_name: str
    last_name: str


class UserData(BaseModel):
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class UserCreatedData(UserData):
    id: int

    class Config:
        orm_mode = True
