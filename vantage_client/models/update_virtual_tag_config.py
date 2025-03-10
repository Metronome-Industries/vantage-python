import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_virtual_tag_config_values_item import UpdateVirtualTagConfigValuesItem


T = TypeVar("T", bound="UpdateVirtualTagConfig")


@_attrs_define
class UpdateVirtualTagConfig:
    """Updates an existing VirtualTagConfig.

    Attributes:
        key (Union[Unset, str]): The key of the VirtualTagConfig.
        overridable (Union[None, Unset, bool]): Whether the VirtualTagConfig can override a provider-supplied tag on a
            matching Cost.
        backfill_until (Union[None, Unset, datetime.date]): The earliest month the VirtualTagConfig should be backfilled
            to.
        values (Union[Unset, list['UpdateVirtualTagConfigValuesItem']]): Values for the VirtualTagConfig, with match
            precedence determined by order in the list.
    """

    key: Union[Unset, str] = UNSET
    overridable: Union[None, Unset, bool] = UNSET
    backfill_until: Union[None, Unset, datetime.date] = UNSET
    values: Union[Unset, list["UpdateVirtualTagConfigValuesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        overridable: Union[None, Unset, bool]
        if isinstance(self.overridable, Unset):
            overridable = UNSET
        else:
            overridable = self.overridable

        backfill_until: Union[None, Unset, str]
        if isinstance(self.backfill_until, Unset):
            backfill_until = UNSET
        elif isinstance(self.backfill_until, datetime.date):
            backfill_until = self.backfill_until.isoformat()
        else:
            backfill_until = self.backfill_until

        values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_virtual_tag_config_values_item import UpdateVirtualTagConfigValuesItem

        d = src_dict.copy()
        key = d.pop("key", UNSET)

        def _parse_overridable(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        overridable = _parse_overridable(d.pop("overridable", UNSET))

        def _parse_backfill_until(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backfill_until_type_0 = isoparse(data).date()

                return backfill_until_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        backfill_until = _parse_backfill_until(d.pop("backfill_until", UNSET))

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = UpdateVirtualTagConfigValuesItem.from_dict(values_item_data)

            values.append(values_item)

        update_virtual_tag_config = cls(
            key=key,
            overridable=overridable,
            backfill_until=backfill_until,
            values=values,
        )

        update_virtual_tag_config.additional_properties = d
        return update_virtual_tag_config

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
