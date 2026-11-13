import re


def slugify(s: str) -> str:
    text = s.lower()
    text = re.sub("[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text
