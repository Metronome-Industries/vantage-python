from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBusinessMetricDatadogMetricFields")


@_attrs_define
class CreateBusinessMetricDatadogMetricFields:
    """Datadog metric configuration fields

    Attributes:
        integration_token (Union[Unset, str]): Integration token for the account from which you would like to fetch
            metrics.
        query (Union[Unset, str]): Datadog metrics query string. e.g. sum:aws.applicationelb.request_count{region:us-
            east-1}.rollup(avg,daily)
    """

    integration_token: Union[Unset, str] = UNSET
    query: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integration_token = self.integration_token

        query = self.query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if integration_token is not UNSET:
            field_dict["integration_token"] = integration_token
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        integration_token = d.pop("integration_token", UNSET)

        query = d.pop("query", UNSET)

        create_business_metric_datadog_metric_fields = cls(
            integration_token=integration_token,
            query=query,
        )

        create_business_metric_datadog_metric_fields.additional_properties = d
        return create_business_metric_datadog_metric_fields

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
