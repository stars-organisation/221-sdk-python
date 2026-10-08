from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.lieu_resume import LieuResume
    from ..models.recognised import Recognised


T = TypeVar("T", bound="AdresseNormalisee")


@_attrs_define
class AdresseNormalisee:
    """
    Attributes:
        alternatives (list[LieuResume] | None):
        ambigu (bool):
        lieu (LieuResume | None):
        lieu_id (None | str):
        lieux_reconnus (list[Recognised] | None):
        limites (str):
        relation (None | str): en_face_de, derriere, a_cote_de ou pres_de ; null si aucune relation n'est reconnue.
        repere (None | str):
        texte (str):
    """

    alternatives: list[LieuResume] | None
    ambigu: bool
    lieu: LieuResume | None
    lieu_id: None | str
    lieux_reconnus: list[Recognised] | None
    limites: str
    relation: None | str
    repere: None | str
    texte: str

    def to_dict(self) -> dict[str, Any]:
        from ..models.lieu_resume import LieuResume

        alternatives: list[dict[str, Any]] | None
        if isinstance(self.alternatives, list):
            alternatives = []
            for alternatives_type_0_item_data in self.alternatives:
                alternatives_type_0_item = alternatives_type_0_item_data.to_dict()
                alternatives.append(alternatives_type_0_item)

        else:
            alternatives = self.alternatives

        ambigu = self.ambigu

        lieu: dict[str, Any] | None
        if isinstance(self.lieu, LieuResume):
            lieu = self.lieu.to_dict()
        else:
            lieu = self.lieu

        lieu_id: None | str
        lieu_id = self.lieu_id

        lieux_reconnus: list[dict[str, Any]] | None
        if isinstance(self.lieux_reconnus, list):
            lieux_reconnus = []
            for lieux_reconnus_type_0_item_data in self.lieux_reconnus:
                lieux_reconnus_type_0_item = lieux_reconnus_type_0_item_data.to_dict()
                lieux_reconnus.append(lieux_reconnus_type_0_item)

        else:
            lieux_reconnus = self.lieux_reconnus

        limites = self.limites

        relation: None | str
        relation = self.relation

        repere: None | str
        repere = self.repere

        texte = self.texte

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "alternatives": alternatives,
                "ambigu": ambigu,
                "lieu": lieu,
                "lieu_id": lieu_id,
                "lieux_reconnus": lieux_reconnus,
                "limites": limites,
                "relation": relation,
                "repere": repere,
                "texte": texte,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lieu_resume import LieuResume
        from ..models.recognised import Recognised

        d = dict(src_dict)

        def _parse_alternatives(data: object) -> list[LieuResume] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alternatives_type_0 = []
                _alternatives_type_0 = data
                for alternatives_type_0_item_data in _alternatives_type_0:
                    alternatives_type_0_item = LieuResume.from_dict(
                        alternatives_type_0_item_data
                    )

                    alternatives_type_0.append(alternatives_type_0_item)

                return alternatives_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LieuResume] | None, data)

        alternatives = _parse_alternatives(d.pop("alternatives"))

        ambigu = d.pop("ambigu")

        def _parse_lieu(data: object) -> LieuResume | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lieu_type_0 = LieuResume.from_dict(data)

                return lieu_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LieuResume | None, data)

        lieu = _parse_lieu(d.pop("lieu"))

        def _parse_lieu_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        lieu_id = _parse_lieu_id(d.pop("lieu_id"))

        def _parse_lieux_reconnus(data: object) -> list[Recognised] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                lieux_reconnus_type_0 = []
                _lieux_reconnus_type_0 = data
                for lieux_reconnus_type_0_item_data in _lieux_reconnus_type_0:
                    lieux_reconnus_type_0_item = Recognised.from_dict(
                        lieux_reconnus_type_0_item_data
                    )

                    lieux_reconnus_type_0.append(lieux_reconnus_type_0_item)

                return lieux_reconnus_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Recognised] | None, data)

        lieux_reconnus = _parse_lieux_reconnus(d.pop("lieux_reconnus"))

        limites = d.pop("limites")

        def _parse_relation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        relation = _parse_relation(d.pop("relation"))

        def _parse_repere(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        repere = _parse_repere(d.pop("repere"))

        texte = d.pop("texte")

        adresse_normalisee = cls(
            alternatives=alternatives,
            ambigu=ambigu,
            lieu=lieu,
            lieu_id=lieu_id,
            lieux_reconnus=lieux_reconnus,
            limites=limites,
            relation=relation,
            repere=repere,
            texte=texte,
        )

        return adresse_normalisee
