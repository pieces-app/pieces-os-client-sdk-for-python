<h1 align="center">
    <b>
        <a href="https://pieces.app">
            <picture>
                <source srcset="./assets/Logo-light-theme.png" media="(prefers-color-scheme: light)">
                <source srcset="./assets/Logo-dark-theme.png" media="(prefers-color-scheme: dark)">
                <img src="./assets/Logo-dark-theme.png" height="125" width="600" />
            </picture>
        </a><br>
    </b>
</h1>

# <p align="center"> Pieces OS Client SDK For Python
   <p align="center">
      <a href="https://github.com/pieces-app/pieces-os-client-sdk-for-python/graphs/contributors" alt="GitHub contributors">
         <img src="https://img.shields.io/github/contributors/pieces-app/pieces-os-client-sdk-for-python.svg" />
      </a>
      <a href="https://github.com/pieces-app/pieces-os-client-sdk-for-python/issues" alt="GitHub issues by-label">
         <img src="https://img.shields.io/github/issues/pieces-app/pieces-os-client-sdk-for-python" />
      </a>
      <a href="https://discord.gg/getpieces" alt="Discord">
         <img src="https://img.shields.io/badge/Discord-@layer5.svg?color=7389D8&label&logo=discord&logoColor=ffffff" />
      </a>
      <a href="https://twitter.com/getpieces" alt="Twitter Follow">
         <img src="https://img.shields.io/twitter/follow/pieces.svg?label=Follow" />
      </a>
      <a href="https://github.com/pieces-app/pieces-os-client-sdk-for-python/blob/main/LICENSE" alt="License">
         <img src="https://img.shields.io/github/license/pieces-app/pieces-os-client-sdk-for-python.svg" />
      </a>
      <a href="https://pypi.org/project/pieces_os_client" >
         <img src="https://badge.fury.io/py/pieces-os-client.svg" />
      </a>
      <a href="https://pepy.tech/project/pieces_os_client" >
         <img src="https://static.pepy.tech/badge/pieces_os_client" />
      </a>
   </p>
</p>


## Introduction

The Pieces SDK is a powerful code engine package designed for writing applications on top of Pieces OS. It facilitates communication with a locally hosted server to enable features such as copilot chats, asset saving, and more.

## Installation

To get started with the Pieces SDK, follow these steps:

