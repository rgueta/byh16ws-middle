import asyncio
from datetime import datetime

import websockets


async def handler(ws):
    print(f"📲 App conectada {datetime.now().strftime('%Y%m%d_%H%M%S')}")
    async for msg in ws:
        print("➡️ Comando recibido:", msg)

        # Aquí mandas el comando al SIM800L
        # ejemplo: send_to_sim800(msg)

        await ws.send("OK")


async def main():
    async with websockets.serve(handler, "0.0.0.0", 9000):
        print("🚀 WebSocket listo en puerto 9000")
        await asyncio.Future()


asyncio.run(main())
