# Dashboard

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**title** | **str** | The title of the Dashboard. | [optional] 
**widgets** | [**list[DashboardWidget]**](DashboardWidget.md) |  | [optional] 
**saved_filter_tokens** | **list[str]** | The tokens of the Saved Filters used in the Dashboard. | [optional] 
**date_bin** | **str** | Determines how to group costs in the Dashboard. | [optional] 
**date_interval** | **str** | Determines the date range for Reports in the Dashboard. Guaranteed to be set to &#39;custom&#39; if &#39;start_date&#39; and &#39;end_date&#39; are set. | [optional] 
**start_date** | **str** | The start date for the date range for Reports in the Dashboard. ISO 8601 Formatted. Overwrites &#39;date_interval&#39; if set. | [optional] 
**end_date** | **str** | The end date for the date range for Reports in the Dashboard. ISO 8601 Formatted. Overwrites &#39;date_interval&#39; if set. | [optional] 
**created_at** | **str** | The date and time, in UTC, the Dashboard was created. ISO 8601 Formatted. | [optional] 
**updated_at** | **str** | The date and time, in UTC, the Dashboard was created. ISO 8601 Formatted. | [optional] 
**workspace_token** | **str** | The token for the Workspace the Dashboard is a part of. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


