# Shares

this is just an iterable of our individual share models.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**iterable** | [**List[Share]**](Share.md) | this is just an iterable of our individual share models. | 
**score** | [**Score**](Score.md) |  | [optional] 

## Example

```python
from openapi_client.models.shares import Shares

# TODO update the JSON string below
json = "{}"
# create an instance of Shares from a JSON string
shares_instance = Shares.from_json(json)
# print the JSON string representation of the object
print Shares.to_json()

# convert the object into a dict
shares_dict = shares_instance.to_dict()
# create an instance of Shares from a dict
shares_form_dict = shares.from_dict(shares_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


