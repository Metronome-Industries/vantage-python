from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserFeedback")


@_attrs_define
class UserFeedback:
    """UserFeedback model

    Attributes:
        token (Union[Unset, str]): Token of the feedback
        message (Union[Unset, str]): User feedback message
        created_by_token (Union[Unset, str]): Token of the creator of the feedback
        created_at (Union[Unset, str]): Feedback creation timestamp Example: 2023-01-01T00:00:00Z.
    """

    token: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    created_by_token: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        message = self.message

        created_by_token = self.created_by_token

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if message is not UNSET:
            field_dict["message"] = message
        if created_by_token is not UNSET:
            field_dict["created_by_token"] = created_by_token
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        message = d.pop("message", UNSET)

        created_by_token = d.pop("created_by_token", UNSET)

        created_at = d.pop("created_at", UNSET)

        user_feedback = cls(
            token=token,
            message=message,
            created_by_token=created_by_token,
            created_at=created_at,
        )

        user_feedback.additional_properties = d
        return user_feedback

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
