import pytest
from unittest.mock import Mock, patch, MagicMock
from pieces_os_client import (Asset,
    Format,
    ClassificationGenericEnum,
    ClassificationSpecificEnum,
    Annotations,
    Annotation,
    Linkify,
    AssetReclassification,
    Shares)
from datetime import datetime
from pieces_os_client.wrapper.basic_identifier import BasicAsset
from pieces_os_client.wrapper.streamed_identifiers.assets_snapshot import AssetSnapshot

class TestBasicAsset:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.mock_asset = Mock(spec=Asset)
        self.mock_asset.id = "test_asset_id"
        self.mock_asset.name = "Test Asset"
        self.mock_asset.original = Mock()
        self.mock_asset.original.reference.fragment.string.raw = "Test content"
        self.mock_asset.original.reference.classification.specific = ClassificationSpecificEnum.PY
        self.mock_asset.original.reference.classification.generic = ClassificationGenericEnum.CODE
        self.mock_asset.formats = Mock()
        self.mock_asset.formats.iterable = []
        AssetSnapshot.identifiers_snapshot = {"test_asset_id": self.mock_asset}
        AssetSnapshot.pieces_client = Mock()

    def test_basic_asset_initialization(self):
        asset = BasicAsset("test_asset_id")
        assert asset.id == "test_asset_id"
        assert asset.asset == self.mock_asset

    def test_basic_asset_initialization_invalid_id(self):
        with pytest.raises(ValueError, match="Asset not found"):
            BasicAsset("invalid_id").asset

    def test_raw_content_property(self):
        asset = BasicAsset("test_asset_id")
        assert asset.raw_content == "Test content"

    def test_is_image(self):
        asset = BasicAsset("test_asset_id")
        assert not asset.is_image

        self.mock_asset.original.reference.classification.generic = ClassificationGenericEnum.IMAGE
        assert asset.is_image

    def test_classification_property(self):
        asset = BasicAsset("test_asset_id")
        assert asset.classification == ClassificationSpecificEnum.PY

    def test_edit_content(self):
        asset = BasicAsset("test_asset_id")
        new_content = "Updated content"

        with patch.object(AssetSnapshot.pieces_client, 'format_api') as mock_format_api:
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

    def test_edit_name(self):
        asset = BasicAsset("test_asset_id")
        new_name = "New Asset Name"

        with patch.object(AssetSnapshot.pieces_client, 'asset_api') as mock_asset_api:
            asset.name = new_name

            assert asset.asset.name == new_name
            mock_asset_api.asset_update.assert_called_once()

    def test_name_property(self):
        asset = BasicAsset("test_asset_id")
        assert asset.name == "Test Asset"

        self.mock_asset.name = None
        assert asset.name == "Unnamed snippet"

    def test_description_property(self):
        asset = BasicAsset("test_asset_id")
        mock_annotation = MagicMock(spec=Annotation)
        mock_annotation.type = "DESCRIPTION"
        mock_annotation.text = "Test description"
        mock_annotation.updated = MagicMock()
        mock_annotation.updated.value = datetime.now()
        mock_annotations = [
            mock_annotation,
            MagicMock(spec=Annotation, type="OTHER", text="Other annotation", updated=MagicMock(value=datetime.now()))
        ]
        self.mock_asset.annotations = MagicMock(spec=Annotations, iterable=mock_annotations)

        assert asset.description == "Test description"

    def test_annotations_property(self):
        asset = BasicAsset("test_asset_id")
        mock_annotations = [MagicMock(spec=Annotation), MagicMock(spec=Annotation)]
        self.mock_asset.annotations = MagicMock(spec=Annotations, iterable=mock_annotations)

        assert asset.annotations == mock_annotations

    def test_delete(self):
        asset = BasicAsset("test_asset_id")
        with patch.object(AssetSnapshot.pieces_client, 'assets_api') as mock_assets_api:
            asset.delete()
            mock_assets_api.assets_delete_asset.assert_called_once_with("test_asset_id")

    def test_create(self):
        raw_content = "New asset content"
        mock_seed = MagicMock()
        
        with patch.object(BasicAsset, '_get_seed', return_value=mock_seed) as mock_get_seed, \
             patch.object(AssetSnapshot.pieces_client.assets_api, 'assets_create_new_asset') as mock_create_new_asset:
            
            mock_create_new_asset.return_value = MagicMock(id="new_asset_id")
            
            new_asset_id = BasicAsset.create(raw_content)
            
            mock_get_seed.assert_called_once_with(raw_content, None)
            mock_create_new_asset.assert_called_once_with(transferables=False, seed=mock_seed)
            assert new_asset_id == "new_asset_id"

    def test_share_with_asset(self):
        asset = BasicAsset("test_asset_id")
        mock_user_profile = MagicMock()
        mock_user_profile.allocation = True

        with patch('pieces_os_client.wrapper.basic_identifier.BasicUser.user_profile', mock_user_profile), \
             patch.object(AssetSnapshot.pieces_client.linkfy_api, 'linkify') as mock_linkify:

            mock_linkify.return_value = "shareable_link"

            shareable_link = asset._share(asset=asset.asset)

            mock_linkify.assert_called_once_with(
                linkify=Linkify(
                    access="PUBLIC",
                    asset=asset.asset
                )
            )
            assert shareable_link == "shareable_link"

    def test_share_with_seed(self):
        mock_seed = MagicMock()
        mock_user_profile = MagicMock()
        mock_user_profile.allocation = True

        with patch('pieces_os_client.wrapper.basic_identifier.BasicUser.user_profile', mock_user_profile), \
             patch.object(AssetSnapshot.pieces_client.linkfy_api, 'linkify') as mock_linkify:
            
            mock_linkify.return_value = "shareable_link"

            shareable_link = BasicAsset._share(seed=mock_seed)

            mock_linkify.assert_called_once_with(
                linkify=Linkify(
                    access="PUBLIC",
                    seed=mock_seed
                )
            )
            assert shareable_link == "shareable_link"

    def test_share_without_user_profile(self):
        basic_asset = BasicAsset("test_asset_id")

        with patch('pieces_os_client.wrapper.basic_identifier.BasicUser.user_profile', None):
            with pytest.raises(PermissionError, match="You need to be logged in to generate a shareable link"):
                basic_asset._share(asset=basic_asset.asset)

    def test_share_without_allocation(self):
        basic_asset = BasicAsset("test_asset_id")
        mock_user_profile = MagicMock()
        mock_user_profile.allocation = False

        with patch('pieces_os_client.wrapper.basic_identifier.BasicUser.user_profile', mock_user_profile):
            with pytest.raises(PermissionError, match="You need to connect to the cloud to generate a shareable link"):
                basic_asset._share(asset=basic_asset.asset)

    def test_classification_setter(self):
        asset = BasicAsset("test_asset_id")
        new_classification = ClassificationSpecificEnum.JS

        with patch.object(AssetSnapshot.pieces_client.asset_api, 'asset_reclassify') as mock_reclassify:
            asset.classification = new_classification

            mock_reclassify.assert_called_once_with(
                asset_reclassification=AssetReclassification(
                    ext=new_classification, asset=asset.asset),
                transferables=False
            )

    def test_classification_setter_with_string(self):
        asset = BasicAsset("test_asset_id")
        new_classification = "js"

        with patch.object(AssetSnapshot.pieces_client.asset_api, 'asset_reclassify') as mock_reclassify:
            asset.classification = new_classification

            mock_reclassify.assert_called_once_with(
                asset_reclassification=AssetReclassification(
                    ext=ClassificationSpecificEnum.JS, asset=asset.asset),
                transferables=False
            )

    def test_classification_setter_invalid_classification(self):
        asset = BasicAsset("test_asset_id")

        with pytest.raises(ValueError, match="Invalid classification"):
            asset.classification = 123

    def test_classification_setter_image_reclassification(self):
        asset = BasicAsset("test_asset_id")
        self.mock_asset.original.reference.classification.generic = ClassificationGenericEnum.IMAGE

        with pytest.raises(NotImplementedError, match="Error in reclassify asset: Image reclassification is not supported"):
            asset.classification = ClassificationSpecificEnum.JS

    def test_share(self):
        asset = BasicAsset("test_asset_id")
        mock_shares = Mock(spec=Shares)

        with patch.object(BasicAsset, '_share', return_value=mock_shares) as mock_share:
            result = asset.share()

            mock_share.assert_called_once_with(asset.asset)
            assert result == mock_shares

    def test_share_raw_content(self):
        raw_content = "Test raw content"
        mock_seed = Mock()
        mock_shares = Mock(spec=Shares)

        with patch.object(BasicAsset, '_get_seed', return_value=mock_seed) as mock_get_seed, \
             patch.object(BasicAsset, '_share', return_value=mock_shares) as mock_share:

            result = BasicAsset.share_raw_content(raw_content)

            mock_get_seed.assert_called_once_with(raw_content)
            mock_share.assert_called_once_with(seed=mock_seed)
            assert result == mock_shares

    def test_search(self):
        query = "test query"
        mock_result = Mock()
        mock_result.iterable = [
            Mock(exact=True, identifier="exact_id"),
            Mock(exact=False, identifier="suggested_id")
        ]

        with patch.object(AssetSnapshot.pieces_client.search_api, 'full_text_search', return_value=mock_result) as mock_fts, \
             patch.object(BasicAsset, '__init__', return_value=None) as mock_init:

            results = BasicAsset.search(query)

            mock_fts.assert_called_once_with(query=query)
            assert len(results) == 2
            mock_init.assert_any_call("exact_id")
            mock_init.assert_any_call("suggested_id")

    def test_search_ncs(self):
        query = "test query"
        mock_result = Mock()
        mock_result.iterable = [
            Mock(exact=True, identifier="exact_id"),
            Mock(exact=False, identifier="suggested_id")
        ]

        with patch.object(AssetSnapshot.pieces_client.search_api, 'neural_code_search', return_value=mock_result) as mock_ncs, \
                patch.object(BasicAsset, '__init__', return_value=None) as mock_init:

            results = BasicAsset.search(query, search_type="ncs")

            mock_ncs.assert_called_once_with(query=query)
            assert len(results) == 2
            mock_init.assert_any_call("exact_id")
            mock_init.assert_any_call("suggested_id")

    def test_search_fuzzy(self):
        query = "test query"
        mock_result = Mock()
        mock_result.iterable = [
            Mock(exact=True, identifier="exact_id"),
            Mock(exact=False, identifier="suggested_id")
        ]

        with patch.object(AssetSnapshot.pieces_client.assets_api, 'search_assets', return_value=mock_result) as mock_fuzzy, \
             patch.object(BasicAsset, '__init__', return_value=None) as mock_init:

            results = BasicAsset.search(query, search_type="fuzzy")

            mock_fuzzy.assert_called_once_with(query=query, transferables=False)
            assert len(results) == 2
            mock_init.assert_any_call("exact_id")
            mock_init.assert_any_call("suggested_id")

    @patch('pieces_os_client.wrapper.client.PiecesClient')
    def test_pieces_os_not_running(self, mock_pieces_client_class):
        mock_client = mock_pieces_client_class.return_value
        mock_client.is_pieces_running = Mock(return_value=False)
        
        # Create a mock copilot that raises ValueError when Pieces OS is not running
        mock_copilot = MagicMock()
        mock_copilot.question.side_effect = ValueError("Pieces OS is not running")
        mock_client.copilot = mock_copilot

        c = mock_client

        assert not c.is_pieces_running()

        with pytest.raises(ValueError, match="Pieces OS is not running"):
            c.copilot.question("HI")

    @patch('pieces_os_client.wrapper.client.PiecesClient')
    def test_open_pieces_os(self, mock_pieces_client_class):
        mock_client = mock_pieces_client_class.return_value
        mock_client.is_pieces_running = Mock(side_effect=[False, True])
        mock_client.open_pieces_os = Mock(return_value=True)

        c = mock_client

        assert not c.is_pieces_running()
        assert c.open_pieces_os()
        assert c.is_pieces_running()

    @patch('pieces_os_client.wrapper.client.PiecesClient')
    def test_copilot_after_pieces_os_running(self, mock_pieces_client_class):
        mock_client = mock_pieces_client_class.return_value
        mock_client.is_pieces_running = Mock(return_value=True)
        mock_client.copilot = MagicMock()

        c = mock_client

        assert c.is_pieces_running()
        
        c.copilot.question("HI")
        mock_client.copilot.question.assert_called_once_with("HI")
        
if __name__ == '__main__':
    pytest.main([__file__])

