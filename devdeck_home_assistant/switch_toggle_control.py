import os
import requests
import tempfile

from .call_service_control import CallServiceControl
from PIL import Image, ImageDraw, ImageFont


class SwitchToggleControl(CallServiceControl):
    def __init__(self, key_no, **kwargs):
        super().__init__(key_no, **kwargs)
        self.domain = 'switch'
        self.service = 'toggle'
        self.service_data = {'entity_id': kwargs['entity_id']}
        self.state_entity = kwargs['entity_id']

        on = self.make_image(
            kwargs.get('icon', 'toggle-switch-outline'),
            'on',
            kwargs.get('text', ''),
            kwargs.get('bg_color', 'black')
        )

        off = self.make_image(
            kwargs.get('icon', 'toggle-switch-outline'),
            'off',
            kwargs.get('text', ''),
            kwargs.get('bg_color', 'black')
        )

        self.state_map = {
            'on': {'image': on},
            'off': {'image': off},
        }
        self.dynamic_icon = True

    def make_image(self, icon, state, text, bg_color):
        bg = Image.new('RGBA', (512, 512), bg_color)
        font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), "assets/roboto", 'Roboto-Regular.ttf'), 80)
        mdi_dir = os.path.join(os.path.dirname(__file__), "assets/mdi")
        img = Image.open(os.path.join(mdi_dir, icon + '-' + state + '.png'))

        if len(text) > 0:
            draw = ImageDraw.Draw(img)
            draw.text((256, 500), text, fill=(255,255,255,255), anchor='mb', font=font)

        out = Image.composite(img, bg, img)
        filename = tempfile.NamedTemporaryFile()
        out.save(filename, format="PNG")
        return filename

    def settings_schema(self):
        return {
            'api_key': {
                'type': 'string',
                'required': True
            },
            'bg_color': {
                'type': 'string',
                'required': False
            },
            'entity_id': {
                'type': 'string',
                'required': True
            },
            'icon': {
                'type': 'string',
                'required': False
            },
            'redraw_interval': {
                'type': 'number',
                'min': 0.1,
                'required': False
            },
            'text': {
                'type': 'string',
                'required': False
            },
            'url': {
                'type': 'string',
                'required': True
            }
        }
