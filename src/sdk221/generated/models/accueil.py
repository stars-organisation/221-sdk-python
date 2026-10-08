from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.accueil_answers import AccueilAnswers
    from ..models.accueil_questions import AccueilQuestions


T = TypeVar("T", bound="Accueil")


@_attrs_define
class Accueil:
    """
    Attributes:
        answers (AccueilAnswers):
        finished (bool):
        questions (AccueilQuestions):
    """

    answers: AccueilAnswers
    finished: bool
    questions: AccueilQuestions

    def to_dict(self) -> dict[str, Any]:
        answers = self.answers.to_dict()

        finished = self.finished

        questions = self.questions.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "answers": answers,
                "finished": finished,
                "questions": questions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.accueil_answers import AccueilAnswers
        from ..models.accueil_questions import AccueilQuestions

        d = dict(src_dict)
        answers = AccueilAnswers.from_dict(d.pop("answers"))

        finished = d.pop("finished")

        questions = AccueilQuestions.from_dict(d.pop("questions"))

        accueil = cls(
            answers=answers,
            finished=finished,
            questions=questions,
        )

        return accueil
