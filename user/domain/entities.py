from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class UserEntity:
    first_name: str
    last_name: str
