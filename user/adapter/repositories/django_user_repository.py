from user import UserEntity
from user import UserRepository
from user import User


class DjangoUserRepository(UserRepository):
    def get_names(self, pk: int) -> UserEntity:
        """Get user full name."""

        user = User.objects.get(pk=pk)
        return UserEntity(
            first_name=user.first_name,
            last_name=user.last_name,
        )
