# VirtualTagConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The token of the VirtualTagConfig. | [optional] 
**created_by_token** | **str** | The token of the Creator of the VirtualTagConfig. | [optional] 
**key** | **str** | The key of the VirtualTagConfig. | [optional] 
**overridable** | **bool** | Whether the VirtualTagConfig can override a provider-supplied tag on a matching Cost. | [optional] 
**backfill_until** | **str** | The earliest month VirtualTagConfig should be backfilled to. | [optional] 
**values** | [**list[VirtualTagConfigValue]**](VirtualTagConfigValue.md) | Values for the VirtualTagConfig, with match precedence determined by their relative order in the list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


