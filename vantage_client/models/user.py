from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """User model

    Attributes:
        token (Union[Unset, str]):
        name (Union[Unset, str]): The name of the User. Example: John Doe.
        email (Union[Unset, str]): The email of the User. Example: john_doe@acme.com.
        role (Union[Unset, str]): The role of the User. Example: Admin.
        last_seen_at (Union[Unset, str]): The last time the User logged in. Example: 2024-01-01 00:00:00+00:00.
    """

    token: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    role: Union[Unset, str] = UNSET
    last_seen_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        name = self.name

        email = self.email

        role = self.role

        last_seen_at = self.last_seen_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if role is not UNSET:
            field_dict["role"] = role
        if last_seen_at is not UNSET:
            field_dict["last_seen_at"] = last_seen_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        role = d.pop("role", UNSET)

        last_seen_at = d.pop("last_seen_at", UNSET)

        user = cls(
            token=token,
            name=name,
            email=email,
            role=role,
            last_seen_at=last_seen_at,
        )

        user.additional_properties = d
        return user

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
