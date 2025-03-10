from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.links import Links
    from ..models.resource_report import ResourceReport


T = TypeVar("T", bound="ResourceReports")


@_attrs_define
class ResourceReports:
    """ResourceReports model

    Attributes:
        links (Union[Unset, Links]):
        resource_reports (Union[Unset, list['ResourceReport']]):
    """

    links: Union[Unset, "Links"] = UNSET
    resource_reports: Union[Unset, list["ResourceReport"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        resource_reports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.resource_reports, Unset):
            resource_reports = []
            for resource_reports_item_data in self.resource_reports:
                resource_reports_item = resource_reports_item_data.to_dict()
                resource_reports.append(resource_reports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if resource_reports is not UNSET:
            field_dict["resource_reports"] = resource_reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.links import Links
        from ..models.resource_report import ResourceReport

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        resource_reports = []
        _resource_reports = d.pop("resource_reports", UNSET)
        for resource_reports_item_data in _resource_reports or []:
            resource_reports_item = ResourceReport.from_dict(resource_reports_item_data)

            resource_reports.append(resource_reports_item)

        resource_reports = cls(
            links=links,
            resource_reports=resource_reports,
        )

        resource_reports.additional_properties = d
        return resource_reports

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
