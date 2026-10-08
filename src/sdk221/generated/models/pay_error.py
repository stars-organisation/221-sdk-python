from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.pay_error_code import PayErrorCode
from ..models.pay_error_kyc_status import PayErrorKycStatus
from ..models.pay_error_limit_type import PayErrorLimitType
from ..models.pay_error_merchant_status import PayErrorMerchantStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pay_error_fields import PayErrorFields


T = TypeVar("T", bound="PayError")


@_attrs_define
class PayError:
    """
    Attributes:
        code (PayErrorCode): Code applicatif stable. La liste des codes possibles est donnée par chaque réponse
            d'erreur.
        message (str): Message lisible, en français ou en anglais selon ?lang ou Accept-Language.
        request_id (UUID): Identifiant de la requête, aussi dans l'en-tête X-Request-Id : à donner au support.
        fields (PayErrorFields | Unset): Un message par champ refusé du corps de la requête.
        gateway_mode (str | Unset): PAYMENTS_UNAVAILABLE : raison pour le mode demandé (not_wired : pas de fournisseur
            branché).
        kyc_status (PayErrorKycStatus | Unset): KYC_REQUIRED : état de la vérification d'identité.
        limit (int | Unset): MERCHANT_LIMIT_EXCEEDED : valeur du plafond en XOF.
        limit_type (PayErrorLimitType | Unset): MERCHANT_LIMIT_EXCEEDED : plafond atteint.
        merchant_status (PayErrorMerchantStatus | Unset): MERCHANT_SUSPENDED : état du compte.
        missing (list[str] | Unset): MISSING_CAPTURES : photos encore à envoyer.
    """

    code: PayErrorCode
    message: str
    request_id: UUID
    fields: PayErrorFields | Unset = UNSET
    gateway_mode: str | Unset = UNSET
    kyc_status: PayErrorKycStatus | Unset = UNSET
    limit: int | Unset = UNSET
    limit_type: PayErrorLimitType | Unset = UNSET
    merchant_status: PayErrorMerchantStatus | Unset = UNSET
    missing: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        code = self.code.value

        message = self.message

        request_id = str(self.request_id)

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        gateway_mode = self.gateway_mode

        kyc_status: str | Unset = UNSET
        if not isinstance(self.kyc_status, Unset):
            kyc_status = self.kyc_status.value

        limit = self.limit

        limit_type: str | Unset = UNSET
        if not isinstance(self.limit_type, Unset):
            limit_type = self.limit_type.value

        merchant_status: str | Unset = UNSET
        if not isinstance(self.merchant_status, Unset):
            merchant_status = self.merchant_status.value

        missing: list[str] | Unset = UNSET
        if not isinstance(self.missing, Unset):
            missing = self.missing

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "message": message,
                "request_id": request_id,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields
        if gateway_mode is not UNSET:
            field_dict["gateway_mode"] = gateway_mode
        if kyc_status is not UNSET:
            field_dict["kyc_status"] = kyc_status
        if limit is not UNSET:
            field_dict["limit"] = limit
        if limit_type is not UNSET:
            field_dict["limit_type"] = limit_type
        if merchant_status is not UNSET:
            field_dict["merchant_status"] = merchant_status
        if missing is not UNSET:
            field_dict["missing"] = missing

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pay_error_fields import PayErrorFields

        d = dict(src_dict)
        code = PayErrorCode(d.pop("code"))

        message = d.pop("message")

        request_id = UUID(d.pop("request_id"))

        _fields = d.pop("fields", UNSET)
        fields: PayErrorFields | Unset
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = PayErrorFields.from_dict(_fields)

        gateway_mode = d.pop("gateway_mode", UNSET)

        _kyc_status = d.pop("kyc_status", UNSET)
        kyc_status: PayErrorKycStatus | Unset
        if isinstance(_kyc_status, Unset):
            kyc_status = UNSET
        else:
            kyc_status = PayErrorKycStatus(_kyc_status)

        limit = d.pop("limit", UNSET)

        _limit_type = d.pop("limit_type", UNSET)
        limit_type: PayErrorLimitType | Unset
        if isinstance(_limit_type, Unset):
            limit_type = UNSET
        else:
            limit_type = PayErrorLimitType(_limit_type)

        _merchant_status = d.pop("merchant_status", UNSET)
        merchant_status: PayErrorMerchantStatus | Unset
        if isinstance(_merchant_status, Unset):
            merchant_status = UNSET
        else:
            merchant_status = PayErrorMerchantStatus(_merchant_status)

        missing = cast(list[str], d.pop("missing", UNSET))

        pay_error = cls(
            code=code,
            message=message,
            request_id=request_id,
            fields=fields,
            gateway_mode=gateway_mode,
            kyc_status=kyc_status,
            limit=limit,
            limit_type=limit_type,
            merchant_status=merchant_status,
            missing=missing,
        )

        return pay_error
