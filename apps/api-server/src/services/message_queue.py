from fastapi import Request
from src.settings import settings
import aio_pika
import json

from src.types.insight import InsightRequest


async def create_queue_connection() -> aio_pika.RobustConnection:
    print('THIS IS A TEST', settings.rabbitmq_default_pass, settings.rabbitmq_default_user, settings.rabbitmq_default_vhost)
    return await aio_pika.connect_robust(
        host=settings.rabbitmq_default_vhost,
        login=settings.rabbitmq_default_user,
        password=settings.rabbitmq_default_pass,
    )

async def get_queue_connection(request: Request) -> aio_pika.RobustConnection:
    return request.app.queue_connection

async def publish_task(connection: aio_pika.RobustConnection, payload: InsightRequest) -> bool:
    channel = await connection.channel()
    queue = await channel.declare_queue(settings.insight_message_queue, durable=True)
    await channel.default_exchange.publish(
        message=aio_pika.Message(
            body=json.dumps(payload.model_dump()).encode(),
            content_type='application/json',
            delivery_mode=aio_pika.DeliveryMode.PERSISTENT
        ),
        routing_key=queue.name
    )
    return True