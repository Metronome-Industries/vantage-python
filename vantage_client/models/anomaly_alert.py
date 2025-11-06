from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnomalyAlert")


@_attrs_define
class AnomalyAlert:
    """AnomalyAlert model

    Attributes:
        token (str | Unset):
        created_at (str | Unset): The date and time, in UTC, the AnomalyAlert was created. ISO 8601 Formatted. Example:
            2021-07-09T00:00:00Z.
        alerted_at (str | Unset): The date and time, in UTC, the AnomalyAlert is sent. ISO 8601 Formatted. Example:
            2021-07-09T00:00:00Z.
        category (str | Unset): The category of the AnomalyAlert.
        service (str | Unset): The provider service causing the AnomalyAlert.
        provider (str | Unset): The provider of the service causing the AnomalyAlert.
        amount (str | Unset): The amount observed.
        previous_amount (str | Unset): The previous amount observed.
        seven_day_average (str | Unset): The seven day average of the amount observed.
        status (str | Unset): The status of the AnomalyAlert.
        feedback (str | Unset): The user-provided feedback of why alert was ignored/archived.
        resources (list[str] | Unset): The names of the resources the AnomalyAlert was attributed to.
        cost_report_token (str | Unset): The token of the Report associated with the AnomalyAlert.
    """

    token: str | Unset = UNSET
    created_at: str | Unset = UNSET
    alerted_at: str | Unset = UNSET
    category: str | Unset = UNSET
    service: str | Unset = UNSET
    provider: str | Unset = UNSET
    amount: str | Unset = UNSET
    previous_amount: str | Unset = UNSET
    seven_day_average: str | Unset = UNSET
    status: str | Unset = UNSET
    feedback: str | Unset = UNSET
    resources: list[str] | Unset = UNSET
    cost_report_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        created_at = self.created_at

        alerted_at = self.alerted_at

        category = self.category

        service = self.service

        provider = self.provider

        amount = self.amount

        previous_amount = self.previous_amount

        seven_day_average = self.seven_day_average

        status = self.status

        feedback = self.feedback

        resources: list[str] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources

        cost_report_token = self.cost_report_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if alerted_at is not UNSET:
            field_dict["alerted_at"] = alerted_at
        if category is not UNSET:
            field_dict["category"] = category
        if service is not UNSET:
            field_dict["service"] = service
        if provider is not UNSET:
            field_dict["provider"] = provider
        if amount is not UNSET:
            field_dict["amount"] = amount
        if previous_amount is not UNSET:
            field_dict["previous_amount"] = previous_amount
        if seven_day_average is not UNSET:
            field_dict["seven_day_average"] = seven_day_average
        if status is not UNSET:
            field_dict["status"] = status
        if feedback is not UNSET:
            field_dict["feedback"] = feedback
        if resources is not UNSET:
            field_dict["resources"] = resources
        if cost_report_token is not UNSET:
            field_dict["cost_report_token"] = cost_report_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        created_at = d.pop("created_at", UNSET)

        alerted_at = d.pop("alerted_at", UNSET)

        category = d.pop("category", UNSET)

        service = d.pop("service", UNSET)

        provider = d.pop("provider", UNSET)

        amount = d.pop("amount", UNSET)

        previous_amount = d.pop("previous_amount", UNSET)

        seven_day_average = d.pop("seven_day_average", UNSET)

        status = d.pop("status", UNSET)

        feedback = d.pop("feedback", UNSET)

        resources = cast(list[str], d.pop("resources", UNSET))

        cost_report_token = d.pop("cost_report_token", UNSET)

        anomaly_alert = cls(
            token=token,
            created_at=created_at,
            alerted_at=alerted_at,
            category=category,
            service=service,
            provider=provider,
            amount=amount,
            previous_amount=previous_amount,
            seven_day_average=seven_day_average,
            status=status,
            feedback=feedback,
            resources=resources,
            cost_report_token=cost_report_token,
        )

        anomaly_alert.additional_properties = d
        return anomaly_alert

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
