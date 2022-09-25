from app.modules.user.repository import UserRepository, UserNodeRepository
from app.modules.spent.schema import GetSpentSchema, GetSubSpendingSchema
from app.modules.spent.repository import SpentNodeRepository


class GetSourceSpendingService:
    def __init__(self, user_id: int):
        self._graph_spent_repository = SpentNodeRepository()
        self._graph_user_repository = UserNodeRepository()
        self._repository = UserRepository()
        self._user_id = user_id

    async def _serializer(self, source_spending: list):
        return [GetSpentSchema(**spent.__dict__) for spent in source_spending]

    async def execute(self):
        user = await self._repository.get_by_id(self._user_id)
        user_node = await self._graph_user_repository.filter_by_email(user.email)
        source_spending = await self._graph_spent_repository.filter_source_spending(
            user_node
        )
        return await self._serializer(source_spending)


class GetSubSpendingService:
    def __init__(self, user_id: int, spent_uuid: str):
        self._graph_spent_repository = SpentNodeRepository()
        self._graph_user_repository = UserNodeRepository()
        self._repository = UserRepository()
        self._spent_uuid = spent_uuid
        self._user_id = user_id

    async def _serializer(self, spent, source_spending: list):
        result = dict(
            spent=spent.__dict__,
            sub_spending=[GetSpentSchema(**spt.__dict__) for spt in source_spending],
        )
        return GetSubSpendingSchema(**result)

    async def execute(self):
        user = await self._repository.get_by_id(self._user_id)
        user_node = await self._graph_user_repository.filter_by_email(user.email)
        spent, source_spending = await self._graph_spent_repository.filter_sub_spending(
            user_node, self._spent_uuid
        )
        return await self._serializer(spent, source_spending)
