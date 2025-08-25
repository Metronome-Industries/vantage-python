from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invoice import Invoice
    from ..models.invoices_links import InvoicesLinks


T = TypeVar("T", bound="Invoices")


@_attrs_define
class Invoices:
    """Invoices model

    Attributes:
        links (Union[Unset, InvoicesLinks]):
        invoices (Union[Unset, list['Invoice']]):
    """

    links: Union[Unset, "InvoicesLinks"] = UNSET
    invoices: Union[Unset, list["Invoice"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        invoices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.invoices, Unset):
            invoices = []
            for invoices_item_data in self.invoices:
                invoices_item = invoices_item_data.to_dict()
                invoices.append(invoices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if invoices is not UNSET:
            field_dict["invoices"] = invoices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invoice import Invoice
        from ..models.invoices_links import InvoicesLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: Union[Unset, InvoicesLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = InvoicesLinks.from_dict(_links)

        invoices = []
        _invoices = d.pop("invoices", UNSET)
        for invoices_item_data in _invoices or []:
            invoices_item = Invoice.from_dict(invoices_item_data)

            invoices.append(invoices_item)

        invoices = cls(
            links=links,
            invoices=invoices,
        )

        invoices.additional_properties = d
        return invoices

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
