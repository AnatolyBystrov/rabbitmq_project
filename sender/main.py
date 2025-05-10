from fastapi import FastAPI
from pydantic import BaseModel
import aio_pika

app = FastAPI()
RABBIT_URL = "amqp://guest:guest@localhost/"

class MessageBody(BaseModel):
    message: str

@app.on_event("startup")
async def startup():
    app.state.connection = await aio_pika.connect_robust(RABBIT_URL)
    app.state.channel = await app.state.connection.channel()
    await app.state.channel.declare_queue("my_queue", durable=True)

@app.post("/send/")
async def send_message(body: MessageBody):
    await app.state.channel.default_exchange.publish(
        aio_pika.Message(body=body.message.encode()),
        routing_key="my_queue"
    )
    return {"status": "sent", "message": body.message}
