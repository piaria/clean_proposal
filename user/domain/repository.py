from abc import ABC, abstractmethod

from user.domain.entities import UserEntity


class UserRepository(ABC):
    @abstractmethod
    def get_names(self, pk: int) -> UserEntity:
        """Get user full name."""
