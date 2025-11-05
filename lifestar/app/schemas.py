from uuid import UUID
from pydantic import BaseModel, ConfigDict


class OfferSchema(BaseModel):
    """Offer"""

    uuid: UUID
    id: int
    url: str | None
    is_active: bool
    name: str
    sum_to: str | None
    term_to: int | None
    percent_rate: int | None

    model_config = ConfigDict(from_attributes=True)


class OfferWallOfferSchema(BaseModel):
    """OfferWallOffer"""

    offer: OfferSchema

    model_config = ConfigDict(from_attributes=True)


class OfferWallPopupOfferSchema(BaseModel):
    """OfferWallPopupOffer"""

    offer: OfferSchema

    model_config = ConfigDict(from_attributes=True)


class OfferWallSchema(BaseModel):
    """OfferWall"""

    token: UUID
    name: str | None
    url: str | None
    description: str | None
    offer_assignments: list[OfferWallOfferSchema]
    popup_assignments: list[OfferWallPopupOfferSchema]

    model_config = ConfigDict(from_attributes=True)


class OfferNamesResponse(BaseModel):
    """get_offer_names"""

    offer_names: list[str]