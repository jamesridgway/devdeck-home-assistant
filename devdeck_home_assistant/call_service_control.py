from io import BytesIO
import logging
import threading
import time

from devdeck_core.controls.deck_control import DeckControl
import requests

logger = logging.getLogger('devdeck')

# Temporary workaround. Needs a more generalized solution to avoid draw issues.
draw_lock = threading.Lock()


class CallServiceControl(DeckControl):
    def __init__(self, key_no, **kwargs):
        self.key_no = key_no
        self.headers = {}
        self.ha_url = kwargs['url']
        if 'service' in kwargs:
            self.domain, self.service = kwargs['service'].split('.', maxsplit=1)
        self.service_data = kwargs.get('data', {})
        self.state_entity = kwargs.get('state_entity')
        self.state_map = kwargs.get('state_map', {})
        self.redraw_interval = kwargs.get('redraw_interval', 3)
        self.dynamic_icon = 'state_entity' in kwargs
        self.running = False
        self.thread = None
        super().__init__(key_no, **kwargs)

    def initialize(self):
        if 'Authorization' not in self.headers:
            self.headers['Authorization'] = 'Bearer {}'.format(
                self.settings['api_key'])
        self.render_icon()
        if self.dynamic_icon:
            self.thread = threading.Thread(target=self._render_thread)
            self.running = True
            self.thread.start()

    def _render_thread(self):
        while self.running:
            time.sleep(self.redraw_interval)
            with draw_lock:
                try:
                    self.render_icon()
                except Exception as e:
                    logger.error('Cannot redraw key %s: %s', self.key_no, e)

    def dispose(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def render_icon(self):
        if self.state_entity is not None:
            entity_state = self.get_state(self.state_entity)
            default = self.state_map.get('_default',
                                         {'text': entity_state['state']})
            to_render = self.state_map.get(entity_state['state'], default)
            self._render_icon_spec(to_render, entity_state=entity_state)
        else:
            self._render_icon_spec(self.settings)

    def _render_icon_spec(self, spec, entity_state=None):
        with self.deck_context() as context:
            with context.renderer() as r:
                if 'emoji' in spec:
                    r.emoji(spec['emoji']).end()
                elif 'text' in spec:
                    r.text(spec['text'])
                elif 'image' in spec:
                    r.image(spec['image']).end()
                elif 'entity_image' in spec:
                    if spec['entity_image'] == self.state_entity:
                        state = entity_state
                    else:
                        state = self.get_state(spec['entity_image'])
                    self._render_state_image(state, r)

    def _render_state_image(self, state, renderer):
        path = state['attributes'].get('entity_picture', None)
        if path is not None:
            url = '{}/{}'.format(self.ha_url, path.lstrip('/'))
            renderer.image(requests.get(url, stream=True).raw).end()

    def call_service(self, domain, service, data=None):
        url = '{}/api/services/{}/{}'.format(self.ha_url, domain, service)
        requests.post(url, json=data or {}, headers=self.headers)

    def get_state(self, entity_id) -> dict:
        url = '{}/api/states/{}'.format(self.ha_url, entity_id)
        r = requests.get(url, headers=self.headers)
        return r.json()

    def pressed(self):
        self.call_service(self.domain, self.service, self.service_data)
        self.render_icon()

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
            'service': {
                'type': 'string',
                'required': True
            },
            'data': {
                'type': 'dict',
                'required': False,
                'allow_unknown': True
            },
            'emoji': {
                'type': 'string',
                'required': False
            },
            'text': {
                'type': 'string',
                'required': False
            },
            'image': {
                'type': 'string',
                'required': False
            },
            'entity_image': {
                'type': 'string',
                'required': False
            },
            'state_entity': {
                'type': 'string',
                'required': False
            },
            'state_map': {
                'type': 'dict',
                'required': False,
                'keysrules': {
                    'type': 'string'
                },
                'valuesrules': {
                    'type': 'dict',
                    'maxlength': 1,
                    'minlength': 1,
                    'keysrules': {
                        'allowed': ['emoji', 'text', 'image', 'entity_image']
                    },
                    'valuesrules': {
                        'type': 'string'
                    }
                }
            },
            'redraw_interval': {
                'type': 'number',
                'min': 0.1,
                'required': False
            }
        }
