# MailgunDistribution

This is a specific Distribution for mailgun specific information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipients** | [**Recipients**](Recipients.md) |  | 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 

## Example

```python
from pieces_os_client.models.mailgun_distribution import MailgunDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of MailgunDistribution from a JSON string
mailgun_distribution_instance = MailgunDistribution.from_json(json)
# print the JSON string representation of the object
print MailgunDistribution.to_json()

# convert the object into a dict
mailgun_distribution_dict = mailgun_distribution_instance.to_dict()
# create an instance of MailgunDistribution from a dict
mailgun_distribution_from_dict = MailgunDistribution.from_dict(mailgun_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


