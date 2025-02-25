<h1 align="center">
    <b>
        <a href="https://pieces.app">
            <picture>
                <source srcset="https://github.com/user-attachments/assets/6d1c9fc1-11d5-47b0-bb39-a81d40d8fab0" media="(prefers-color-scheme: light)">
                <source srcset="https://github.com/user-attachments/assets/4529e56f-f614-4743-8ca8-33e0c040b069" media="(prefers-color-scheme: dark)">
                <img src="https://github.com/user-attachments/assets/4529e56f-f614-4743-8ca8-33e0c040b069" height="125" width="600" />
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

The Pieces OS Client SDK is a powerful code engine package designed for writing applications on top of Pieces OS. It facilitates communication with a locally hosted server to enable features such as copilot chats, asset saving, and more.

## Features
The Pieces SDK offers the following key features:

1. Copilot Chats: Communicate seamlessly with copilot chats functionality.
2. Asset Management: Save and manage assets and formats efficiently.
3. Local Server Interaction: Interact with a locally hosted server for various functionalities.
4. Multi LLMs support: Use any Pieces supported LLM to power your app.

## Installation

To get started with the Pieces OS Client SDK, follow these steps:

1. **Download Pieces OS**: Pieces OS serves as the primary backend service, providing essential functionality for the SDK. Download the appropriate version for your operating system:
   - [macOS](https://docs.pieces.app/installation-getting-started/macos) 
   - [Windows](https://docs.pieces.app/installation-getting-started/windows) 
   - [Linux](https://docs.pieces.app/installation-getting-started/linux)

2. **Install the SDK**: Use pip to install the Pieces OS Client SDK package:
   ```shell
   pip install pieces_os_client
   ```

## Basic Usage (Recommended)

The Pieces OS Client SDK has a built-in wrapper that simplifies the process of interacting with the Pieces OS server. Here's how you can get started with the wrapper.

### Initialize the Pieces Client

```python
from pieces_os_client.wrapper import PiecesClient

pieces_client = PiecesClient()
```

#### Custom Host URL

When we initialize the Pieces Client, it defaults to `http://localhost:1000` for macOS/Windows and `http://localhost:5323` for Linux. If you have a remote instance of Pieces OS running, you can specify the host URL when initializing the Pieces Client:

```python
from pieces_os_client.wrapper import PiecesClient

# Specify the host URL
host_url = "http://your-host-url:your-port"

pieces_client = PiecesClient(host=host_url)
```

### Create a New Asset

To create a new asset, you can use the `create_asset` method of the Pieces Client. Here's an example of how to create a new asset:

```python
from pieces_os_client.wrapper import PiecesClient
from pieces_os_client.models.classification_specific_enum import ClassificationSpecificEnum
from pieces_os_client.models.fragment_metadata import FragmentMetadata

pieces_client = PiecesClient()

# Set the content and metadata for the new asset
content = "print('Hello, World!')"
metadata = FragmentMetadata(ext=ClassificationSpecificEnum.PY) # optional metadata

# Create the new asset using the content and metadata
new_asset_id = pieces_client.create_asset(content, metadata)
print(f"Created asset with ID: {new_asset_id}")

# Close the client
pieces_client.close()
```

### Get All Assets

To get all your assets, you can use the `assets` method of the Pieces Client. Here's an example of how to get all your assets and print their names:

```python
from pieces_os_client.wrapper import PiecesClient

pieces_client = PiecesClient()

# Get all assets and print their names
assets = pieces_client.assets()
for asset in assets:
   print(f"Asset Name: {asset.name}")

# Close the client
pieces_client.close()
```

### Ask a Question to Pieces Copilot

To ask a question to Pieces Copilot and stream the response, you can use the `stream_question` method of the Pieces Client. Here's an example of how to ask a question and stream the response:

```python
from pieces_os_client.wrapper import PiecesClient

pieces_client = PiecesClient()

# Set the question you want to ask
question = "What is Object-Oriented Programming?"

# Ask the question and stream the response
for response in pieces_client.copilot.stream_question(question):
   if response.question:
         # Each answer is a chunk of the entire response to the question
         answers = response.question.answers.iterable
         for answer in answers:
            print(answer.text,end="")

# Close the client
pieces_client.close()
```

### Next Steps

You can explore more features and functionalities of the built-in wrapper by referring to the [Pieces OS Client Wrapper SDK documentation](https://docs.pieces.app/build/sdks/python).

## Advanced Usage (Not recommended)

If you want to use the Pieces OS Client SDK directly without the built-in wrapper, you can follow these steps to get started.

### Getting Started

First, we will create a Python script to test the connection to the Pieces OS server.

Create a python file and add the following code to confirm you can connect to your Pieces OS server:

```python
from pieces_os_client.api.well_known_api import WellKnownApi
import pieces_os_client
import platform

# Define the localhost port based on your operating system
# For Linux, use port 5323, for macOS/Windows, use port 1000
platform_info = platform.platform()
if 'Linux' in platform_info:
    port = 5323
else:
    port = 1000

# The `basePath` defaults to http://localhost:1000, but in this case we are checking the operating system to correctly set the port
configuration = pieces_os_client.Configuration(host=f"http://localhost:{port}")

# Initialize the Pieces ApiClient
api_client = pieces_os_client.ApiClient(configuration)

# Enter a context with an instance of the ApiClient
with pieces_os_client.ApiClient(configuration) as api_client:
    # Create an instance of the WellKnown API
    api_instance = WellKnownApi(api_client)

    try:
        # Retrieve the (wellknown) health of your Pieces OS server
        api_response = api_instance.get_well_known_health()
        print("The response of WellKnownApi().get_well_known_health:")
        print(api_response) # Response: ok
    except Exception as e:
        print("Exception when calling WellKnownApi->get_well_known_health: %s\n" % e)
```

A developer documentation that outlines all the ins and outs of our available endpoints can be found [here](https://docs.pieces.app/build/reference/python/).

## Learn More / Support
Explore more about Pieces SDK and get help from the following resources:

- 🚀 [Getting Started with Pieces](https://docs.pieces.app/installation-getting-started/what-am-i-installing)
- 📜 [Pieces Docs](https://docs.pieces.app/build)
- 💬 [Discord Community](https://discord.gg/getpieces)

## License

This repository is available under the [MIT License](./LICENSE).


