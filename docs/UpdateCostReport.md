# UpdateCostReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the CostReport. | [optional] 
**groupings** | **str** | Grouping values for aggregating costs on the report. Valid groupings: account_id, billing_account_id, charge_type, cost_category, cost_subcategory, provider, region, resource_id, service, tagged, tag:&lt;tag_value&gt;. If providing multiple groupings, join as comma separated values: groupings&#x3D;provider,service,region | [optional] 
**filter** | **str** | The filter query language to apply to the CostReport. Additional documentation available at https://docs.vantage.sh/vql. | [optional] 
**saved_filter_tokens** | **list[str]** | The tokens of the SavedFilters to apply to the CostReport. | [optional] 
**business_metric_tokens_with_metadata** | [**list[CreateCostReportBusinessMetricTokensWithMetadata]**](CreateCostReportBusinessMetricTokensWithMetadata.md) | The tokens for any BusinessMetrics to attach to the CostReport, and the unit scale. | [optional] 
**folder_token** | **str** | The token of the Folder to add the CostReport to. Determines the Workspace the report is assigned to. | [optional] 
**settings** | [**UpdateCostReportSettings**](UpdateCostReportSettings.md) |  | [optional] 
**previous_period_start_date** | **str** | The previous period start date of the CostReport. ISO 8601 Formatted. | [optional] 
**previous_period_end_date** | **str** | The previous period end date of the CostReport. ISO 8601 Formatted. | [optional] 
**start_date** | **str** | The start date of the CostReport. ISO 8601 Formatted. Incompatible with &#39;date_interval&#39; parameter. | [optional] 
**end_date** | **str** | The end date of the CostReport. ISO 8601 Formatted. Incompatible with &#39;date_interval&#39; parameter. | [optional] 
**date_interval** | **str** | The date interval of the CostReport. Incompatible with &#39;start_date&#39; and &#39;end_date&#39; parameters. Defaults to &#39;this_month&#39; if start_date and end_date are not provided. | [optional] 
**chart_type** | **str** | The chart type of the CostReport. | [optional] [default to 'line']
**date_bin** | **str** | The date bin of the CostReport. | [optional] [default to 'cumulative']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


