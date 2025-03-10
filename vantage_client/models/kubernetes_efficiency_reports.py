from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.kubernetes_efficiency_report import KubernetesEfficiencyReport
    from ..models.links import Links


T = TypeVar("T", bound="KubernetesEfficiencyReports")


@_attrs_define
class KubernetesEfficiencyReports:
    """KubernetesEfficiencyReports model

    Attributes:
        links (Union[Unset, Links]):
        kubernetes_efficiency_reports (Union[Unset, list['KubernetesEfficiencyReport']]):
    """

    links: Union[Unset, "Links"] = UNSET
    kubernetes_efficiency_reports: Union[Unset, list["KubernetesEfficiencyReport"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        kubernetes_efficiency_reports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.kubernetes_efficiency_reports, Unset):
            kubernetes_efficiency_reports = []
            for kubernetes_efficiency_reports_item_data in self.kubernetes_efficiency_reports:
                kubernetes_efficiency_reports_item = kubernetes_efficiency_reports_item_data.to_dict()
                kubernetes_efficiency_reports.append(kubernetes_efficiency_reports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if kubernetes_efficiency_reports is not UNSET:
            field_dict["kubernetes_efficiency_reports"] = kubernetes_efficiency_reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.kubernetes_efficiency_report import KubernetesEfficiencyReport
        from ..models.links import Links

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        kubernetes_efficiency_reports = []
        _kubernetes_efficiency_reports = d.pop("kubernetes_efficiency_reports", UNSET)
        for kubernetes_efficiency_reports_item_data in _kubernetes_efficiency_reports or []:
            kubernetes_efficiency_reports_item = KubernetesEfficiencyReport.from_dict(
                kubernetes_efficiency_reports_item_data
            )

            kubernetes_efficiency_reports.append(kubernetes_efficiency_reports_item)

        kubernetes_efficiency_reports = cls(
            links=links,
            kubernetes_efficiency_reports=kubernetes_efficiency_reports,
        )

        kubernetes_efficiency_reports.additional_properties = d
        return kubernetes_efficiency_reports

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
