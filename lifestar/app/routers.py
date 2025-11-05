from typing import Annotated
from uuid import UUID
from litestar import get
from litestar.di import Provide
from litestar.exceptions import NotFoundException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .db import get_session
from .models import OfferWall
from .schemas import OfferWallSchema, OfferNamesResponse

OFFER_CHOICES = [
    "Loanplus",
    "SgroshiCPA2",
    "Novikredyty",
    "TurboGroshi",
    "Crypsee",
    "Suncredit",
    "Lehko",
    "Monto",
    "Limon",
    "Amigo",
    "FirstCredit",
    "Finsfera",
    "Pango",
    "Treba",
    "StarFin",
    "BitCapital",
    "SgroshiCPL",
    "LoviLave",
    "Prostocredit",
    "Sloncredit",
    "Clickcredit",
    "Credos",
    "Dodam",
    "SelfieCredit",
    "Egroshi",
    "Alexcredit",
    "SgroshiCPA1",
    "Tengo",
    "Credit7",
    "Tpozyka",
    "Creditkasa",
    "Moneyveo",
    "MyCredit",
    "CreditPlus",
    "Miloan",
    "AvansCredit",
]


@get("/api/offerwalls/{token:uuid}/")
async def retrieve_offerwall(
    token: UUID, session: Annotated[AsyncSession, Provide(get_session)]
) -> OfferWallSchema:
    """
    OfferWall token with offers.
    """
    query = select(OfferWall).where(OfferWall.token == token)
    result = await session.execute(query)
    offerwall = result.scalar_one_or_none()

    if not offerwall:
        raise NotFoundException(detail="OfferWall not found")

    return OfferWallSchema.model_validate(offerwall)


@get("/api/offerwalls/get_offer_names/")
async def get_offer_names() -> OfferNamesResponse:
    """
    list of all offer names
    """
    return OfferNamesResponse(offer_names=OFFER_CHOICES)