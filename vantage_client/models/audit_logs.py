from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_log import AuditLog
    from ..models.audit_logs_links import AuditLogsLinks


T = TypeVar("T", bound="AuditLogs")


@_attrs_define
class AuditLogs:
    """AuditLogs model

    Attributes:
        links (Union[Unset, AuditLogsLinks]):
        audit_logs (Union[Unset, list['AuditLog']]):
    """

    links: Union[Unset, "AuditLogsLinks"] = UNSET
    audit_logs: Union[Unset, list["AuditLog"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        audit_logs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.audit_logs, Unset):
            audit_logs = []
            for audit_logs_item_data in self.audit_logs:
                audit_logs_item = audit_logs_item_data.to_dict()
                audit_logs.append(audit_logs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if links is not UNSET:
            field_dict["links"] = links
        if audit_logs is not UNSET:
            field_dict["audit_logs"] = audit_logs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_log import AuditLog
        from ..models.audit_logs_links import AuditLogsLinks

        d = dict(src_dict)
        _links = d.pop("links", UNSET)
        links: Union[Unset, AuditLogsLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = AuditLogsLinks.from_dict(_links)

        audit_logs = []
        _audit_logs = d.pop("audit_logs", UNSET)
        for audit_logs_item_data in _audit_logs or []:
            audit_logs_item = AuditLog.from_dict(audit_logs_item_data)

            audit_logs.append(audit_logs_item)

        audit_logs = cls(
            links=links,
            audit_logs=audit_logs,
        )

        audit_logs.additional_properties = d
        return audit_logs

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
