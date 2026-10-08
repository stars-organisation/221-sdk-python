from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.payments_health import PaymentsHealth


T = TypeVar("T", bound="Health")


@_attrs_define
class Health:
    """
    Attributes:
        control_center_url (str): Tableau de bord des paiements (vide s'il n'est pas configuré).
        database (bool):
        kyc_url (str): Adresse publique de kyc-core que la page de capture sur téléphone appelle (vide si non
            configurée).
        social (list[str] | None): Fournisseurs de connexion configurés ; le hub désactive les autres boutons.
        status (str):
        pay_client_id (str | Unset): Obsolète, toujours absent : le fournisseur OIDC de 221 est supprimé.
        payments (PaymentsHealth | Unset):
    """

    control_center_url: str
    database: bool
    kyc_url: str
    social: list[str] | None
    status: str
    pay_client_id: str | Unset = UNSET
    payments: PaymentsHealth | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        control_center_url = self.control_center_url

        database = self.database

        kyc_url = self.kyc_url

        social: list[str] | None
        if isinstance(self.social, list):
            social = self.social

        else:
            social = self.social

        status = self.status

        pay_client_id = self.pay_client_id

        payments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payments, Unset):
            payments = self.payments.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "control_center_url": control_center_url,
                "database": database,
                "kyc_url": kyc_url,
                "social": social,
                "status": status,
            }
        )
        if pay_client_id is not UNSET:
            field_dict["pay_client_id"] = pay_client_id
        if payments is not UNSET:
            field_dict["payments"] = payments

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.payments_health import PaymentsHealth

        d = dict(src_dict)
        control_center_url = d.pop("control_center_url")

        database = d.pop("database")

        kyc_url = d.pop("kyc_url")

        def _parse_social(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                social_type_0 = cast(list[str], data)

                return social_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        social = _parse_social(d.pop("social"))

        status = d.pop("status")

        pay_client_id = d.pop("pay_client_id", UNSET)

        _payments = d.pop("payments", UNSET)
        payments: PaymentsHealth | Unset
        if isinstance(_payments, Unset):
            payments = UNSET
        else:
            payments = PaymentsHealth.from_dict(_payments)

        health = cls(
            control_center_url=control_center_url,
            database=database,
            kyc_url=kyc_url,
            social=social,
            status=status,
            pay_client_id=pay_client_id,
            payments=payments,
        )

        return health
