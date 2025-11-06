from fastapi import APIRouter, Depends, Request
from src.types import insight as insight_types
from src.services import message_queue as message_queue_services

router = APIRouter(prefix="/insight", tags=["insight"])


@router.post("")
async def offload_insight_task(
    request: insight_types.InsightRequest,
    connection = Depends(message_queue_services.get_queue_connection)
) -> None:
    await message_queue_services.publish_task(
        connection=connection,
        payload=request
    )