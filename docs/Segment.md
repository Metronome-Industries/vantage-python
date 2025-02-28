# Segment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**title** | **str** | The title of the Segment. | [optional] 
**parent_segment_token** | **str** | The token of the parent Segment of this Segment. | [optional] 
**description** | **str** | The description of the Segment. | [optional] 
**track_unallocated** | **bool** | Track Unallocated Costs which are not assigned to any of the created Segments. | [optional] 
**report_settings** | [**SegmentReportSettings**](SegmentReportSettings.md) |  | [optional] 
**priority** | **int** | Costs are assigned in priority order across all Segments with assigned filters. | [optional] 
**filter** | **str** | The filter applied to the Segment. Additional documentation available at https://docs.vantage.sh/vql. | [optional] 
**created_at** | **str** | The date and time, in UTC, the Segment was created. ISO 8601 Formatted. | [optional] 
**workspace_token** | **str** | The token for the Workspace the Segment is a part of. | [optional] 
**report_token** | **str** | The token for the Report the Segment has generated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


