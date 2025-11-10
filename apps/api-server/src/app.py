from typing import AsyncGenerator
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.services import message_queue as message_queue_services
from src.routes import blob_storage as blob_storage_routes
from src.routes import insight as insight_routes


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    queue_connection = await message_queue_services.create_queue_connection()
    app.state.queue_connection = queue_connection
    app.state.queue_channel = queue_connection.channel()
    yield
    await app.state.queue_connection.close()


app = FastAPI(lifespan=lifespan)

app.include_router(blob_storage_routes.router)
app.include_router(insight_routes.router)
