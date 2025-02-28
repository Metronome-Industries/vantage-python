# UpdateVirtualTagConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the VirtualTagConfig. | [optional] 
**overridable** | **bool** | Whether the VirtualTagConfig can override a provider-supplied tag on a matching Cost. | [optional] 
**backfill_until** | **date** | The earliest month the VirtualTagConfig should be backfilled to. | [optional] 
**values** | [**list[CreateVirtualTagConfigValues]**](CreateVirtualTagConfigValues.md) | Values for the VirtualTagConfig, with match precedence determined by order in the list. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


