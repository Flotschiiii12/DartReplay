
import asyncio
import websockets

from config import SERIAL_NUMBER, ACCESS_TOKEN


async def main():
    websocket_url = (
        f"wss://game.scoliadarts.com/api/v1/social"
        f"?serialNumber={SERIAL_NUMBER}"
        f"&accessToken={ACCESS_TOKEN}"
    )

    print("Verbinde mit:")
    print(websocket_url)

    async with websockets.connect(websocket_url) as websocket:
        print("Verbunden!")

        while True:
            message = await websocket.recv()
            print(message)


asyncio.run(main())
