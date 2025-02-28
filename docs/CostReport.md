# CostReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**title** | **str** | The title of the CostReport. | [optional] 
**folder_token** | **str** | The token for the Folder the CostReport is a part of. | [optional] 
**saved_filter_tokens** | **list[str]** | The tokens for the SavedFilters assigned to the CostReport. | [optional] 
**business_metric_tokens_with_metadata** | [**list[AttachedBusinessMetricForCostReport]**](AttachedBusinessMetricForCostReport.md) | The tokens for the BusinessMetrics assigned to the CostReport, the unit scale, and label filter. | [optional] 
**filter** | **str** | The filter applied to the CostReport. Additional documentation available at https://docs.vantage.sh/vql. | [optional] 
**groupings** | **str** | The grouping aggregations applied to the filtered data. | [optional] 
**settings** | [**CreateCostReportSettings**](CreateCostReportSettings.md) |  | [optional] 
**created_at** | **str** | The date and time, in UTC, the report was created. ISO 8601 Formatted. | [optional] 
**workspace_token** | **str** | The token for the Workspace the CostReport is a part of. | [optional] 
**previous_period_start_date** | **str** | The previous period start date of the CostReport. ISO 8601 Formatted. | [optional] 
**previous_period_end_date** | **str** | The previous period end date of the CostReport. ISO 8601 Formatted. | [optional] 
**start_date** | **str** | The start date of the CostReports. ISO 8601 Formatted. Overwrites &#39;date_interval&#39; if set. | [optional] 
**end_date** | **str** | The end date of the CostReports. ISO 8601 Formatted. Overwrites &#39;date_interval&#39; if set. | [optional] 
**date_interval** | **str** | The date interval of the CostReport. | [optional] 
**chart_type** | **str** | The chart type of the CostReport. | [optional] 
**date_bin** | **str** | The date bin of the CostReport. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


