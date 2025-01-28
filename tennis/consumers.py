import json
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import aiohttp

class TennisConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.room_group_name = f'tennis_{self.game_id}'

        # Join the group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        pass  # Клиент ничего не отправляет

    async def send_event_update(self, event):
        await self.send(text_data=json.dumps(event))

    async def fetch_event_details(self):
        api_url = f"https://bookiesapi.com/api/get.php?login=smarketsup&token=35824-8BSMVjWJPi12T1R&task=eventdata&game_id={self.game_id}"
        while True:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(api_url) as response:
                        if response.status == 200:
                            data = await response.json()
                            await self.channel_layer.group_send(
                                self.room_group_name,
                                {
                                    'type': 'send_event_update',
                                    'event': data
                                }
                            )
            except Exception as e:
                print(f"Ошибка при обновлении данных: {e}")

            await asyncio.sleep(2)  # Пауза между запросами

    async def send_event_update(self, event):
        await self.send(text_data=json.dumps(event['event']))
