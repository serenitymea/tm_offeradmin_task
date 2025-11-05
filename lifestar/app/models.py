from sqlalchemy import Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .db import Base


class OfferWall(Base):
    __tablename__ = "admin_panel_offerwall"

    token: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    url: Mapped[str | None] = mapped_column(String(200), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    offer_assignments: Mapped[list["OfferWallOffer"]] = relationship(
        "OfferWallOffer",
        back_populates="offer_wall",
        order_by="OfferWallOffer.order",
        lazy="selectin",
    )
    popup_assignments: Mapped[list["OfferWallPopupOffer"]] = relationship(
        "OfferWallPopupOffer",
        back_populates="offer_wall",
        order_by="OfferWallPopupOffer.order",
        lazy="selectin",
    )


class Offer(Base):
    __tablename__ = "admin_panel_offer"

    uuid: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True)
    id: Mapped[int] = mapped_column(Integer, nullable=False)
    url: Mapped[str | None] = mapped_column(String(200), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    sum_to: Mapped[str | None] = mapped_column(String(255), nullable=True)
    term_to: Mapped[int | None] = mapped_column(Integer, nullable=True)
    percent_rate: Mapped[int | None] = mapped_column(Integer, nullable=True)

    wall_assignments: Mapped[list["OfferWallOffer"]] = relationship(
        "OfferWallOffer", back_populates="offer"
    )
    popup_assignments: Mapped[list["OfferWallPopupOffer"]] = relationship(
        "OfferWallPopupOffer", back_populates="offer"
    )


class OfferWallOffer(Base):
    __tablename__ = "admin_panel_offerwalloffer"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    offer_wall_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("admin_panel_offerwall.token"),
        nullable=False,
    )
    offer_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("admin_panel_offer.uuid"), nullable=False
    )
    order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    offer_wall: Mapped["OfferWall"] = relationship(
        "OfferWall", back_populates="offer_assignments"
    )
    offer: Mapped["Offer"] = relationship(
        "Offer", back_populates="wall_assignments", lazy="selectin"
    )


class OfferWallPopupOffer(Base):
    __tablename__ = "admin_panel_offerwallpopupoffer"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    offer_wall_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("admin_panel_offerwall.token"),
        nullable=False,
    )
    offer_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("admin_panel_offer.uuid"), nullable=False
    )
    order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    offer_wall: Mapped["OfferWall"] = relationship(
        "OfferWall", back_populates="popup_assignments"
    )
    offer: Mapped["Offer"] = relationship(
        "Offer", back_populates="popup_assignments", lazy="selectin"
    )