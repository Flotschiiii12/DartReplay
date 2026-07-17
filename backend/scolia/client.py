import asyncio
import json
import websockets
import psycopg2

from config import SERIAL_NUMBER, ACCESS_TOKEN


async def main():

    while True:

        connection = None

        try:

            connection = psycopg2.connect(
                host="localhost",
                database="dartreplay",
                user="dartreplay",
                password="dartreplay123"
            )

            cursor = connection.cursor()

            websocket_url = (
                f"wss://game.scoliadarts.com/api/v1/social"
                f"?serialNumber={SERIAL_NUMBER}"
                f"&accessToken={ACCESS_TOKEN}"
            )

            print(websocket_url)
            print("Verbinde zu SCOLIA...")

            async with websockets.connect(websocket_url) as websocket:

                print("✅ Verbunden!")

                while True:

                    message = await websocket.recv()

                    data = json.loads(message)

                    print(data)

                    if data.get("type") == "THROW_DETECTED":

                        payload = data["payload"]

                        cursor.execute(
                            """
                            INSERT INTO throws
                            (
                                sector,
                                x,
                                y,
                                bounceout,
                                detection_time
                            )
                            VALUES
                            (
                                %s,
                                %s,
                                %s,
                                %s,
                                %s
                            )
                            """,
                            (
                                payload["sector"],
                                payload["coordinates"][0],
                                payload["coordinates"][1],
                                payload["bounceout"],
                                payload["detectionTime"]
                            )
                        )

                        connection.commit()

                        print("✅ Wurf gespeichert")

        except Exception as e:

            print(f"❌ SCOLIA ERROR: {e}")
            print("🔄 Reconnect in 5 Sekunden...")

            try:
                if connection:
                    connection.close()
            except Exception:
                pass

            await asyncio.sleep(5)


asyncio.run(main())
