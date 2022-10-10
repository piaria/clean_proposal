from user.business_logic.dtos import UserDetailDTO, UserCreatedData

from ..models import User


def get_users():

    users = User.objects.all()

    return [__convert_user_to_dto(user) for user in users]


def get_user_by_id(id: int):
    user = User.objects.get(pk=id)

    return __convert_user_to_dto(user)


def get_users_by_id(ids: list[int]):
    users = User.objects.filter(id__in=ids)

    return __convert_users_to_dto(users)


def create_user(*, first_name: str, last_name: str):
    user = User.objects.create(first_name=first_name, last_name=last_name)
    return UserCreatedData.from_orm(user)


def __convert_users_to_dto(users: list[User]):
    return [__convert_user_to_dto(user) for user in users]


def __convert_user_to_dto(user: User) -> UserDetailDTO:
    return UserDetailDTO(
        first_name=user.first_name, last_name=user.last_name, id=user.id
    )
