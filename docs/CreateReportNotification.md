# CreateReportNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the ReportNotification. | 
**cost_report_token** | **str** | The CostReport token. | 
**workspace_token** | **str** | The token of the Workspace to add the ReportNotification to. Required if the API token is associated with multiple Workspaces. | [optional] 
**user_tokens** | **list[str]** | The Users that receive the notification. | [optional] 
**recipient_channels** | **list[str]** | The Slack or Microsoft Teams channels that receive the notification. | [optional] 
**frequency** | **str** | The frequency the ReportNotification is sent. Possible values: daily, weekly, monthly. | 
**change** | **str** | The type of change the ReportNotification is tracking. Possible values: percentage, dollars. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


