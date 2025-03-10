from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.financial_commitment import FinancialCommitment
    from ..models.links import Links


T = TypeVar("T", bound="FinancialCommitments")


@_attrs_define
class FinancialCommitments:
    """FinancialCommitments model

    Attributes:
        links (Union[Unset, Links]):
        financial_commitments (Union[Unset, list['FinancialCommitment']]):
    """

    links: Union[Unset, "Links"] = UNSET
    financial_commitments: Union[Unset, list["FinancialCommitment"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        financial_commitments: Union[Unset, list[dict[str, Any]]] = UNSET
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
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.financial_commitment import FinancialCommitment
        from ..models.links import Links

        d = src_dict.copy()
        _links = d.pop("links", UNSET)
        links: Union[Unset, Links]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = Links.from_dict(_links)

        financial_commitments = []
        _financial_commitments = d.pop("financial_commitments", UNSET)
        for financial_commitments_item_data in _financial_commitments or []:
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
