import asyncio, websockets, sys


async def connect():
    async with websockets.connect("ws://localhost:8765") as websocket:
        print("Connected to server!")

        async def receive_messages():
            async for message in websocket:
                print(f"\nMessage recevied: {message}")

        receiver = asyncio.create_task(receive_messages())
                
        try:
            while True:
                message = await asyncio.to_thread(input, "Enter message: ")
                await websocket.send(message)
        finally:
            receiver.cancel()   

if sys.argv[2] == "connect":
    asyncio.run(connect())