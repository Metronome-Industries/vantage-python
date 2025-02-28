# UpdateBudget

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Budget. | [optional] 
**cost_report_token** | **str** | The CostReport token. Ignored for hierarchical Budgets. | [optional] 
**child_budget_tokens** | **list[str]** | The tokens of any child Budgets when creating a hierarchical Budget. | [optional] 
**periods** | [**list[CreateBudgetPeriods]**](CreateBudgetPeriods.md) | The periods for the Budget. The start_at and end_at must be iso8601 formatted e.g. YYYY-MM-DD. Ignored for hierarchical Budgets. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


