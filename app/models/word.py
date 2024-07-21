from pydantic import BaseModel

from app.models.IPA import IPA


class Word(BaseModel):
    word: str
    ipas: list[IPA]
