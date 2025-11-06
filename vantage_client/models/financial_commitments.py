from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_commitment import FinancialCommitment
    from ..models.financial_commitments_links import FinancialCommitmentsLinks


T = TypeVar("T", bound="FinancialCommitments")


@_attrs_define
class FinancialCommitments:
    """FinancialCommitments model

    Attributes:
        links (FinancialCommitmentsLinks | Unset):
        financial_commitments (list[FinancialCommitment] | Unset):
    """

    links: FinancialCommitmentsLinks | Unset = UNSET
    financial_commitments: list[FinancialCommitment] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        financial_commitments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.financial_commitments, Unset):
            financial_commitments = []
            for financial_commitments_item_data in self.financial_commitments:
                financial_commitments_item = financial_commitments_item_data.to_dict()
                financial_commitments.append(financial_commitments_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if financial_commitments is not UNSET:
            field_dict["financial_commitments"] = financial_commitments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.financial_commitment import FinancialCommitment
        from ..models.financial_commitments_links import FinancialCommitmentsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: FinancialCommitmentsLinks | Unset
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = FinancialCommitmentsLinks.from_dict(_links)

        _financial_commitments = d.pop("financial_commitments", UNSET)
        financial_commitments: list[FinancialCommitment] | Unset = UNSET
        if _financial_commitments is not UNSET:
            financial_commitments = []
            for financial_commitments_item_data in _financial_commitments:
                financial_commitments_item = FinancialCommitment.from_dict(financial_commitments_item_data)

                financial_commitments.append(financial_commitments_item)

        financial_commitments = cls(
            links=links,
            financial_commitments=financial_commitments,
        )

        financial_commitments.additional_properties = d
        return financial_commitments

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
