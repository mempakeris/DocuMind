from fastapi import APIRouter, Depends, Request, Response
from src.database import get_session
from src.models.user import User
from src.types import insight as insight_types
from src.services import message_queue as message_queue_services
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import uuid4

router = APIRouter(prefix="/insight", tags=["insight"])


@router.post("")
async def offload_insight_task(
    request: insight_types.InsightRequest,
    connection=Depends(message_queue_services.get_queue_connection),
) -> None:
    await message_queue_services.publish_task(connection=connection, payload=request)


# TODO: This will be removed and only used for testing at the moment.
@router.post("/user")
async def create_user(session: AsyncSession = Depends(get_session)):
    user = User(account_id=uuid4(), email="test@test.com")
    session.add(user)
    await session.commit()
    return Response(status_code=201)
