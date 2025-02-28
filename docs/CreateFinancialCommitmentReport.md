# CreateFinancialCommitmentReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_token** | **str** | The Workspace in which the FinancialCommitmentReport will be created. | 
**title** | **str** | The title of the FinancialCommitmentReport. | 
**filter** | **str** | The filter query language to apply to the FinancialCommitmentReport. Additional documentation available at https://docs.vantage.sh/vql. | [optional] 
**start_date** | **date** | The start date of the FinancialCommitmentReport. YYYY-MM-DD formatted. Incompatible with &#39;date_interval&#39; parameter. | [optional] 
**end_date** | **date** | The end date of the FinancialCommitmentReport. YYYY-MM-DD formatted. Incompatible with &#39;date_interval&#39; parameter. | [optional] 
**date_interval** | **str** | The date interval of the FinancialCommitmentReport. Unless &#39;custom&#39; is used, this is incompatible with &#39;start_date&#39; and &#39;end_date&#39; parameters. Defaults to &#39;last_3_months&#39;. | [optional] 
**date_bucket** | **str** | The date bucket of the FinancialCommitmentReport. | [optional] 
**on_demand_costs_scope** | **str** | The scope for the costs. Possible values: discountable, all. | [optional] 
**groupings** | **list[str]** | Grouping values for aggregating costs on the FinancialCommitmentReport. Valid groupings: cost_type, commitment_type, service, resource_account_id, provider_account_id, region, cost_category, cost_sub_category, instance_type, tag, tag:&lt;label_name&gt;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


