from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_virtual_tag_config_values_item import CreateVirtualTagConfigValuesItem


T = TypeVar("T", bound="CreateVirtualTagConfig")


@_attrs_define
class CreateVirtualTagConfig:
    """Create a new VirtualTagConfig.

    Attributes:
        key (str): The key of the VirtualTagConfig.
        overridable (bool): Whether the VirtualTagConfig can override a provider-supplied tag on a matching Cost.
        backfill_until (datetime.date | Unset): The earliest month the VirtualTagConfig should be backfilled to.
        values (list[CreateVirtualTagConfigValuesItem] | Unset): Values for the VirtualTagConfig, with match precedence
            determined by order in the list.
    """

    key: str
    overridable: bool
    backfill_until: datetime.date | Unset = UNSET
    values: list[CreateVirtualTagConfigValuesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        overridable = self.overridable

        backfill_until: str | Unset = UNSET
        if not isinstance(self.backfill_until, Unset):
            backfill_until = self.backfill_until.isoformat()

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "overridable": overridable,
            }
        )
        if backfill_until is not UNSET:
            field_dict["backfill_until"] = backfill_until
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_virtual_tag_config_values_item import CreateVirtualTagConfigValuesItem

        d = dict(src_dict)
        key = d.pop("key")

        overridable = d.pop("overridable")

        _backfill_until = d.pop("backfill_until", UNSET)
        backfill_until: datetime.date | Unset
        if isinstance(_backfill_until, Unset):
            backfill_until = UNSET
        else:
            backfill_until = isoparse(_backfill_until).date()

        _values = d.pop("values", UNSET)
        values: list[CreateVirtualTagConfigValuesItem] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = CreateVirtualTagConfigValuesItem.from_dict(values_item_data)

                values.append(values_item)

        create_virtual_tag_config = cls(
            key=key,
            overridable=overridable,
            backfill_until=backfill_until,
            values=values,
        )

        create_virtual_tag_config.additional_properties = d
        return create_virtual_tag_config

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
