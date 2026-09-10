from datetime import datetime

from pydantic import BaseModel, ConfigDict


class PersonelBase(BaseModel):
    nrp: str
    nama: str
    pangkat: str | None = None
    korps: str | None = None
    jabatan: str | None = None
    kompi: str | None = None
    status: str = "aktif"


class PersonelCreate(PersonelBase):
    pass


class PersonelResponse(PersonelBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)