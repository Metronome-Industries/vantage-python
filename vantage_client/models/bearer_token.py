from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BearerToken")


@_attrs_define
class BearerToken:
    """
    Attributes:
        description (Union[Unset, str]): The user supplied description of this BearerToken
        created_at (Union[Unset, str]): The date and time, in UTC, the BearerToken was created. ISO 8601 Formatted.
            Example: 2023-08-04T00:00:00Z.
        scope (Union[Unset, list[str]]): The scopes applied to the BearerToken used to authenticate this request.
    """

    description: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    scope: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        created_at = self.created_at

        scope: Union[Unset, list[str]] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        created_at = d.pop("created_at", UNSET)

        scope = cast(list[str], d.pop("scope", UNSET))

        bearer_token = cls(
            description=description,
            created_at=created_at,
            scope=scope,
        )

        bearer_token.additional_properties = d
        return bearer_token

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
