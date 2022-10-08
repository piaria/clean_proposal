from dataclasses import dataclass
from datetime import datetime


@dataclass(init=True)
class MessageDetailDTO:
    id: int
    user_id: int
    text: int
    timestamp: datetime


@dataclass(init=True)
class MessageCreationDTO:
    user_id: int
    text: int
