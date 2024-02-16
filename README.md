#  Pieces OS Client
[![PyPI version](https://badge.fury.io/py/pieces-os-client.svg)](https://badge.fury.io/py/pieces-os-client)
[![Downloads](https://static.pepy.tech/badge/pieces_os_client)](https://pepy.tech/project/pieces_os_client)

<h1 align="center">
   <b>
        <a href="https://pieces.app"><img src="https://storage.googleapis.com/pieces_static_resources/pfd_wiki/PIECES_MAIN_LOGO_WIKI.png" /></a><br>
    </b>
</h1>

<p align="center">Powerful code engine package for writing applications on top of Pieces OS and communicated with the locally hosted server to create copilot chats, to save assets + formats and more.</p>

<p align="center">
	<a href="https://pieces.app"><b>Website</b></a> •
	<a href="https://docs.pieces.app"><b>Documentation</b></a>
</p>

## Table of Contents

- [Operating System Support](#-operating-system-support)
- [Installing](#-installing)
    - [Pieces OS](#-pieces-os)
    - [Downloading PyPI Package](#-downloading-pypi-package)
    - [Starter Project](#starter-project)
- [Testing Usage](#testing-usage)
- [Examples](#examples)
    - [/connect](#connect)
    - [Asset + /assets](#creating-with-asset--assets)
    - [SeededAsset](#seededasset)
    - [/assets/create](#using-assetscreate)
    - [/assets/snapshot](#get-your-assets-snapshot)
    - [/asset/update](#update-your-assets-metadata-or-properties)
    - [/assets/delete](#deleting-an-asset)
- [Releases](#releases)
- [Contributing](#contributing)
- [Supported Versions](#supported-versions-)


## Operating System Support
Currently, Pieces OS is utilized as the primary backend service with [Pieces for Developers](https://docs.pieces.app/installation-getting-started/what-am-i-installing) that powers all of the features that can be used there. Both programs are designed for full support by all operating systems, although our [Linux Platform](https://docs.pieces.app/installation-getting-started/linux) is available, it leans towards a 'heavily supported beta' and may experience incremental issues on specific flavors of linux.

> if you have any issues on any Linux flavor be sure to check our list of supported distributions on the [linux documentation page](https://docs.pieces.app/installation-getting-started/linux).

## Installing
When developing on the Pieces platform, you need two primary things:

1. **Download the Pieces OS application**
2. **Install the pypi package**

## Pieces OS
Pieces OS runs in the background of your computer and serves as a hub for all plugins and extensions developed by the team. In order to utilize your own Server locally and support all the functionality that powers things like [Global Search](https://docs.pieces.app/features/global-search), [Copilot Chats](https://docs.pieces.app/features/pieces-copilot), [Asset Saving](https://docs.pieces.app/features/managing-saved-materials), [context](https://docs.pieces.app/features/pieces-copilot#set-your-own-copilot-context), and more.

Select the right version to download Pieces OS for your operating system:
- [macOS](https://docs.pieces.app/installation-getting-started/macos) - [Compatible with macOS 11 Big Sur or higher]
- [Windows](https://docs.pieces.app/installation-getting-started/windows) - [Compatible with Windows 10 version 1809 or higher]
- [Linux](https://docs.pieces.app/installation-getting-started/linux) - [Compatible with Ubuntu 18 or Higher]

You can also visit our user-facing documentation to learn more about different features that are available now to give you an idea of some of the things that you can potentially do. 

## Downloading PyPI Package 
Using pip: 

```python
pip install pieces-os-client
```

After you install the package, you  can import the library into your project:

```python
from pieces_os_client.models
``` 

## Starter Project

Coming soon...

## Testing Usage
Following the initial download and light configuration, you can perform a simple test to ensure that both **Pieces OS** is running and that **you also have correctly installed the PyPI package**.

Create a wellknown.py file and add this code to confirm you have installed the correct package:

```python
# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.WellKnownApi(api_client)

    try:
        # /.well-known/version [Get]
        api_response = api_instance.get_well_known_version()
        print("The response of WellKnownApi->get_well_known_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellKnownApi->get_well_known_version: %s\n" % e)
``` 

**Your output should appear on your IDE terminal stating the version of the Pieces OS installed.**

## Examples
Here are a few examples of using some of the basic endpoints for getting up and running, along with creating an asset for the first time. 

A developer documentation that outlines all the ins and outs of our available endpoints can be found [here](https://github.com/pieces-app/pieces-os-client-sdk-for-python/tree/main/docs/docs).

### `/connect`
When developing and creating an application on top of Pieces OS, it is important that you authenticate with the application itself when performing requests.

To 'connect' your application (this python project) to the server, you will need to make a POST request to /connect endpoint of the API and print the response. 


```python
# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.ConnectorApi(api_client)
    seeded_connector_connection = pieces_os_client.SeededConnectorConnection() 
    # SeededConnectorConnection |  (optional)

    try:
        # /connect [POST]
        api_response = api_instance.connect(seeded_connector_connection=seeded_connector_connection)
        print("The response of ConnectorApi->connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->connect: %s\n" % e)       
```

### Creating with `Asset` & `/Assets`
**Asset** is a very important model who's primary purpose is to manage the seeded data that comes in to the application, and is stored inside of Pieces OS. Each asset is identifiable as a piece of saved data, or pre-seeded data.

**/Assets** is equally important, but instead of containing a single asset with parameters storing data on it, Assets serves as the list of `type: Asset` objects that are stored there. Also, you will find the operations for adding, deleting, searching, and other functions that are related to referencing a number of different snippets to make a comparison.

### `SeededAsset`
SeededAsset is the **Format** needed by `/assets/create` in order to accept the snippet, create, and return the information you need. The structure (at bare minimum is as follows):

```python
from pieces_os_client.models.seeded_asset import SeededAsset

# TODO update the JSON string below
json = "{}"
# create an instance of SeededAsset from a JSON string
seeded_asset_instance = SeededAsset.from_json(json)
# print the JSON string representation of the object
print SeededAsset.to_json()

# convert the object into a dict
seeded_asset_dict = seeded_asset_instance.to_dict()
# create an instance of SeededAsset from a dict
seeded_asset_form_dict = seeded_asset.from_dict(seeded_asset_dict)
``` 

### Get your Assets Snapshot
When working with your app implementation you will often need to call the entire asset snapshot in order to get the correct snippet from your storage in Pieces OS. You can use this asset snapshot by passing the asset's ID and a boolean value indicating whether or not to return transferable data.
The response from the API is then printed to the console.

```python
# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    seeded_accessor = pieces_os_client.SeededAccessor() # SeededAccessor |  (optional)

    try:
        # /asset/{asset} [POST] Scoped to an Asset
        api_response = api_instance.asset_snapshot_post(asset, transferables=transferables, seeded_accessor=seeded_accessor)
        print("The response of AssetApi->asset_snapshot_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_snapshot_post: %s\n" % e)
``` 

### Updating your Assets
Individual assets can be manipulated with a number of different properties and metadata. You can add **titles**, **annotations**, **tags**, **links**, **anchors**, and much more all through this single endpoint. 
To use the assest_update method of the AssetAPi class, pass a boolean value for `transferables` and an instance of the Asset class for the `asset`. It should update the assest in the database and print the response from the API call. 

```python
# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.AssetApi(api_client)
    transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
    asset = pieces_os_client.Asset() # Asset | This is the updated Asset that needs to be updated in our db. (optional)

    try:
        # /asset/update [POST] Scoped to Asset
        api_response = api_instance.asset_update(transferables=transferables, asset=asset)
        print("The response of AssetApi->asset_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_update: %s\n" % e)
``` 

### Deleting an Asset
Similar to the previous example, you need assetSnapshot in order to access the proper asset on your list of data. You can use this endpoint to completely delete a specific asset where ever it may be in the list of all of your assets by taking a uid to delete out of the assets table. 

```python
# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.AssetsApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.

    try:
        # /assets/delete [POST] Scoped to Asset
        api_response = api_instance.assets_delete_asset(asset)
        print("The response of AssetsApi->assets_delete_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->assets_delete_asset: %s\n" % e)
``` 


## Releases
The release pipeline will trigger when a tag is pushed to main.

## Contributing

This project uses poetry for managing dependencies and builds. Install poetry with:
```shell
pip install poetry
```

Then use poetry to install the required dependencies
```shell
poetry install
```

You build with 
```shell
poetry build
```

Finally any project dependencies should be added to the pyproject.toml file with
```shell
poetry add 
```

these can be local/github/pypi etc.


## Supported Versions 
**It is recommended to always stay up to date with the latest production release of Pieces OS.**

If you are limited on updating versions due to development progress or needing to remain on a specific version - try to remain on the same _minor version_ to avoid any issues. If you start to encounter issues, please update to the next available version when receiving errors.
