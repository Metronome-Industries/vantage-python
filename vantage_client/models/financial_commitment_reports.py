from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_commitment_report import FinancialCommitmentReport
    from ..models.links import Links


T = TypeVar("T", bound="FinancialCommitmentReports")


@_attrs_define
class FinancialCommitmentReports:
    """FinancialCommitmentReports model

    Attributes:
        links (Union[Unset, Links]):
        financial_commitment_reports (Union[Unset, list['FinancialCommitmentReport']]):
    """

    links: Union[Unset, "Links"] = UNSET
    financial_commitment_reports: Union[Unset, list["FinancialCommitmentReport"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        financial_commitment_reports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.financial_commitment_reports, Unset):
            financial_commitment_reports = []
            for financial_commitment_reports_item_data in self.financial_commitment_reports:
                financial_commitment_reports_item = financial_commitment_reports_item_data.to_dict()
                financial_commitment_reports.append(financial_commitment_reports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if financial_commitment_reports is not UNSET:
            field_dict["financial_commitment_reports"] = financial_commitment_reports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.financial_commitment_report import FinancialCommitmentReport
        from ..models.links import Links

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        financial_commitment_reports = []
        _financial_commitment_reports = d.pop("financial_commitment_reports", UNSET)
        for financial_commitment_reports_item_data in _financial_commitment_reports or []:
            financial_commitment_reports_item = FinancialCommitmentReport.from_dict(
                financial_commitment_reports_item_data
            )

            financial_commitment_reports.append(financial_commitment_reports_item)

        financial_commitment_reports = cls(
            links=links,
            financial_commitment_reports=financial_commitment_reports,
        )

        financial_commitment_reports.additional_properties = d
        return financial_commitment_reports

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