1. **Download Pieces OS**: Pieces OS serves as the primary backend service, providing essential functionality for the SDK. Download the appropriate version for your operating system:
   - [macOS](https://docs.pieces.app/installation-getting-started/macos) 
   - [Windows](https://docs.pieces.app/installation-getting-started/windows) 
   - [Linux](https://docs.pieces.app/installation-getting-started/linux)

2. **Install the PyPI Package**: Use pip to install the Pieces SDK package:
   ```shell
   pip install pieces_os_client
   ```

## Usage
After installing the SDK, you can import the library into your project and start utilizing its features:

```shell
import pieces_os_client as pos_client
```
For detailed usage instructions and examples, refer to the [documentation](https://docs.pieces.app/build).

## Features
The Pieces SDK offers the following key features:

1. Copilot Chats: Communicate seamlessly with copilot chats functionality.
2. Asset Management: Save and manage assets and formats efficiently.
3. Local Server Interaction: Interact with a locally hosted server for various functionalities.
4. Multi LLMs support: Use any Pieces supported LLMs to power apps.

## Requirements
The Pieces SDK has the following system requirements:

- Pieces OS running as a backend service.
- Python environment with pip for installing the SDK package.

## Getting Started

First, we will create a Python script to test the connection to the Pieces OS server. This involves creating a `config.py` file to store your configuration info and a `wellknown.py` file to test the connection.

> It's important to note that the localhost port for Pieces OS is different based on the operating system.
> 
> For Linux, you should use `localhost:5323`.
>
> For macOS and Windows, you should use `localhost:1000`.

Create a `main.py` file and add this code to confirm you have installed the correct package:

```python title="main.py"
import pieces_os_client
import platform

# Defining the port based on the operating system. For Linux, the port is 5323, and for macOS/Windows, the port is 1000.
platform_info = platform.platform()
if 'Linux' in platform_info:
    port = 5323
else:
    port = 1000

# The `basePath` defaults to http://localhost:1000, however we need to change it to the correct port based on the operating system.
configuration = pieces_os_client.Configuration(host=f"http://localhost:{port}")

# Initialize the Pieces ApiClient
api_client = pieces_os_client.ApiClient(configuration)

# Enter a context with an instance of the ApiClient
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the WellKnownApi class
    api_instance = pieces_os_client.WellKnownApi(api_client)

    try:
        # Retrieve the (wellknown) health of the Pieces OS
        api_response = api_instance.get_well_known_health()
        print("The response of WellKnownApi().get_well_known_health:")
        print(api_response) # Response: ok
    except Exception as e:
        print("Exception when calling WellKnownApi->get_well_known_health: %s\n" % e)
```

Run the following command to execute the script:

```shell
python3 main.py
```

## Examples
Here are some examples of the basic endpoint for getting up and running: 


<details>
<summary>Connect</summary

   When developing and creating an application on top of Pieces OS, it is important that you authenticate with the application itself when performing requests.
   
   To 'connect' your application (this Python project) to the server, you will need to make a POST request to the `api_instance.connect()` endpoint of the API and print the response.

  ```python

# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.ConnectorApi(api_client)
    seeded_connector_connection = pieces_os_client.SeededConnectorConnection() # SeededConnectorConnection |  (optional)

    try:
        # /connect [POST]
        api_response = api_instance.connect(seeded_connector_connection=seeded_connector_connection)
        print("The response of ConnectorApi->connect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->connect: %s\n" % e) 
  ```
  
</details>

<details>
<summary>Create a new Asset</summary>
   When integrating your application with Pieces OS, creating a new asset is a fundamental task that enables you to manage your resources effectively. This code snippet demonstrates how to accomplish this task using the Pieces OS API.

   After establishing a connection with the API client and instantiating the Assets API class, you can call the `assets_create_new_asset` method to create the asset.You can customize the asset creation process by setting parameters such as `transferables` and `seed`.

   ```python

   # Enter a context with an instance of the API client
   with pieces_os_client.ApiClient(configuration) as api_client:
      # Create an instance of the API class
      api_instance = Assets API(api_client)
      transferables = True # bool | This is a boolean that will decided if we are want to return the transferable data (default) or not(performance enhancement) (optional)
      seed = pieces_os_client.Seed() # Seed |  (optional)

      try:
         # /assets/create [POST] Scoped to Asset
         api_response = api_instance.assets_create_new_asset(transferables=transferables, seed=seed)
         print("The response of AssetsApi->assets_create_new_asset:\n")
         pprint(api_response)
      except Exception as e:
         print("Exception when calling AssetsApi->assets_create_new_asset: %s\n" % e)

   ```
</details>

<details>
<summary>Get your Assets Snapshot</summary>

   When working with your app implementation you will often need to call the entire asset snapshot in order to get the correct snippet from your storage in Pieces OS. You can use this asset snapshot by passing the asset's ID and a boolean value indicating whether or not to return transferable data. The response from the API is then printed to the console.

```python
 
# Enter a context with an instance of the API client
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pieces_os_client.AssetApi(api_client)
    asset = '2254f2c8-5797-40e8-ac56-41166dc0e159' # str | The id (uuid) of the asset that you are trying to access.
    transferables = True # bool | This is a boolean that will decide if we want to return the transferable data (default) or not (performance enhancement) (optional)
    seeded_accessor = pieces_os_client.SeededAccessor() # SeededAccessor |  (optional)

    try:
         # api_instance.asset_snapshot(asset, transferables=transferables, seeded_accessor=seeded_accessor) [POST] Scoped to an Asset
        api_response = api_instance.asset_snapshot_post(asset, transferables=transferables, seeded_accessor=seeded_accessor)
        print("The response of AssetApi->asset_snapshot_post:\n")
        print(api_response)
    except Exception as e:
        print("Exception when calling AssetApi->asset_snapshot_post: %s\n" % e)
```
</details>


A developer documentation that outlines all the ins and outs of our available endpoints can be found [here](https://docs.pieces.app/build/reference/python/).

## Learn More / Support
Explore more about Pieces SDK and get help from the following resources:

- 🚀 [Getting Started Tutorial](https://docs.pieces.app/installation-getting-started/what-am-i-installing)
- 📜 [Pieces Docs](https://docs.pieces.app/build)
- 💬 [Discord Community](https://discord.gg/getpieces)

## License

This repository is available under the [MIT License](./LICENSE).


