from fastapi import APIRouter, Depends, status
from fastapi_pagination import paginate, Page

from app.modules.core.logging import LoggingUnder
from app.modules.spent import schema, usecase


router = APIRouter()


@router.get(
    "/source/{user_id}",
    description="Router to get user spending source.",
    response_model=Page[schema.GetSpentSchema],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(LoggingUnder())],
)
async def get_user_spending_source(user_id: int):
    spending = await usecase.GetSourceSpendingService(user_id).execute()
    return paginate(spending)
