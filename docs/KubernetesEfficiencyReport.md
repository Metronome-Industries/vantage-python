# KubernetesEfficiencyReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**title** | **str** | The title of the KubernetesEfficiencyReport. | [optional] 
**default** | **bool** | Indicates whether the KubernetesEfficiencyReport is the default report. | [optional] 
**created_at** | **str** | The date and time, in UTC, the report was created. ISO 8601 Formatted. | [optional] 
**workspace_token** | **str** | The token for the Workspace the KubernetesEfficiencyReport is a part of. | [optional] 
**user_token** | **str** | The token for the User who created this KubernetesEfficiencyReport. | [optional] 
**start_date** | **str** | The start date for the KubernetesEfficiencyReport. Only set for custom date ranges. ISO 8601 Formatted. | [optional] 
**end_date** | **str** | The end date for the KubernetesEfficiencyReport. Only set for custom date ranges. ISO 8601 Formatted. | [optional] 
**date_interval** | **str** | The date range for the KubernetesEfficiencyReport. Only present if a custom date range is not specified. | [optional] 
**date_bucket** | **str** | How costs are grouped and displayed in the KubernetesEfficiencyReport. Possible values: day, week, month. | [optional] 
**aggregated_by** | **str** | How costs are aggregated by. Possible values: idle_cost, amount, cost_efficiency. | [optional] 
**groupings** | **str** | Grouping values for aggregating costs on the KubernetesEfficiencyReport. Valid groupings: cluster_id, namespace, labeled, category, label, label:&lt;label_name&gt;. | [optional] 
**filter** | **str** | The filter applied to the KubernetesEfficiencyReport. Additional documentation available at https://docs.vantage.sh/vql. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


