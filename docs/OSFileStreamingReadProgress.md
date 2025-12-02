# OSFileStreamingReadProgress

This is the progress for the OSFileStreamingRead

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**total** | [**ByteDescriptor**](ByteDescriptor.md) |  | 
**transferred** | [**ByteDescriptor**](ByteDescriptor.md) |  | 

## Example

```python
from pieces_os_client.models.os_file_streaming_read_progress import OSFileStreamingReadProgress

# TODO update the JSON string below
json = "{}"
# create an instance of OSFileStreamingReadProgress from a JSON string
os_file_streaming_read_progress_instance = OSFileStreamingReadProgress.from_json(json)
# print the JSON string representation of the object
print(OSFileStreamingReadProgress.to_json())

# convert the object into a dict
os_file_streaming_read_progress_dict = os_file_streaming_read_progress_instance.to_dict()
# create an instance of OSFileStreamingReadProgress from a dict
os_file_streaming_read_progress_from_dict = OSFileStreamingReadProgress.from_dict(os_file_streaming_read_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


