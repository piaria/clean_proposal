from user.domain.repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def get_full_name(self, pk: int) -> str:
        user_entity = self._repository.get_names(pk)
        return f"{user_entity.first_name} {user_entity.last_name}"
