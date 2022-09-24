from app.modules.spent.repository import SpentNodeRepository
from app.modules.spent.schema import GetSpentSchema
from app.modules.user.repository import UserRepository, UserNodeRepository


class GetSourceSpendingService:
    def __init__(self, user_id: int):
        self._user_id = user_id
        self._repository = UserRepository()
        self._graph_spent_repository = SpentNodeRepository()
        self._graph_user_repository = UserNodeRepository()

    async def _serializer(self, source_spending: list):
        return [GetSpentSchema(**spent.__dict__) for spent in source_spending]

    async def execute(self):
        user = await self._repository.get_by_id(self._user_id)
        user_node = await self._graph_user_repository.filter_by_email(user.email)
        source_spending = await self._graph_spent_repository.filter_source_spending(
            user_node
        )
        return await self._serializer(source_spending)
