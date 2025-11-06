from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_commitment_report import FinancialCommitmentReport
    from ..models.financial_commitment_reports_links import FinancialCommitmentReportsLinks


T = TypeVar("T", bound="FinancialCommitmentReports")


@_attrs_define
class FinancialCommitmentReports:
    """FinancialCommitmentReports model

    Attributes:
        links (FinancialCommitmentReportsLinks | Unset):
        financial_commitment_reports (list[FinancialCommitmentReport] | Unset):
    """

    links: FinancialCommitmentReportsLinks | Unset = UNSET
    financial_commitment_reports: list[FinancialCommitmentReport] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        financial_commitment_reports: list[dict[str, Any]] | Unset = UNSET
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.financial_commitment_report import FinancialCommitmentReport
        from ..models.financial_commitment_reports_links import FinancialCommitmentReportsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: FinancialCommitmentReportsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = FinancialCommitmentReportsLinks.from_dict(_links)

        _financial_commitment_reports = d.pop("financial_commitment_reports", UNSET)
        financial_commitment_reports: list[FinancialCommitmentReport] | Unset = UNSET
        if _financial_commitment_reports is not UNSET:
            financial_commitment_reports = []
            for financial_commitment_reports_item_data in _financial_commitment_reports:
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
