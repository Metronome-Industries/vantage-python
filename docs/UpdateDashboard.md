# UpdateDashboard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the Dashboard. | [optional] 
**widgets** | [**list[CreateDashboardWidgets]**](CreateDashboardWidgets.md) | The widgets to add to the Dashboard. Currently supports CostReport, ResourceReport, KubernetesEfficiencyReport, and FinancialCommitmentReport. | [optional] 
**saved_filter_tokens** | **list[str]** | The tokens of the Saved Filters used in the Dashboard. | [optional] 
**date_bin** | **str** | Determines how to group costs in the Dashboard. | [optional] 
**date_interval** | **str** | Determines the date range in the Dashboard. Incompatible with &#39;start_date&#39; and &#39;end_date&#39; parameters. | [optional] 
**start_date** | **str** | The start date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with &#39;date_interval&#39; parameter. | [optional] 
**end_date** | **str** | The end date for the date range for costs in the Dashboard. ISO 8601 Formatted. Incompatible with &#39;date_interval&#39; parameter. | 
**workspace_token** | **str** | The token of the Workspace the Dashboard belongs to. Required if the API token is associated with multiple Workspaces. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


