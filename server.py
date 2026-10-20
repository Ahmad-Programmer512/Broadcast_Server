import asyncio, websockets, sys


clients = set()

async def broadcast(websocket):
    clients.add(websocket)
    print(f"Client connected! Total clients: {len(clients)}")

    try:
        async for message in websocket:
            print(f"Message received: {message}")

            for client in clients.copy():
                if client != websocket:
                    await client.send(message)
    
    except websockets.exceptions.ConnectionClosed:
        pass

    finally:
        clients.discard(websocket)
        print(f"Client disconnected! Total clients: {len(clients)}")

async def main():
    async with websockets.serve(broadcast, "localhost", 8765):
        print("Broadcast server is running on port 8765")
        await asyncio.Future()

if sys.argv[2] == "start":
    asyncio.run(main())