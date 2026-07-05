import json
import os


class Bookmarks:

    def __init__(self):
        self.file = "astra/data/bookmarks.json"

        os.makedirs("astra/data", exist_ok=True)

        if not os.path.exists(self.file):
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def get_all(self):
        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def add(self, title, url):
        bookmarks = self.get_all()

        for bookmark in bookmarks:
            if bookmark["url"] == url:
                return

        bookmarks.append({
            "title": title,
            "url": url
        })

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(bookmarks, f, indent=4, ensure_ascii=False)

    def remove(self, url):
        bookmarks = [
            b for b in self.get_all()
            if b["url"] != url
        ]

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(bookmarks, f, indent=4, ensure_ascii=False)