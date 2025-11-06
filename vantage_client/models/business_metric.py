from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.business_metric_import_type import BusinessMetricImportType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attached_cost_report_for_business_metric import AttachedCostReportForBusinessMetric
    from ..models.cloudwatch_fields import CloudwatchFields
    from ..models.datadog_metric_fields import DatadogMetricFields


T = TypeVar("T", bound="BusinessMetric")


@_attrs_define
class BusinessMetric:
    """BusinessMetric model

    Attributes:
        token (str | Unset): The token of the BusinessMetric. Example: bsnss_mtrc_1234.
        title (str | Unset): The title of the BusinessMetric. Example: Total Revenue.
        created_by_token (str | Unset): The token of the Creator of the BusinessMetric. Example: usr_1234.
        cost_report_tokens_with_metadata (list[AttachedCostReportForBusinessMetric] | Unset): The tokens for any
            CostReports that use the BusinessMetric, the unit scale, and label filter.
        import_type (BusinessMetricImportType | Unset): The type of import for the BusinessMetric. Example:
            datadog_metrics.
        integration_token (str | Unset): The Integration token used to import the BusinessMetric.
        cloudwatch_fields (CloudwatchFields | Unset):
        datadog_metric_fields (DatadogMetricFields | Unset):
    """

    token: str | Unset = UNSET
    title: str | Unset = UNSET
    created_by_token: str | Unset = UNSET
    cost_report_tokens_with_metadata: list[AttachedCostReportForBusinessMetric] | Unset = UNSET
    import_type: BusinessMetricImportType | Unset = UNSET
    integration_token: str | Unset = UNSET
    cloudwatch_fields: CloudwatchFields | Unset = UNSET
    datadog_metric_fields: DatadogMetricFields | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        title = self.title

        created_by_token = self.created_by_token

        cost_report_tokens_with_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cost_report_tokens_with_metadata, Unset):
            cost_report_tokens_with_metadata = []
            for cost_report_tokens_with_metadata_item_data in self.cost_report_tokens_with_metadata:
                cost_report_tokens_with_metadata_item = cost_report_tokens_with_metadata_item_data.to_dict()
                cost_report_tokens_with_metadata.append(cost_report_tokens_with_metadata_item)

        import_type: str | Unset = UNSET
        if not isinstance(self.import_type, Unset):
            import_type = self.import_type.value

        integration_token = self.integration_token

        cloudwatch_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cloudwatch_fields, Unset):
            cloudwatch_fields = self.cloudwatch_fields.to_dict()

        datadog_metric_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.datadog_metric_fields, Unset):
            datadog_metric_fields = self.datadog_metric_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if title is not UNSET:
            field_dict["title"] = title
        if created_by_token is not UNSET:
            field_dict["created_by_token"] = created_by_token
        if cost_report_tokens_with_metadata is not UNSET:
            field_dict["cost_report_tokens_with_metadata"] = cost_report_tokens_with_metadata
        if import_type is not UNSET:
            field_dict["import_type"] = import_type
        if integration_token is not UNSET:
            field_dict["integration_token"] = integration_token
        if cloudwatch_fields is not UNSET:
            field_dict["cloudwatch_fields"] = cloudwatch_fields
        if datadog_metric_fields is not UNSET:
            field_dict["datadog_metric_fields"] = datadog_metric_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attached_cost_report_for_business_metric import AttachedCostReportForBusinessMetric
        from ..models.cloudwatch_fields import CloudwatchFields
        from ..models.datadog_metric_fields import DatadogMetricFields

        d = dict(src_dict)
        token = d.pop("token", UNSET)

        title = d.pop("title", UNSET)

        created_by_token = d.pop("created_by_token", UNSET)

        _cost_report_tokens_with_metadata = d.pop("cost_report_tokens_with_metadata", UNSET)
        cost_report_tokens_with_metadata: list[AttachedCostReportForBusinessMetric] | Unset = UNSET
        if _cost_report_tokens_with_metadata is not UNSET:
            cost_report_tokens_with_metadata = []
            for cost_report_tokens_with_metadata_item_data in _cost_report_tokens_with_metadata:
                cost_report_tokens_with_metadata_item = AttachedCostReportForBusinessMetric.from_dict(
                    cost_report_tokens_with_metadata_item_data
                )

                cost_report_tokens_with_metadata.append(cost_report_tokens_with_metadata_item)

        _import_type = d.pop("import_type", UNSET)
        import_type: BusinessMetricImportType | Unset
        if isinstance(_import_type, Unset):
            import_type = UNSET
        else:
            import_type = BusinessMetricImportType(_import_type)

        integration_token = d.pop("integration_token", UNSET)

        _cloudwatch_fields = d.pop("cloudwatch_fields", UNSET)
        cloudwatch_fields: CloudwatchFields | Unset
        if isinstance(_cloudwatch_fields, Unset):
            cloudwatch_fields = UNSET
        else:
            cloudwatch_fields = CloudwatchFields.from_dict(_cloudwatch_fields)

        _datadog_metric_fields = d.pop("datadog_metric_fields", UNSET)
        datadog_metric_fields: DatadogMetricFields | Unset
        if isinstance(_datadog_metric_fields, Unset):
            datadog_metric_fields = UNSET
        else:
            datadog_metric_fields = DatadogMetricFields.from_dict(_datadog_metric_fields)

        business_metric = cls(
            token=token,
            title=title,
            created_by_token=created_by_token,
            cost_report_tokens_with_metadata=cost_report_tokens_with_metadata,
            import_type=import_type,
            integration_token=integration_token,
            cloudwatch_fields=cloudwatch_fields,
            datadog_metric_fields=datadog_metric_fields,
        )

        business_metric.additional_properties = d
        return business_metric

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
