# Pieces OS Client

This repo...

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