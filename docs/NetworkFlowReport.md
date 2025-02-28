# NetworkFlowReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**title** | **str** | The title of the NetworkFlowReport. | [optional] 
**default** | **bool** | Indicates whether the NetworkFlowReport is the default report. | [optional] 
**created_at** | **str** | The date and time, in UTC, the report was created. ISO 8601 Formatted. | [optional] 
**workspace_token** | **str** | The token for the Workspace the NetworkFlowReport is a part of. | [optional] 
**created_by_token** | **str** | The token for the User or Team that created this NetworkFlowReport. | [optional] 
**start_date** | **str** | The start date for the NetworkFlowReport. Only set for custom date ranges. ISO 8601 Formatted. | [optional] 
**end_date** | **str** | The end date for the NetworkFlowReport. Only set for custom date ranges. ISO 8601 Formatted. | [optional] 
**date_interval** | **str** | The date range for the NetworkFlowReport. Only present if a custom date range is not specified. | [optional] 
**groupings** | **str** | The grouping aggregations applied to the filtered data. | [optional] 
**flow_direction** | **str** | The flow weight of the NetworkFlowReport. Possible values: costs, bytes. | [optional] 
**flow_weight** | **str** | The flow weight of the NetworkFlowReport. Possible values: costs, bytes. | [optional] 
**filter** | **str** | The filter applied to the NetworkFlowReport. Additional documentation available at https://docs.vantage.sh/vql. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


