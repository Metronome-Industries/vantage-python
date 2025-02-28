# UpdateSegment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the Segment. | [optional] 
**description** | **str** | The description of the Segment. | [optional] 
**priority** | **int** | The priority of the Segment. | [optional] 
**track_unallocated** | **bool** | Track Unallocated Costs which are not assigned to any of the created Segments. | [optional] [default to False]
**report_settings** | [**CreateSegmentReportSettings**](CreateSegmentReportSettings.md) |  | [optional] 
**filter** | **str** | The filter query language to apply to the Segment. Additional documentation available at https://docs.vantage.sh/vql. | [optional] 
**parent_segment_token** | **str** | The token of the parent Segment this new Segment belongs to. Determines the Workspace the segment is assigned to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


