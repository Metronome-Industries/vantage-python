from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Tag")


@_attrs_define
class Tag:
    """Tag model

    Attributes:
        tag_key (Union[Unset, str]): The Tag key. Example: aws:createdBy.
        hidden (Union[Unset, bool]): Whether the Tag has been hidden from the Vantage UI.
        providers (Union[Unset, str]): The unique providers that are covered by the Tag key.
    """

    tag_key: Union[Unset, str] = UNSET
    hidden: Union[Unset, bool] = UNSET
    providers: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_key = self.tag_key

        hidden = self.hidden

        providers = self.providers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag_key is not UNSET:
            field_dict["tag_key"] = tag_key
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if providers is not UNSET:
            field_dict["providers"] = providers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        tag_key = d.pop("tag_key", UNSET)

        hidden = d.pop("hidden", UNSET)

        providers = d.pop("providers", UNSET)

        tag = cls(
            tag_key=tag_key,
            hidden=hidden,
            providers=providers,
        )

        tag.additional_properties = d
        return tag

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
