# 🐇 FastAPI + RabbitMQ Microservice Demo

<p align="center">
  <img src="https://media.giphy.com/media/voKRB2g96S8q4/giphy.gif?cid=ecf05e47728gvo6ysapuqfoo35ruyu93w11oy12nsa1zfrtl&ep=v1_gifs_search&rid=giphy.gif&ct=g" width="500" />
</p>

A simple microservice setup using FastAPI and RabbitMQ, designed to demonstrate how to publish and consume messages in a clean, async Python architecture.

---

## 📦 Architecture

```
[FastAPI API] --> [RabbitMQ Queue] --> [Async Worker Consumer]
```

- `sender/` – FastAPI app that sends messages to RabbitMQ  
- `worker/` – Async consumer that listens for messages and processes them  
- `mobile/my-rn-app/` – React Native app that sends messages to the API  
- `docker-compose.yml` – Runs RabbitMQ locally  

---

## ⚙️ Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [aio-pika](https://aio-pika.readthedocs.io/)
- [RabbitMQ](https://www.rabbitmq.com/)
- [React Native (Expo)](https://docs.expo.dev/)

---

## 🚀 How to Run

### 1. 🐇 Start RabbitMQ

```bash
docker-compose up -d
```

Open RabbitMQ UI: http://localhost:15672  
Login: `guest` / `guest`

### 2. 📨 Run Sender API

```bash
cd sender
source venv/bin/activate
uvicorn main:app --reload
```

Go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Use `/send/` to publish a message to RabbitMQ.

### 3. ⚙️ Run Worker Consumer

```bash
cd worker
source venv/bin/activate
python consumer.py
```

You'll see incoming messages printed in terminal.

### 4. 📱 Launch Mobile App

```bash
cd mobile/my-rn-app
npx expo start
```

Use iOS simulator or Expo Go to open the app and send messages.

---

## 💡 Why RabbitMQ?

- Clean decoupling of producers & consumers
- Async & queue-based logic via `aio-pika`
- Real-world microservice example

---

## 🧑‍💻 Author

[Anatoly Bystrov](https://github.com/AnatolyBystrov)

---

> Built with ❤️ for interviews and production-ready microservices
