import aio_pika
import asyncio

RABBIT_URL = "amqp://guest:guest@localhost/"

async def on_message(message: aio_pika.IncomingMessage):
    async with message.process():
        print(f"🟢 [x] Получено сообщение: {message.body.decode()}")

async def main():
    connection = await aio_pika.connect_robust(RABBIT_URL)
    channel = await connection.channel()
    queue = await channel.declare_queue("my_queue", durable=True)
    await queue.consume(on_message)
    print("👂 Слушаю очередь... Нажми CTRL+C для выхода.")
    await asyncio.Future()  # бесконечно слушаем

if __name__ == "__main__":
    asyncio.run(main())
