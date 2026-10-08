from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.demande import Demande


T = TypeVar("T", bound="DemandeListe")


@_attrs_define
class DemandeListe:
    """
    Attributes:
        data (list[Demande] | None):
    """

    data: list[Demande] | None

    def to_dict(self) -> dict[str, Any]:
        data: list[dict[str, Any]] | None
        if isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)

        else:
            data = self.data

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.demande import Demande

        d = dict(src_dict)

        def _parse_data(data: object) -> list[Demande] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in _data_type_0:
                    data_type_0_item = Demande.from_dict(data_type_0_item_data)

                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Demande] | None, data)

        data = _parse_data(d.pop("data"))

        demande_liste = cls(
            data=data,
        )

        return demande_liste
