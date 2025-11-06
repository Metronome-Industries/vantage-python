from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cost_alert_event_metadata import CostAlertEventMetadata


T = TypeVar("T", bound="CostAlertEvent")


@_attrs_define
class CostAlertEvent:
    """CostAlertEvent model

    Attributes:
        token (str | Unset):
        created_at (str | Unset): The date and time, in UTC, the CostAlertEvent was created. ISO 8601 Formatted.
            Example: 2021-07-09T00:00:00Z.
        triggered_at (str | Unset): The date and time, in UTC, the CostAlertEvent is sent. ISO 8601 Formatted. Example:
            2021-07-09T00:00:00Z.
        description (str | Unset): The description of the CostAlertEvent.
        alert_type (str | Unset): The type of the CostAlertEvent.
        metadata (CostAlertEventMetadata | Unset): The metadata of the CostAlertEvent.
        report_token (str | Unset): The token of the report associated with the CostAlertEvent.
        alert_token (str | Unset): The token of the alert associated with the CostAlertEvent.
    """

    token: str | Unset = UNSET
    created_at: str | Unset = UNSET
    triggered_at: str | Unset = UNSET
    description: str | Unset = UNSET
    alert_type: str | Unset = UNSET
    metadata: CostAlertEventMetadata | Unset = UNSET
    report_token: str | Unset = UNSET
    alert_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        created_at = self.created_at

        triggered_at = self.triggered_at

        description = self.description

        alert_type = self.alert_type

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        report_token = self.report_token

        alert_token = self.alert_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if triggered_at is not UNSET:
            field_dict["triggered_at"] = triggered_at
        if description is not UNSET:
            field_dict["description"] = description
        if alert_type is not UNSET:
            field_dict["alert_type"] = alert_type
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if report_token is not UNSET:
            field_dict["report_token"] = report_token
        if alert_token is not UNSET:
            field_dict["alert_token"] = alert_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cost_alert_event_metadata import CostAlertEventMetadata

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        created_at = d.pop("created_at", UNSET)

        triggered_at = d.pop("triggered_at", UNSET)

        description = d.pop("description", UNSET)

        alert_type = d.pop("alert_type", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CostAlertEventMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CostAlertEventMetadata.from_dict(_metadata)

        report_token = d.pop("report_token", UNSET)

        alert_token = d.pop("alert_token", UNSET)

        cost_alert_event = cls(
            token=token,
            created_at=created_at,
            triggered_at=triggered_at,
            description=description,
            alert_type=alert_type,
            metadata=metadata,
            report_token=report_token,
            alert_token=alert_token,
        )

        cost_alert_event.additional_properties = d
        return cost_alert_event

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
