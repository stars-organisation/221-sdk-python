from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

T = TypeVar("T", bound="AnswerInputBody")


@_attrs_define
class AnswerInputBody:
    """
    Attributes:
        answer (str):
    """

    answer: str

    def to_dict(self) -> dict[str, Any]:
        answer = self.answer

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "answer": answer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        answer = d.pop("answer")

        answer_input_body = cls(
            answer=answer,
        )

        return answer_input_body
