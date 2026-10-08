from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="Compteur")


@_attrs_define
class Compteur:
    """
    Attributes:
        jeu (str):
        ouvertures (int): Ouvertures de la page du jeu.
        telechargements (int): Fichiers téléchargés depuis le hub.
    """

    jeu: str
    ouvertures: int
    telechargements: int

    def to_dict(self) -> dict[str, Any]:
        jeu = self.jeu

        ouvertures = self.ouvertures

        telechargements = self.telechargements

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "jeu": jeu,
                "ouvertures": ouvertures,
                "telechargements": telechargements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        jeu = d.pop("jeu")

        ouvertures = d.pop("ouvertures")

        telechargements = d.pop("telechargements")

        compteur = cls(
            jeu=jeu,
            ouvertures=ouvertures,
            telechargements=telechargements,
        )

        return compteur
