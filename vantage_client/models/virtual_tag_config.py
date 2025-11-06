from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_tag_config_value import VirtualTagConfigValue


T = TypeVar("T", bound="VirtualTagConfig")


@_attrs_define
class VirtualTagConfig:
    """VirtualTagConfig model

    Attributes:
        token (str | Unset): The token of the VirtualTagConfig. Example: vtag_1234.
        created_by_token (str | Unset): The token of the Creator of the VirtualTagConfig. Example: usr_1234.
        key (str | Unset): The key of the VirtualTagConfig. Example: Cost Center.
        overridable (bool | Unset): Whether the VirtualTagConfig can override a provider-supplied tag on a matching
            Cost.
        backfill_until (str | Unset): The earliest month VirtualTagConfig should be backfilled to. Example: 2025-05-01.
        values (list[VirtualTagConfigValue] | Unset): Values for the VirtualTagConfig, with match precedence determined
            by their relative order in the list.
    """

    token: str | Unset = UNSET
    created_by_token: str | Unset = UNSET
    key: str | Unset = UNSET
    overridable: bool | Unset = UNSET
    backfill_until: str | Unset = UNSET
    values: list[VirtualTagConfigValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        created_by_token = self.created_by_token

        key = self.key

        overridable = self.overridable

        backfill_until = self.backfill_until

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if created_by_token is not UNSET:
            field_dict["created_by_token"] = created_by_token
        if key is not UNSET:
            field_dict["key"] = key
        if overridable is not UNSET:
            field_dict["overridable"] = overridable
        if backfill_until is not UNSET:
            field_dict["backfill_until"] = backfill_until
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.virtual_tag_config_value import VirtualTagConfigValue

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        created_by_token = d.pop("created_by_token", UNSET)

        key = d.pop("key", UNSET)

        overridable = d.pop("overridable", UNSET)

        backfill_until = d.pop("backfill_until", UNSET)

        _values = d.pop("values", UNSET)
        values: list[VirtualTagConfigValue] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = VirtualTagConfigValue.from_dict(values_item_data)

                values.append(values_item)

        virtual_tag_config = cls(
            token=token,
            created_by_token=created_by_token,
            key=key,
            overridable=overridable,
            backfill_until=backfill_until,
            values=values,
        )

        virtual_tag_config.additional_properties = d
        return virtual_tag_config

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
