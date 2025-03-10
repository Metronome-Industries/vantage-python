from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.network_flow_report import NetworkFlowReport


T = TypeVar("T", bound="NetworkFlowReports")


@_attrs_define
class NetworkFlowReports:
    """NetworkFlowReports model

    Attributes:
        links (Union[Unset, Links]):
        network_flow_reports (Union[Unset, list['NetworkFlowReport']]):
    """

    links: Union[Unset, "Links"] = UNSET
    network_flow_reports: Union[Unset, list["NetworkFlowReport"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        network_flow_reports: Union[Unset, list[dict[str, Any]]] = UNSET
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.links import Links
        from ..models.network_flow_report import NetworkFlowReport

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        network_flow_reports = []
        _network_flow_reports = d.pop("network_flow_reports", UNSET)
        for network_flow_reports_item_data in _network_flow_reports or []:
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
