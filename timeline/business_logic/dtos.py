from dataclasses import dataclass

from message.business_logic.dtos import MessageDetailDTO
from user import UserDetailDTO


@dataclass(init=True)
class TimelineEntryDTO:
    message: MessageDetailDTO
    user: UserDetailDTO
