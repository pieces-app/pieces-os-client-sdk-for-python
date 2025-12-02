# SendInternalSummaryReportsToUserTeamServiceInstanceConfiguration

Configuration for sending internal summary reports to the user team service  note: this model can scale to use cadence and so on in the future

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | [**InstanceConfigurationEnabledEnum**](InstanceConfigurationEnabledEnum.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.send_internal_summary_reports_to_user_team_service_instance_configuration import SendInternalSummaryReportsToUserTeamServiceInstanceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of SendInternalSummaryReportsToUserTeamServiceInstanceConfiguration from a JSON string
send_internal_summary_reports_to_user_team_service_instance_configuration_instance = SendInternalSummaryReportsToUserTeamServiceInstanceConfiguration.from_json(json)
# print the JSON string representation of the object
print(SendInternalSummaryReportsToUserTeamServiceInstanceConfiguration.to_json())

# convert the object into a dict
send_internal_summary_reports_to_user_team_service_instance_configuration_dict = send_internal_summary_reports_to_user_team_service_instance_configuration_instance.to_dict()
# create an instance of SendInternalSummaryReportsToUserTeamServiceInstanceConfiguration from a dict
send_internal_summary_reports_to_user_team_service_instance_configuration_from_dict = SendInternalSummaryReportsToUserTeamServiceInstanceConfiguration.from_dict(send_internal_summary_reports_to_user_team_service_instance_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


