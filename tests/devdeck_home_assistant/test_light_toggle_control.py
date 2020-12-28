import vcr
from devdeck_core.mock_deck_context import mock_context, assert_rendered
from tests.testing_utils import TestingUtils

from devdeck_home_assistant.light_toggle_control import LightToggleControl


class TestLightToggleControl:
    @vcr.use_cassette('tests/fixtures/test_light_toggle/test_initialize_sets_icon.yaml')
    def test_initialize_sets_icon(self):
        settings = {
            'api_key': 'my_secret_api_key',
            'entity_id': 'light.light1',
            'url': 'https://homeassistant:8123'
        }
        control = LightToggleControl(0, **settings)
        with mock_context(control) as ctx:
            control.initialize()
            assert_rendered(ctx, TestingUtils.get_filename('../devdeck_home_assistant/assets/font-awesome/lightbulb-solid.png'))

    @vcr.use_cassette('tests/fixtures/test_light_toggle/test_initialize_sets_icon_off.yaml')
    def test_initialize_sets_icon_off(self):
        settings = {
            'api_key': 'my_secret_api_key',
            'entity_id': 'light.light1',
            'url': 'https://homeassistant:8123'
        }
        control = LightToggleControl(0, **settings)
        with mock_context(control) as ctx:
            control.initialize()
            assert_rendered(ctx, TestingUtils.get_filename('../devdeck_home_assistant/assets/font-awesome/lightbulb-regular.png'))
