from app.modules.core.abstract_models import BaseRepository
from app.modules.core.graph_models import User as UserNode
from app.modules.user.model import User


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.entity = User

    async def get_by_email(self, email: str) -> [dict, None]:
        return await self.entity.get_or_none(email=email)


class UserNodeRepository:
    async def create(self, payload: dict):
        user_node = UserNode(**payload)
        user_node.save()
        return user_node

    async def filter_by_email(self, email: str):
        return UserNode().nodes.filter(email=email).get()
