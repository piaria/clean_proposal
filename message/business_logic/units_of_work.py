from abc import ABC
from django.db import transaction
from message.business_logic.dtos import MessageDetailDTO
from message.business_logic.exceptions import BusinessException, DomainModelNotFound
from message.business_logic.validations import validate_message_creation

from ..models import Message

class UnitOfWork(ABC):
    
    def execute(*args, **kwargs):
        ...
        

class GetMessageUOW(UnitOfWork):        

    def execute(*args, **kwargs):
        messages = Message.objects.all()

        return [__convert_message_to_dto(message) for message in messages]


def get_messages() -> list[MessageDetailDTO]:

    messages = Message.objects.all()

    return [__convert_message_to_dto(message) for message in messages]


@transaction.atomic
def create_message(*, text: str, user_id: int) -> MessageDetailDTO:

    try:
        validate_message_creation(text, user_id)
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
