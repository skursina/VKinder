from api.client import VKClient

import random


class VKMessageAPI:
    def __init__(self, client: VKClient):
        self.client = client

    def send_message(self, peer_id: int, text: str, keyboard: str | None = None, attachments: list[str] | None = None) -> None:
        params = {
            "peer_id": peer_id,
            "message": text,
            "random_id": random.randint(1, 2_000_000_000),
        }
        if keyboard:
            params["keyboard"] = keyboard
        if attachments:
            params["attachment"] = ",".join(attachments)
            
        self.client.call_method("messages.send", params)
