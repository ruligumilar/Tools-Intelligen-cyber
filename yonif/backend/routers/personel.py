from fastapi import APIRouter, Depends, HTTPException, status
from dependencies import require_role	
from sqlalchemy.orm import Session

from database import get_db
from models import Personel
from schemas import PersonelCreate, PersonelResponse
from dependencies import get_current_user


router = APIRouter(
    prefix="/api/personel",
    tags=["Personel"],
)


@router.post(
    "/",
    response_model=PersonelResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_personel(
    data: PersonelCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_role("admin", "operator")
    ),
):
    existing = (
        db.query(Personel)
        .filter(Personel.nrp == data.nrp)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="NRP sudah terdaftar",
        )

    personel = Personel(**data.model_dump())

    db.add(personel)
    db.commit()
    db.refresh(personel)

    return personel


@router.get(
    "/",
    response_model=list[PersonelResponse],
)
def get_personel(
    db: Session = Depends(get_db),
    current_user=Depends(
        require_role("admin", "operator", "viewer")
    ),
):
    return (
        db.query(Personel)
        .order_by(Personel.id)
        .all()
    )


@router.get(
    "/{personel_id}",
    response_model=PersonelResponse,
)
def get_personel_by_id(
    personel_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_role("admin", "operator", "viewer")
    ),
):
    personel = (
        db.query(Personel)
        .filter(Personel.id == personel_id)
        .first()
    )

    if not personel:
        raise HTTPException(
            status_code=404,
            detail="Personel tidak ditemukan",
        )

    return personel


@router.put(
    "/{personel_id}",
    response_model=PersonelResponse,
)
def update_personel(
    personel_id: int,
    data: PersonelCreate,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_role("admin", "operator")
    ),
):
    personel = (
        db.query(Personel)
        .filter(Personel.id == personel_id)
        .first()
    )

    if not personel:
        raise HTTPException(
            status_code=404,
            detail="Personel tidak ditemukan",
        )

    existing = (
        db.query(Personel)
        .filter(
            Personel.nrp == data.nrp,
            Personel.id != personel_id,
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="NRP sudah digunakan personel lain",
        )

    for field, value in data.model_dump().items():
        setattr(personel, field, value)

    db.commit()
    db.refresh(personel)

    return personel


@router.delete(
    "/{personel_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_personel(
    personel_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        require_role("admin")
    ),
):
    personel = (
        db.query(Personel)
        .filter(Personel.id == personel_id)
        .first()
    )

    if not personel:
        raise HTTPException(
            status_code=404,
            detail="Personel tidak ditemukan",
        )

    db.delete(personel)
    db.commit()