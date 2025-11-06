from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard import Dashboard
    from ..models.dashboards_links import DashboardsLinks


T = TypeVar("T", bound="Dashboards")


@_attrs_define
class Dashboards:
    """Dashboards model

    Attributes:
        links (DashboardsLinks | Unset):
        dashboards (list[Dashboard] | Unset):
    """

    links: DashboardsLinks | Unset = UNSET
    dashboards: list[Dashboard] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        dashboards: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dashboards, Unset):
            dashboards = []
            for dashboards_item_data in self.dashboards:
                dashboards_item = dashboards_item_data.to_dict()
                dashboards.append(dashboards_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if dashboards is not UNSET:
            field_dict["dashboards"] = dashboards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard import Dashboard
        from ..models.dashboards_links import DashboardsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: DashboardsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = DashboardsLinks.from_dict(_links)

        _dashboards = d.pop("dashboards", UNSET)
        dashboards: list[Dashboard] | Unset = UNSET
        if _dashboards is not UNSET:
            dashboards = []
            for dashboards_item_data in _dashboards:
                dashboards_item = Dashboard.from_dict(dashboards_item_data)

                dashboards.append(dashboards_item)

        dashboards = cls(
            links=links,
            dashboards=dashboards,
        )

        dashboards.additional_properties = d
        return dashboards

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
