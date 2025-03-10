from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TagValue")


@_attrs_define
class TagValue:
    """
    Attributes:
        tag_value (Union[Unset, str]): The TagValue. Example: vantage.
        providers (Union[Unset, str]): The unique providers that are covered by the TagValue.
    """

    tag_value: Union[Unset, str] = UNSET
    providers: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_value = self.tag_value

        providers = self.providers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag_value is not UNSET:
            field_dict["tag_value"] = tag_value
        if providers is not UNSET:
            field_dict["providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        tag_value = d.pop("tag_value", UNSET)

        providers = d.pop("providers", UNSET)

        tag_value = cls(
            tag_value=tag_value,
            providers=providers,
        )

        tag_value.additional_properties = d
        return tag_value

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
