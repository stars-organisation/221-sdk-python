from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.projet import Projet


T = TypeVar("T", bound="ProjetListe")


@_attrs_define
class ProjetListe:
    """
    Attributes:
        data (list[Projet] | None):
        limit (int):
    """

    data: list[Projet] | None
    limit: int

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | None
        if isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
                "limit": limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.projet import Projet

        d = dict(src_dict)

        def _parse_data(data: object) -> list[Projet] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = Projet.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Projet] | None, data)

        data = _parse_data(d.pop("data"))

        limit = d.pop("limit")

        projet_liste = cls(
            data=data,
            limit=limit,
        )

        return projet_liste
