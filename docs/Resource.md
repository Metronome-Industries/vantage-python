# Resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**uuid** | **str** | The unique identifier for the resource. | [optional] 
**type** | **str** | The kind of resource. | [optional] 
**label** | **str** |  | [optional] 
**metadata** | **str** | Type-specific attributes of the resource. | [optional] 
**account_id** | **str** | The provider account where the resource is located. | [optional] 
**billing_account_id** | **str** | The provider billing account this resource is charged to. | [optional] 
**provider** | **str** | The provider of the resource. | [optional] 
**region** | **str** | The region where the resource is located. Region values are specific to each provider. | [optional] 
**costs** | [**list[ResourceCost]**](ResourceCost.md) | The cost of the resource broken down by category. | [optional] 
**created_at** | **str** | The date and time when Vantage first observed the resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


