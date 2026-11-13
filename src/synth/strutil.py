import re
import unicodedata


def slugify(s: str) -> str:
    text = unicodedata.normalize("NFKD", s)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub("[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text
