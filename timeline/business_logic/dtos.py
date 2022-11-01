from dataclasses import dataclass

from message.business_logic.dtos import MessageDetailDTO
from user.adapter.logic.dtos import UserDetailDTO


@dataclass(init=True)
class TimelineEntryDTO:
    message: MessageDetailDTO
    user: UserDetailDTO
