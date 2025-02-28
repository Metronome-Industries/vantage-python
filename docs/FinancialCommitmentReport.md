# FinancialCommitmentReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**title** | **str** | The title of the FinancialCommitmentReport. | [optional] 
**default** | **bool** | Indicates whether the FinancialCommitmentReport is the default report. | [optional] 
**created_at** | **str** | The date and time, in UTC, the report was created. ISO 8601 Formatted. | [optional] 
**workspace_token** | **str** | The token for the Workspace the FinancialCommitmentReport is a part of. | [optional] 
**user_token** | **str** | The token for the User who created this FinancialCommitmentReport. | [optional] 
**start_date** | **str** | The start date for the FinancialCommitmentReport. Only set for custom date ranges. ISO 8601 Formatted. | [optional] 
**end_date** | **str** | The end date for the FinancialCommitmentReport. Only set for custom date ranges. ISO 8601 Formatted. | [optional] 
**date_interval** | **str** | The date range for the FinancialCommitmentReport. Only present if a custom date range is not specified. | [optional] 
**date_bucket** | **str** | How costs are grouped and displayed in the FinancialCommitmentReport. Possible values: day, week, month. | [optional] 
**groupings** | **str** | The grouping aggregations applied to the filtered data. | [optional] 
**on_demand_costs_scope** | **str** | The scope for the costs. Possible values: discountable, all. | [optional] 
**filter** | **str** | The filter applied to the FinancialCommitmentReport. Additional documentation available at https://docs.vantage.sh/vql. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


