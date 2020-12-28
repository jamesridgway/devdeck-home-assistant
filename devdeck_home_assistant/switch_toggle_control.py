import os

import requests
from devdeck_core.controls.deck_control import DeckControl


class SwitchToggleControl(DeckControl):
    def __init__(self, key_no, **kwargs):
        self.headers = {}
        super().__init__(key_no, **kwargs)

    def initialize(self):
        if 'Authorization' not in self.headers:
            self.headers['Authorization'] = 'Bearer {}'.format(self.settings['api_key'])
        self.__render_icon()

    def pressed(self):
        data = {
            'entity_id': self.settings['entity_id']
        }
        requests.post(
            '{}/api/services/switch/toggle'.format(self.settings['url']),
            json=data,
            headers=self.headers)
        self.__render_icon()

    def __render_icon(self):
        r = requests.get(
            '{}/api/states/{}'.format(self.settings['url'], self.settings['entity_id']),
            headers=self.headers)
        data = r.json()
        with self.deck_context() as context:
            if data['state'] == 'on':
                with context.renderer() as r:
                    r.image(os.path.join(os.path.dirname(__file__), "assets/font-awesome", 'toggle-on-solid.png')).end()
            else:
                with context.renderer() as r:
                    r.image(os.path.join(os.path.dirname(__file__), "assets/font-awesome", 'toggle-off-solid.png')).end()
