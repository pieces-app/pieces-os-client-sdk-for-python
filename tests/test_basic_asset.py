import pytest
from unittest.mock import Mock, patch, MagicMock
from pieces_os_client import Asset, Format, ClassificationGenericEnum, ClassificationSpecificEnum, Annotations, Annotation
from datetime import datetime
import sys
import importlib.util
from pieces_os_client_wrapper.basic_identifier import BasicAsset
from pieces_os_client_wrapper.streamed_identifiers.assets_snapshot import AssetSnapshot
from pieces_os_client_wrapper.client import PiecesClient

class BasicAssetTest(BasicAsset):
    def __init__(self, id) -> None:
        self.asset:Asset = AssetSnapshot.identifiers_snapshot.get(id)
        if not self.asset:
            print(f"Asset not found for ID: {id}")
            print("Available IDs in AssetSnapshot.identifiers_snapshot:", AssetSnapshot.identifiers_snapshot.keys())
            raise ValueError("Asset not found")

@pytest.fixture(scope="function")
def pieces_client():
    return PiecesClient(config={'baseUrl': 'http://localhost:1000'})

@pytest.fixture(scope="function", autouse=True)
def setup_asset_snapshot(pieces_client):
    AssetSnapshot.identifiers_snapshot = {}
    print("Before test:", AssetSnapshot.identifiers_snapshot)
    yield
    print("After test:", AssetSnapshot.identifiers_snapshot)
    AssetSnapshot.identifiers_snapshot = {}

@pytest.fixture
def mock_asset():
    mock = MagicMock(spec=Asset)
    mock.id = "test_asset_id"
    mock.name = "Test Asset"
    mock.original = MagicMock()
    mock.original.reference.fragment.string.raw = "Test content"
    mock.original.reference.classification.specific = ClassificationSpecificEnum.PY
    mock.original.reference.classification.generic = ClassificationGenericEnum.CODE
    mock.formats = MagicMock()
    mock.formats.iterable = []
    return mock

@pytest.fixture
def mock_asset_snapshot(mock_asset):
    AssetSnapshot.identifiers_snapshot[mock_asset.id] = mock_asset
    print(f"Added mock asset with ID {mock_asset.id} to AssetSnapshot.identifiers_snapshot")
    return AssetSnapshot

def test_basic_asset_initialization(mock_asset_snapshot, mock_asset):
    print("In test_basic_asset_initialization:")
    print("AssetSnapshot.identifiers_snapshot:", AssetSnapshot.identifiers_snapshot)
    print("mock_asset.id:", mock_asset.id)
    asset = BasicAsset(mock_asset.id)
    assert asset.asset == mock_asset

def test_raw_content_property(mock_asset_snapshot, mock_asset):
    asset = BasicAsset(mock_asset.id)
    assert asset.raw_content == "Test content"

def test_is_image(mock_asset_snapshot, mock_asset):
    asset = BasicAsset(mock_asset.id)
    assert not asset.is_image

    mock_asset.original.reference.classification.generic = ClassificationGenericEnum.IMAGE
    assert asset.is_image

def test_classification_property(mock_asset_snapshot, mock_asset):
    asset = BasicAsset(mock_asset.id)
    assert asset.classification == ClassificationSpecificEnum.PY

def test_edit_content(mock_asset_snapshot, mock_asset, pieces_client):
    asset = BasicAsset(mock_asset.id)
    new_content = "Updated content"
    
    with patch.object(pieces_client, 'format_api') as mock_format_api:
        mock_format = MagicMock(spec=Format)
        mock_format.classification = MagicMock()
        mock_format.classification.generic = ClassificationGenericEnum.CODE
        mock_format.fragment = MagicMock()
        mock_format.fragment.string = MagicMock()
        mock_format.fragment.string.raw = "Test content"
        mock_format_api.format_snapshot.return_value = mock_format
        
        asset.raw_content = new_content
        
        mock_format_api.format_update_value.assert_called_once()
        assert mock_format.fragment.string.raw == new_content

def test_edit_name(mock_asset_snapshot, mock_asset, pieces_client):
    asset = BasicAsset(mock_asset.id)
    new_name = "New Asset Name"
    
    with patch.object(pieces_client, 'asset_api') as mock_asset_api:
        asset.name = new_name
        
        assert asset.asset.name == new_name
        mock_asset_api.asset_update.assert_called_once()

def test_name_property(mock_asset_snapshot, mock_asset):
    asset = BasicAsset(mock_asset.id)
    assert asset.name == "Test Asset"
    
    mock_asset.name = None
    assert asset.name == "Unnamed snippet"

def test_description_property(mock_asset_snapshot, mock_asset):
    asset = BasicAsset(mock_asset.id)
    mock_annotation = MagicMock(spec=Annotation)
    mock_annotation.type = "DESCRIPTION"
    mock_annotation.text = "Test description"
    mock_annotation.updated = MagicMock()
    mock_annotation.updated.value = datetime.now()
    mock_annotations = [
        mock_annotation,
        MagicMock(spec=Annotation, type="OTHER", text="Other annotation", updated=MagicMock(value=datetime.now()))
    ]
    mock_asset.annotations = MagicMock(spec=Annotations, iterable=mock_annotations)
    
    assert asset.description == "Test description"

def test_annotations_property(mock_asset_snapshot, mock_asset):
    asset = BasicAsset(mock_asset.id)
    mock_annotations = [MagicMock(spec=Annotation), MagicMock(spec=Annotation)]
    mock_asset.annotations = MagicMock(spec=Annotations, iterable=mock_annotations)
    
    assert asset.annotations == mock_annotations

def test_delete(mock_asset_snapshot, mock_asset, pieces_client):
    asset = BasicAsset(mock_asset.id)
    with patch.object(pieces_client, 'assets_api') as mock_assets_api:
        asset.delete()
        mock_assets_api.assets_delete_asset.assert_called_once_with(mock_asset.id)

def test_create(pieces_client):
    with patch.object(pieces_client, 'assets_api') as mock_assets_api:
        mock_assets_api.assets_create_new_asset.return_value = MagicMock(id="new_asset_id")
        
        new_asset_id = BasicAsset.create("New asset content")
        
        assert new_asset_id == "new_asset_id"
        mock_assets_api.assets_create_new_asset.assert_called_once()
