from dataclasses import dataclass


@dataclass(init=True)
class UserDetailDTO:
    id: int
    first_name: str
    last_name: str
