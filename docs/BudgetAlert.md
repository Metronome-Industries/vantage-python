# BudgetAlert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**budget_tokens** | **list[str]** | The tokens for the Budgets that the Budget Alert is monitoring to trigger alerts on. | [optional] 
**created_at** | **str** | The date and time, in UTC, the Budget Alert was created. ISO 8601 Formatted. | [optional] 
**workspace_token** | **str** | The token for the Workspace the ResourceReport is a part of. | [optional] 
**user_token** | **str** | The token for the User who created this BudgetAlert. | [optional] 
**user_tokens** | **list[str]** | The Users that receive the alert. | [optional] 
**duration_in_days** | **str** | The number of days from the start or end of the month to trigger the alert if the threshold is reached. | [optional] 
**threshold** | **str** | Alerts only send if they reach this number (as a percentage). When threshold is 100, that means alerts are triggered once costs reach 100% of the budget. | [optional] 
**period_to_track** | **str** | The period tracked on the alert. Used with duration_in_days to determine the time window of the alert. Possible values: start_of_the_month, end_of_the_month. | [optional] 
**integration_provider** | **str** | The provider used for sending alerts. This must be configured in the console. Possible values are: slack, microsoft_graph. | [optional] 
**recipient_channels** | **str** | The channels receiving the alerts. Requires an integration provider to be connected. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


