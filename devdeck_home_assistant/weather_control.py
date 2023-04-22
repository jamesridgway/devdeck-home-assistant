import os
import requests

from devdeck_core.controls.deck_control import DeckControl


class WeatherControl(DeckControl):
    def __init__(self, key_no, **kwargs):
        self.headers = {}
        super().__init__(key_no, **kwargs)

    def initialize(self):
        if 'Authorization' not in self.headers:
            self.headers['Authorization'] = 'Bearer {}'.format(self.settings['api_key'])
        self.__render_icon()

    def pressed(self):
        self.__render_icon()

    def __render_icon(self):
        r = requests.get(
            '{}/api/states/{}'.format(self.settings['url'], self.settings['entity_id']),
            headers=self.headers)
        data = r.json()

        temperature = data['attributes']['temperature']
        wind_speed = data['attributes']['wind_speed']
        humidity = data['attributes']['humidity']
        state = data['state']

        emoji_map = {
            'clear-night': 'crescent_moon',
            'cloudy': 'cloud',
            'fog': 'fog',
            'hail': 'cloud_with_rain',
            'lightning': 'cloud_with_lightning',
            'lightning-rainy': 'cloud_with_lightning_and_rain',
            'partlycloudy': 'sun_behind_cloud',
            'pouring': 'cloud_with_rain',
            'rainy': 'cloud_with_rain',
            'snowy': 'cloud_with_snow',
            'snowy-rainy': 'cloud_with_snow',
            'sunny': 'sun',
            'windy': 'wind_face',
            'windy-variant': 'wind_face',
            'exceptional': 'tornado'
        }

        state_emoji = 'exclamation_question_mark'
        if state in emoji_map.keys():
            state_emoji = emoji_map[state]

        with self.deck_context() as context:
            with context.renderer() as r:
                r.emoji(state_emoji) \
                    .width(200) \
                    .height(200) \
                    .x(0) \
                    .y(0) \
                    .end()
                r.text("{}°C".format(temperature)) \
                    .x(230) \
                    .y(100 - (90 / 2)) \
                    .font_size(90) \
                    .end()

                r.emoji('dashing_away') \
                    .width(100) \
                    .height(100) \
                    .x(50) \
                    .y(250) \
                    .end()
                r.text("{}ºC".format(wind_speed)) \
                    .x(230) \
                    .y(250) \
                    .font_size(75) \
                    .end()

                r.emoji('droplet') \
                    .width(100) \
                    .height(100) \
                    .x(50) \
                    .y(380) \
                    .end()
                r.text("{}%".format(humidity)) \
                    .x(230) \
                    .y(380) \
                    .font_size(75) \
                    .end()
