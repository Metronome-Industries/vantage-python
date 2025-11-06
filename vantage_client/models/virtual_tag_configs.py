from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_tag_config import VirtualTagConfig


T = TypeVar("T", bound="VirtualTagConfigs")


@_attrs_define
class VirtualTagConfigs:
    """VirtualTagConfigs model

    Attributes:
        virtual_tag_configs (list[VirtualTagConfig] | Unset):
    """

    virtual_tag_configs: list[VirtualTagConfig] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_tag_configs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.virtual_tag_configs, Unset):
            virtual_tag_configs = []
            for virtual_tag_configs_item_data in self.virtual_tag_configs:
                virtual_tag_configs_item = virtual_tag_configs_item_data.to_dict()
                virtual_tag_configs.append(virtual_tag_configs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if virtual_tag_configs is not UNSET:
            field_dict["virtual_tag_configs"] = virtual_tag_configs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.virtual_tag_config import VirtualTagConfig

        d = dict(src_dict)
        _virtual_tag_configs = d.pop("virtual_tag_configs", UNSET)
        virtual_tag_configs: list[VirtualTagConfig] | Unset = UNSET
        if _virtual_tag_configs is not UNSET:
            virtual_tag_configs = []
            for virtual_tag_configs_item_data in _virtual_tag_configs:
                virtual_tag_configs_item = VirtualTagConfig.from_dict(virtual_tag_configs_item_data)

                virtual_tag_configs.append(virtual_tag_configs_item)

        virtual_tag_configs = cls(
            virtual_tag_configs=virtual_tag_configs,
        )

        virtual_tag_configs.additional_properties = d
        return virtual_tag_configs

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
