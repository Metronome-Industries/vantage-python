# Budget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**name** | **str** | The name of the Budget. | [optional] 
**workspace_token** | **str** | The token for the Workspace the Budget is a part of. | [optional] 
**user_token** | **str** | The token for the User who created this Budget. | [optional] 
**created_by_token** | **str** | The token of the Creator of the Budget. | [optional] 
**cost_report_token** | **str** | The token of the Report associated with the Budget. | [optional] 
**created_at** | **str** | The date and time, in UTC, the Budget was created. ISO 8601 Formatted. | [optional] 
**budget_alert_tokens** | **list[str]** | The tokens of the BudgetAlerts associated with the Budget. | [optional] 
**child_budget_tokens** | **list[str]** | The tokens of the child Budgets associated with the hierarchical Budget. | [optional] 
**periods** | [**list[BudgetPeriod]**](BudgetPeriod.md) | The budget periods associated with the Budget. | [optional] 
**performance** | [**list[BudgetPerformance]**](BudgetPerformance.md) | The historical performance of the Budget. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


