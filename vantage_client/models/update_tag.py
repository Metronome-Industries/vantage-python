from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTag")


@_attrs_define
class UpdateTag:
    """Updates an existing Tag.

    Attributes:
        hidden (bool): Whether the Tag is hidden from the Vantage UI.
        tag_key (Union[Unset, str]):
        tag_keys (Union[Unset, list[str]]):
    """

    hidden: bool
    tag_key: Union[Unset, str] = UNSET
    tag_keys: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hidden = self.hidden

        tag_key = self.tag_key

        tag_keys: Union[Unset, list[str]] = UNSET
        if not isinstance(self.tag_keys, Unset):
            tag_keys = self.tag_keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hidden": hidden,
            }
        )
        if tag_key is not UNSET:
            field_dict["tag_key"] = tag_key
        if tag_keys is not UNSET:
            field_dict["tag_keys"] = tag_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        hidden = d.pop("hidden")

        tag_key = d.pop("tag_key", UNSET)

        tag_keys = cast(list[str], d.pop("tag_keys", UNSET))

        update_tag = cls(
            hidden=hidden,
            tag_key=tag_key,
            tag_keys=tag_keys,
        )

        update_tag.additional_properties = d
        return update_tag

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
