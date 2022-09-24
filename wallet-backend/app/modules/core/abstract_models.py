from tortoise.exceptions import BaseORMException
from tortoise.models import Model


class BaseRepository:
    def __init__(self):
        self.entity = Model

    async def create(self, payload: dict):
        return await self.entity.create(**payload)

    async def update(self, payload: Model) -> bool:
        try:
            await payload.save()
            return True
        except BaseORMException:
            return False

    async def get_all(self) -> list:
        return await self.entity.all()

    async def get_by_id(self, id: int) -> [dict, None]:
        return await self.entity.get_or_none(id=id)

    async def delete(self, id: int) -> bool:
        try:
            await self.entity.filter(id=id).delete()
            return True
        except BaseORMException:
            return False
