from fastapi import FastAPI

from app.core.cambridge import CambridgeDictScraper

app = FastAPI()


@app.get("/word/{word}")
def read_item(word: str):
    return CambridgeDictScraper().get_ipa(word)
