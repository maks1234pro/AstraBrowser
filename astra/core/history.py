import json
import os


class History:

    def __init__(self):
        self.file = "astra/data/history.json"

        os.makedirs("astra/data", exist_ok=True)

        if not os.path.exists(self.file):
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def get_all(self):
        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def add(self, title, url):
        history = self.get_all()

        history.insert(0, {
            "title": title,
            "url": url
        })

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4, ensure_ascii=False)

    def clear(self):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump([], f)