from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_flow_report import NetworkFlowReport
    from ..models.network_flow_reports_links import NetworkFlowReportsLinks


T = TypeVar("T", bound="NetworkFlowReports")


@_attrs_define
class NetworkFlowReports:
    """NetworkFlowReports model

    Attributes:
        links (NetworkFlowReportsLinks | Unset):
        network_flow_reports (list[NetworkFlowReport] | Unset):
    """

    links: NetworkFlowReportsLinks | Unset = UNSET
    network_flow_reports: list[NetworkFlowReport] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        network_flow_reports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.network_flow_reports, Unset):
            network_flow_reports = []
            for network_flow_reports_item_data in self.network_flow_reports:
                network_flow_reports_item = network_flow_reports_item_data.to_dict()
                network_flow_reports.append(network_flow_reports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if network_flow_reports is not UNSET:
            field_dict["network_flow_reports"] = network_flow_reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_flow_report import NetworkFlowReport
        from ..models.network_flow_reports_links import NetworkFlowReportsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: NetworkFlowReportsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = NetworkFlowReportsLinks.from_dict(_links)

        _network_flow_reports = d.pop("network_flow_reports", UNSET)
        network_flow_reports: list[NetworkFlowReport] | Unset = UNSET
        if _network_flow_reports is not UNSET:
            network_flow_reports = []
            for network_flow_reports_item_data in _network_flow_reports:
                network_flow_reports_item = NetworkFlowReport.from_dict(network_flow_reports_item_data)

                network_flow_reports.append(network_flow_reports_item)

        network_flow_reports = cls(
            links=links,
            network_flow_reports=network_flow_reports,
        )

        network_flow_reports.additional_properties = d
        return network_flow_reports

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
