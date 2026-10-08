from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.type_evenement_product import TypeEvenementProduct

T = TypeVar("T", bound="TypeEvenement")


@_attrs_define
class TypeEvenement:
    """
    Attributes:
        label_en (str):
        label_fr (str):
        product (TypeEvenementProduct):
        type_ (str):
    """

    label_en: str
    label_fr: str
    product: TypeEvenementProduct
    type_: str

    def to_dict(self) -> dict[str, Any]:
        label_en = self.label_en

        label_fr = self.label_fr

        product = self.product.value

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "label_en": label_en,
                "label_fr": label_fr,
                "product": product,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        label_en = d.pop("label_en")

        label_fr = d.pop("label_fr")

        product = TypeEvenementProduct(d.pop("product"))

        type_ = d.pop("type")

        type_evenement = cls(
            label_en=label_en,
            label_fr=label_fr,
            product=product,
            type_=type_,
        )

        return type_evenement
