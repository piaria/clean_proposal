from django.db import transaction
from message.business_logic.dtos import MessageDetailDTO
from message.business_logic.exceptions import BusinessException, DomainModelNotFound

from ..models import Message


def get_messages():

    messages = Message.objects.all()

    return [__convert_message_to_dto(message) for message in messages]


@transaction.atomic
def create_message(*, text: str, user_id: int):

    try:
        assert len(text) > 0
        assert user_id
        message = Message.objects.create(text=text, user_id=user_id)
    except:
        raise BusinessException()

    return __convert_message_to_dto(message)


def get_message_by_id(id: int):

    try:
        message = Message.objects.get(pk=id)
    except:
        raise DomainModelNotFound()

    return __convert_message_to_dto(message)


def __convert_message_to_dto(message: Message) -> MessageDetailDTO:
    return MessageDetailDTO(
        id=message.id,
        text=message.text,
        user_id=message.user_id,
        timestamp=message.timestamp,
    )
