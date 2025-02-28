# Recommendation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**category** | **str** | The category of the Recommendation. | [optional] 
**workspace_token** | **str** | The token for the Workspace the Recommendation is a part of. | [optional] 
**provider** | **str** | The provider the Recommendation is for. | [optional] 
**provider_account_id** | **str** | The account ID of the provider. For Azure, this is the subscription ID. | [optional] 
**description** | **str** |  | [optional] 
**potential_savings** | **str** | The monthly potential savings of the Recommendation. | [optional] 
**service** | **str** | The service the Recommendation is for. | [optional] 
**created_at** | **str** | The date and time, in UTC, the Recommendation was created. ISO 8601 Formatted. | [optional] 
**resources_affected_count** | **str** | The number of ProviderResources related to the Recommendation. Use the &#x60;recommendations/:token/resources&#x60; endpoint to get the full list of resources. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


