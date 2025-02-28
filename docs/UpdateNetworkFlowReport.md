# UpdateNetworkFlowReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the NetworkFlowReport. | [optional] 
**filter** | **str** | The filter query language to apply to the NetworkFlowReport. Additional documentation available at https://docs.vantage.sh/vql. | [optional] 
**start_date** | **date** | The start date of the NetworkFlowReport. YYYY-MM-DD formatted. Incompatible with &#39;date_interval&#39; parameter. | [optional] 
**end_date** | **date** | The end date of the NetworkFlowReport. YYYY-MM-DD formatted. Incompatible with &#39;date_interval&#39; parameter. | [optional] 
**date_interval** | **str** | The date interval of the NetworkFlowReport. Unless &#39;custom&#39; is used, this is incompatible with &#39;start_date&#39; and &#39;end_date&#39; parameters. Defaults to &#39;last_7_days&#39;. | [optional] 
**groupings** | **list[str]** | Grouping values for aggregating data on the NetworkFlowReport. Valid groupings: account_id, az_id, dstaddr, dsthostname, flow_direction, interface_id, instance_id, peer_resource_uuid, peer_account_id, peer_vpc_id, peer_region, peer_az_id, peer_subnet_id, peer_interface_id, peer_instance_id, region, resource_uuid, srcaddr, srchostname, subnet_id, traffic_category, traffic_path, vpc_id. | [optional] 
**flow_direction** | **str** | The flow direction of the NetworkFlowReport. | [optional] 
**flow_weight** | **str** | The dimension by which the logs in the report are sorted. Defaults to costs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


