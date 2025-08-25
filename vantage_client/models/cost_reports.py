from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_report import CostReport
    from ..models.cost_reports_links import CostReportsLinks


T = TypeVar("T", bound="CostReports")


@_attrs_define
class CostReports:
    """CostReports model

    Attributes:
        links (Union[Unset, CostReportsLinks]):
        cost_reports (Union[Unset, list['CostReport']]):
    """

    links: Union[Unset, "CostReportsLinks"] = UNSET
    cost_reports: Union[Unset, list["CostReport"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        cost_reports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cost_reports, Unset):
            cost_reports = []
            for cost_reports_item_data in self.cost_reports:
                cost_reports_item = cost_reports_item_data.to_dict()
                cost_reports.append(cost_reports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if cost_reports is not UNSET:
            field_dict["cost_reports"] = cost_reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_report import CostReport
        from ..models.cost_reports_links import CostReportsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: Union[Unset, CostReportsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = CostReportsLinks.from_dict(_links)

        cost_reports = []
        _cost_reports = d.pop("cost_reports", UNSET)
        for cost_reports_item_data in _cost_reports or []:
            cost_reports_item = CostReport.from_dict(cost_reports_item_data)

            cost_reports.append(cost_reports_item)

        cost_reports = cls(
            links=links,
            cost_reports=cost_reports,
        )

        cost_reports.additional_properties = d
        return cost_reports

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
