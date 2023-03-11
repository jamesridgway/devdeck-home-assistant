import os

import requests

from .call_service_control import CallServiceControl


class LightToggleControl(CallServiceControl):
    def __init__(self, key_no, **kwargs):
        super().__init__(key_no, **kwargs)
        self.domain = 'light'
        self.service = 'toggle'
        self.service_data = {'entity_id': kwargs['entity_id']}
        self.state_entity = kwargs['entity_id']
        mdi_dir = os.path.join(os.path.dirname(__file__), "assets/mdi")
        self.state_map = {
            'on': {'image': os.path.join(mdi_dir, kwargs['icon'] + '-solid.png')},
            'off': {'image': os.path.join(mdi_dir, kwargs['icon'] + '-regular.png')},
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
            },
            'icon': {
                'type': 'string',
                'required': True
            }
        }
