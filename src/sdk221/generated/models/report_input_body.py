from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.report_input_body_lang import ReportInputBodyLang
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportInputBody")


@_attrs_define
class ReportInputBody:
    """
    Attributes:
        current_value (str): 1 à 500 caractères, publié dans l’issue GitHub.
        dataset (str): Identifiant du jeu (fiche /donnees/<id>/), ou « autre » pour une fiche de l’annuaire ou une
            démarche.
        email (str): Pour l’accusé et la décision. Jamais publié ; supprimé 30 jours après la décision.
        expected_value (str): 1 à 500 caractères, publié dans l’issue GitHub.
        place (str): 1 à 200 caractères, publié dans l’issue GitHub.
        source (str): 1 à 500 caractères ; seul champ qui accepte un lien.
        turnstile_token (str): Jeton Cloudflare Turnstile du widget du formulaire.
        lang (ReportInputBodyLang | Unset): Langue des e-mails. Default: ReportInputBodyLang.FR.
        version (str | Unset):
    """

    current_value: str
    dataset: str
    email: str
    expected_value: str
    place: str
    source: str
    turnstile_token: str
    lang: ReportInputBodyLang | Unset = ReportInputBodyLang.FR
    version: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        current_value = self.current_value

        dataset = self.dataset

        email = self.email

        expected_value = self.expected_value

        place = self.place

        source = self.source

        turnstile_token = self.turnstile_token

        lang: str | Unset = UNSET
        if not isinstance(self.lang, Unset):
            lang = self.lang.value

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "current_value": current_value,
                "dataset": dataset,
                "email": email,
                "expected_value": expected_value,
                "place": place,
                "source": source,
                "turnstile_token": turnstile_token,
            }
        )
        if lang is not UNSET:
            field_dict["lang"] = lang
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        current_value = d.pop("current_value")

        dataset = d.pop("dataset")

        email = d.pop("email")

        expected_value = d.pop("expected_value")

        place = d.pop("place")

        source = d.pop("source")

        turnstile_token = d.pop("turnstile_token")

        _lang = d.pop("lang", UNSET)
        lang: ReportInputBodyLang | Unset
        if isinstance(_lang, Unset):
            lang = UNSET
        else:
            lang = ReportInputBodyLang(_lang)

        version = d.pop("version", UNSET)

        report_input_body = cls(
            current_value=current_value,
            dataset=dataset,
            email=email,
            expected_value=expected_value,
            place=place,
            source=source,
            turnstile_token=turnstile_token,
            lang=lang,
            version=version,
        )

        return report_input_body
