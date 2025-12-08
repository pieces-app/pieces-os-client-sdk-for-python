# InstanceConfigurationAnalytics

Grouping of all analytics-related features.  This includes BigQuery and Segment integrations for tracking and reporting, as well as internal summary reports.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**big_query** | [**BigQueryInstanceConfiguration**](BigQueryInstanceConfiguration.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**segment** | [**SegmentInstanceConfiguration**](SegmentInstanceConfiguration.md) |  | [optional] 
**send_internal_summary_reports_to_user_team_service** | [**SendInternalSummaryReportsToUserTeamServiceInstanceConfiguration**](SendInternalSummaryReportsToUserTeamServiceInstanceConfiguration.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.instance_configuration_analytics import InstanceConfigurationAnalytics

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceConfigurationAnalytics from a JSON string
instance_configuration_analytics_instance = InstanceConfigurationAnalytics.from_json(json)
# print the JSON string representation of the object
print(InstanceConfigurationAnalytics.to_json())

# convert the object into a dict
instance_configuration_analytics_dict = instance_configuration_analytics_instance.to_dict()
# create an instance of InstanceConfigurationAnalytics from a dict
instance_configuration_analytics_from_dict = InstanceConfigurationAnalytics.from_dict(instance_configuration_analytics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


