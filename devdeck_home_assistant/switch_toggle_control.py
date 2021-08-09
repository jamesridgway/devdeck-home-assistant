import os

import requests

from .call_service_control import CallServiceControl


class SwitchToggleControl(CallServiceControl):
    def __init__(self, key_no, **kwargs):
        super().__init__(key_no, **kwargs)
        self.domain = 'switch'
        self.service = 'toggle'
        self.service_data = {'entity_id': kwargs['entity_id']}
        self.state_entity = kwargs['entity_id']
        fa_dir = os.path.join(os.path.dirname(__file__), "assets/font-awesome")
        self.state_map = {
            'on': {'image': os.path.join(fa_dir, 'toggle-on-solid.png')},
            'off': {'image': os.path.join(fa_dir, 'toggle-off-solid.png')},
        }
        self.dynamic_icon = True

    def settings_schema(self):
        return {
            'url': {
                'type': 'string',
                'required': True
            },
            'api_key': {
                'type': 'string',
                'required': True
            },
            'entity_id': {
                'type': 'string',
                'required': True
            },
            'redraw_interval': {
                'type': 'number',
                'min': 0.1,
                'required': False
            }
        }
