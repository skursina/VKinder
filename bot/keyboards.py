import json


class KeyboardFactory:
    @staticmethod
    def main_menu() -> str:
        return json.dumps(
            {
                "one_time": False,
                "buttons": [
                    [
                        {"action": {"type": "text", "label": "🔍 Найти пару"}, "color": "positive"},
                    ],
                    [
                        {"action": {"type": "text", "label": "📋 Мои избранные"}, "color": "primary"},
                    ],
                ],
            },
            ensure_ascii=False,
        )

    @staticmethod
    def candidate_menu() -> str:
        return json.dumps(
            {
                "one_time": False,
                "buttons": [
                    [
                        {"action": {"type": "text", "label": "➡️ Следующий"}, "color": "primary"},
                        {"action": {"type": "text", "label": "⭐ В избранное"}, "color": "positive"},
                    ],
                    [
                        {"action": {"type": "text", "label": "🚫 В чёрный список"}, "color": "negative"},
                    ],
                ],
            },
            ensure_ascii=False,
        )
