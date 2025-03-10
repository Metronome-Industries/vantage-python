from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tag_value import TagValue


T = TypeVar("T", bound="TagValues")


@_attrs_define
class TagValues:
    """TagValues model

    Attributes:
        tag_values (Union[Unset, list['TagValue']]):
    """

    tag_values: Union[Unset, list["TagValue"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tag_values, Unset):
            tag_values = []
            for tag_values_item_data in self.tag_values:
                tag_values_item = tag_values_item_data.to_dict()
                tag_values.append(tag_values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tag_values is not UNSET:
            field_dict["tag_values"] = tag_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.tag_value import TagValue

        d = src_dict.copy()
        tag_values = []
        _tag_values = d.pop("tag_values", UNSET)
        for tag_values_item_data in _tag_values or []:
            tag_values_item = TagValue.from_dict(tag_values_item_data)

            tag_values.append(tag_values_item)

        tag_values = cls(
            tag_values=tag_values,
        )

        tag_values.additional_properties = d
        return tag_values

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
