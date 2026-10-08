from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.payout_quote_delay import PayoutQuoteDelay
from ..models.payout_quote_destination_type import PayoutQuoteDestinationType
from ..models.payout_quote_rail import PayoutQuoteRail
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payout_debit import PayoutDebit


T = TypeVar("T", bound="PayoutQuote")


@_attrs_define
class PayoutQuote:
    """
    Attributes:
        amount (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        destination_id (UUID):
        expires_at (datetime.datetime):
        fee (str): Montant en francs CFA entiers (XOF), écrit en chaîne de chiffres, sans espace ni décimale.
        livemode (bool): true : objet du mode live ; false : mode test.
        net (str): Montant reçu sur le numéro ou le compte.
        quote_hash (str): À renvoyer dans POST /v1/payouts : à usage unique, valable jusqu'à expires_at.
        debits (list[PayoutDebit] | Unset): Virement bancaire : part débitée de chaque solde (sn_wave, sn_orange), au
            prorata. EN: bank transfer: the part taken from each balance, pro rata.
        delay (PayoutQuoteDelay | Unset): Virement bancaire : traité à la main, 3 à 5 jours ouvrés. EN: bank transfer:
            processed by hand in 3 to 5 business days.
        destination_type (PayoutQuoteDestinationType | Unset): bank : virement vers un compte bancaire (absent pour un
            numéro mobile).
        fee_rate (int | Unset): Virement bancaire : taux du palier du montant, en points de base. EN: bank transfer: the
            amount's tier rate, in basis points.
        rail (PayoutQuoteRail | Unset): Numéro mobile seulement.
    """

    amount: str
    destination_id: UUID
    expires_at: datetime.datetime
    fee: str
    livemode: bool
    net: str
    quote_hash: str
    debits: list[PayoutDebit] | Unset = UNSET
    delay: PayoutQuoteDelay | Unset = UNSET
    destination_type: PayoutQuoteDestinationType | Unset = UNSET
    fee_rate: int | Unset = UNSET
    rail: PayoutQuoteRail | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        destination_id = str(self.destination_id)

        expires_at = self.expires_at.isoformat()

        fee = self.fee

        livemode = self.livemode

        net = self.net

        quote_hash = self.quote_hash

        debits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.debits, Unset):
            debits = []
            for debits_item_data in self.debits:
                debits_item = debits_item_data.to_dict()
                debits.append(debits_item)

        delay: str | Unset = UNSET
        if not isinstance(self.delay, Unset):
            delay = self.delay.value

        destination_type: str | Unset = UNSET
        if not isinstance(self.destination_type, Unset):
            destination_type = self.destination_type.value

        fee_rate = self.fee_rate

        rail: str | Unset = UNSET
        if not isinstance(self.rail, Unset):
            rail = self.rail.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "amount": amount,
                "destination_id": destination_id,
                "expires_at": expires_at,
                "fee": fee,
                "livemode": livemode,
                "net": net,
                "quote_hash": quote_hash,
            }
        )
        if debits is not UNSET:
            field_dict["debits"] = debits
        if delay is not UNSET:
            field_dict["delay"] = delay
        if destination_type is not UNSET:
            field_dict["destination_type"] = destination_type
        if fee_rate is not UNSET:
            field_dict["fee_rate"] = fee_rate
        if rail is not UNSET:
            field_dict["rail"] = rail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.payout_debit import PayoutDebit

        d = dict(src_dict)
        amount = d.pop("amount")

        destination_id = UUID(d.pop("destination_id"))

        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        fee = d.pop("fee")

        livemode = d.pop("livemode")

        net = d.pop("net")

        quote_hash = d.pop("quote_hash")

        _debits = d.pop("debits", UNSET)
        debits: list[PayoutDebit] | Unset = UNSET
        if _debits is not UNSET:
            debits = []
            for debits_item_data in _debits:
                debits_item = PayoutDebit.from_dict(debits_item_data)

                debits.append(debits_item)

        _delay = d.pop("delay", UNSET)
        delay: PayoutQuoteDelay | Unset
        if isinstance(_delay, Unset):
            delay = UNSET
        else:
            delay = PayoutQuoteDelay(_delay)

        _destination_type = d.pop("destination_type", UNSET)
        destination_type: PayoutQuoteDestinationType | Unset
        if isinstance(_destination_type, Unset):
            destination_type = UNSET
        else:
            destination_type = PayoutQuoteDestinationType(_destination_type)

        fee_rate = d.pop("fee_rate", UNSET)

        _rail = d.pop("rail", UNSET)
        rail: PayoutQuoteRail | Unset
        if isinstance(_rail, Unset):
            rail = UNSET
        else:
            rail = PayoutQuoteRail(_rail)

        payout_quote = cls(
            amount=amount,
            destination_id=destination_id,
            expires_at=expires_at,
            fee=fee,
            livemode=livemode,
            net=net,
            quote_hash=quote_hash,
            debits=debits,
            delay=delay,
            destination_type=destination_type,
            fee_rate=fee_rate,
            rail=rail,
        )

        return payout_quote
