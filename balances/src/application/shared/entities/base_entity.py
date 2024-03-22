from uuid import uuid4
from datetime import datetime



class BaseEntity:
    """
    Classe base para entidades no domínio.
    """

    def __init__(
        self, id: uuid4 = None, created_at: str = None, updated_at: str = None
    ):
        self._id = id or str(uuid4())
        self._created_at = created_at or datetime.now()
        self._updated_at = updated_at or datetime.now()

    @property
    def id(self) -> str:
        return str(self._id)

    @property
    def created_at(self) -> str:
        return self._created_at

    @created_at.setter
    def created_at(self, created_at: str) -> None:
        self._created_at = created_at

    @property
    def updated_at(self) -> str:
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at: str) -> None:
        self._updated_at = updated_at
