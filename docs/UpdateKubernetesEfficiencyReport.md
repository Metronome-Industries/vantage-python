# UpdateKubernetesEfficiencyReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the KubernetesEfficiencyReport. | [optional] 
**filter** | **str** | The filter query language to apply to the KubernetesEfficiencyReport. Additional documentation available at https://docs.vantage.sh/vql. | [optional] 
**start_date** | **date** | The start date of the KubernetesEfficiencyReport. ISO 8601 Formatted. Incompatible with &#39;date_interval&#39; parameter. | [optional] 
**end_date** | **date** | The end date of the KubernetesEfficiencyReport. ISO 8601 Formatted. Incompatible with &#39;date_interval&#39; parameter. | [optional] 
**date_interval** | **str** | The date interval of the KubernetesEfficiencyReport. Incompatible with &#39;start_date&#39; and &#39;end_date&#39; parameters. Defaults to &#39;this_month&#39; if start_date and end_date are not provided. | [optional] 
**aggregated_by** | **str** | The column by which the costs are aggregated. | [optional] 
**date_bucket** | **str** | The date bucket of the KubernetesEfficiencyReport. | [optional] 
**groupings** | **list[str]** | Grouping values for aggregating costs on the KubernetesEfficiencyReport. Valid groupings: cluster_id, namespace, labeled, category, label, label:&lt;label_name&gt;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


