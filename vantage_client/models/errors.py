from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.errors_links import ErrorsLinks


T = TypeVar("T", bound="Errors")


@_attrs_define
class Errors:
    """Errors model

    Attributes:
        links (ErrorsLinks | Unset):
        errors (list[str] | Unset):
    """

    links: ErrorsLinks | Unset = UNSET
    errors: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.errors_links import ErrorsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: ErrorsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ErrorsLinks.from_dict(_links)

        errors = cast(list[str], d.pop("errors", UNSET))

        errors = cls(
            links=links,
            errors=errors,
        )

        errors.additional_properties = d
        return errors

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
