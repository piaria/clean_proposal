from itertools import groupby
from message.business_logic.dtos import MessageDetailDTO
from message.business_logic.units_of_work import get_messages
from timeline.business_logic.dtos import TimelineEntryDTO
from user import UserDetailDTO
from user import get_users_by_id


def get_timeline():

    messages = get_messages()
    users_id = set(map(lambda message: message.user_id, messages))
    users = get_users_by_id(users_id)
    users_by_id = dict(groupby(users, key=lambda user: user.id))

    return [__convert_entry_to_dto(message, users) for message in messages]


def __convert_entry_to_dto(message, users):
    user = list(filter(lambda user: message.user_id == user.id, users))[0]
    return TimelineEntryDTO(
        message=MessageDetailDTO(
            id=message.id,
            text=message.text,
            timestamp=message.timestamp,
            user_id=message.user_id,
        ),
        user=UserDetailDTO(
            first_name=user.first_name, last_name=user.last_name, id=user.id
        ),
    )
