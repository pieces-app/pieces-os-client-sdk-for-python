# OSFileStreamingRead

This is a model to return stream progress for a file read.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes** | [**TransferableBytes**](TransferableBytes.md) |  | [optional] 
**id** | **str** | This is a generated UUID that represents this current stream in progress(can be used to cancel this in the future) | 
**path** | **str** |  | 
**percentage** | **float** | Optionally if the download is in progress you will receive a download percent(from 0-100). | [optional] 
**progress** | [**OSFileStreamingReadProgress**](OSFileStreamingReadProgress.md) |  | [optional] 
**var_schema** | [**EmbeddedModelSchema**](EmbeddedModelSchema.md) |  | [optional] 
**status** | [**ModelDownloadProgressStatusEnum**](ModelDownloadProgressStatusEnum.md) |  | 

## Example

```python
from pieces_os_client.models.os_file_streaming_read import OSFileStreamingRead

# TODO update the JSON string below
json = "{}"
# create an instance of OSFileStreamingRead from a JSON string
os_file_streaming_read_instance = OSFileStreamingRead.from_json(json)
# print the JSON string representation of the object
print(OSFileStreamingRead.to_json())

# convert the object into a dict
os_file_streaming_read_dict = os_file_streaming_read_instance.to_dict()
# create an instance of OSFileStreamingRead from a dict
os_file_streaming_read_from_dict = OSFileStreamingRead.from_dict(os_file_streaming_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


