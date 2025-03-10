from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_business_metric_cost_report_tokens_with_metadata_item import (
        UpdateBusinessMetricCostReportTokensWithMetadataItem,
    )
    from ..models.update_business_metric_values_item import UpdateBusinessMetricValuesItem


T = TypeVar("T", bound="UpdateBusinessMetric")


@_attrs_define
class UpdateBusinessMetric:
    """Updates an existing BusinessMetric.

    Attributes:
        title (Union[Unset, str]): The title of the BusinessMetric.
        cost_report_tokens_with_metadata (Union[Unset, list['UpdateBusinessMetricCostReportTokensWithMetadataItem']]):
            The tokens for any CostReports that use the BusinessMetric, and the unit scale.
        values (Union[Unset, list['UpdateBusinessMetricValuesItem']]): The dates, amounts, and (optional) labels for the
            BusinessMetric.
    """

    title: Union[Unset, str] = UNSET
    cost_report_tokens_with_metadata: Union[Unset, list["UpdateBusinessMetricCostReportTokensWithMetadataItem"]] = UNSET
    values: Union[Unset, list["UpdateBusinessMetricValuesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        cost_report_tokens_with_metadata: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.cost_report_tokens_with_metadata, Unset):
            cost_report_tokens_with_metadata = []
            for cost_report_tokens_with_metadata_item_data in self.cost_report_tokens_with_metadata:
                cost_report_tokens_with_metadata_item = cost_report_tokens_with_metadata_item_data.to_dict()
                cost_report_tokens_with_metadata.append(cost_report_tokens_with_metadata_item)

        values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if cost_report_tokens_with_metadata is not UNSET:
            field_dict["cost_report_tokens_with_metadata"] = cost_report_tokens_with_metadata
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_business_metric_cost_report_tokens_with_metadata_item import (
            UpdateBusinessMetricCostReportTokensWithMetadataItem,
        )
        from ..models.update_business_metric_values_item import UpdateBusinessMetricValuesItem

        d = src_dict.copy()
        title = d.pop("title", UNSET)

        cost_report_tokens_with_metadata = []
        _cost_report_tokens_with_metadata = d.pop("cost_report_tokens_with_metadata", UNSET)
        for cost_report_tokens_with_metadata_item_data in _cost_report_tokens_with_metadata or []:
            cost_report_tokens_with_metadata_item = UpdateBusinessMetricCostReportTokensWithMetadataItem.from_dict(
                cost_report_tokens_with_metadata_item_data
            )

            cost_report_tokens_with_metadata.append(cost_report_tokens_with_metadata_item)

        values = []
        _values = d.pop("values", UNSET)
        for values_item_data in _values or []:
            values_item = UpdateBusinessMetricValuesItem.from_dict(values_item_data)

            values.append(values_item)

        update_business_metric = cls(
            title=title,
            cost_report_tokens_with_metadata=cost_report_tokens_with_metadata,
            values=values,
        )

        update_business_metric.additional_properties = d
        return update_business_metric

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
