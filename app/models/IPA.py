from pydantic import BaseModel

from app.models.region import Region


class IPA(BaseModel):
    region: Region
    ipas: list[str]
