# DevDeck - Home Assistant
![CI](https://github.com/jamesridgway/devdeck-home-assistant/workflows/CI/badge.svg?branch=main)

Home Assistant controls for [DevDeck](https://github.com/jamesridgway/devdeck).

## Installing
Simply install *DevDeck - Home Assistant* into the same python environment that you have installed DevDeck.

    pip install devdeck-home-assistant

You can then update your DevDeck configuration to use decks and controls from this package.

## Controls
All Controls share the following required settings:
|  Option Name| Description
|--|--|
| api_key | Your long lived access token
| entity_id | The entity ID from Home Assistant
| url | The URL to your home assistant installation

* `CallServiceControl`

   Can be used to call any Home Assistant service

* `SwitchToggleControl`

   Can be used to toggle the state of a switch entity. This control has the following optional configurable settings:

	|  Option Name| Description  |Default Value
	|--|--|--|
	| icon | The icon to be displayed | toggle-switch-outline
	| bg_color | Background color | black
	| text | Short text label

  The following icons are available, please use the name value from the following table as the icon value in the configuration file:

    | Name | Icon Off | Icon On
    |--|--|--
    | toggle-switch | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/toggle-switch-off.png" width="100" height="100" /> | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/toggle-switch-on.png" width="100" height="100" />
    | toggle-switch-outline | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/toggle-switch-outline-off.png" width="100" height="100" /> | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/toggle-switch-outline-on.png" width="100" height="100" />

* `LightToggleControl`

   Can be used to toggle the state of a light entity. This control has the following optional configurable settings:

	|  Option Name| Description  |Default Value
	|--|--|--|
	| icon | The icon to be displayed | lightbulb
	| bg_color | Background color | black
	| text | Short text label
	
    The following icons are available, please use the name value from the following table as the icon value in the configuration file:

    | Name | Icon Off | Icon On
    |--|--|--
    | ceiling-light | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/ceiling-light-full-off.png" width="100" height="100" /> | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/ceiling-light-full-on.png" width="100" height="100" /> 
    | desk-lamp | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/desk-lamp-full-off.png" width="100" height="100" /> | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/desk-lamp-full-on.png" width="100" height="100" /> 
    | floor-lamp | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/floor-lamp-full-off.png" width="100" height="100" /> | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/floor-lamp-full-on.png" width="100" height="100" /> 
    | globe-light | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/globe-light-full-off.png" width="100" height="100" /> | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/globe-light-full-on.png" width="100" height="100" /> 
    | lamp | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/lamp-full-off.png" width="100" height="100" /> | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/lamp-full-on.png" width="100" height="100" /> 
    | led-strip | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/led-strip-full-off.png" width="100" height="100" /> | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/led-strip-full-on.png" width="100" height="100" /> 
    | led-strip-variant | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/led-strip-variant-full-off.png" width="100" height="100" /> | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/led-strip-variant-full-on.png" width="100" height="100" /> 
    | lightbulb | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/lightbulb-full-off.png" width="100" height="100" /> | <img src="https://github.com/timtimellis/devdeck-home-assistant/raw/fiddle/devdeck_home_assistant/assets/mdi/lightbulb-full-on.png" width="100" height="100" /> 

## Configuration

Example configuration:

    decks:
      - serial_number: "ABC123"
        name: 'devdeck.decks.single_page_deck_controller.SinglePageDeckController'
        settings:
          controls:
            - name: 'devdeck_home_assistant.light_toggle_control.LightToggleControl'
              key: 0
              settings:
                api_key: 'YOUR_API_KEY_GOES_HERE'
                entity_id: 'light.your_light_entity_id'
                url: 'http://homeassistant:8123'
                icon: 'lightbulb'
                bg_color: 'black'
                text: 'Hall'
            - name: 'devdeck_home_assistant.switch_toggle_control.SwitchToggleControl'
              key: 1
              settings:
                api_key: 'YOUR_API_KEY_GOES_HERE'
                entity_id: 'switch.your_switch_entity_id'
                url: 'http://homeassistant:8123'
            - name: 'devdeck_home_assistant.call_service_control.CallServiceControl'
              key: 2
              settings:
                api_key: 'YOUR_API_KEY_GOES_HERE'
                url: 'http://homeassistant:8123'
                service: scene.turn_on
                data:
                  entity_id: scene.work_mode
                emoji: ':laptop:'
            - name: 'devdeck_home_assistant.call_service_control.CallServiceControl'
              key: 3
              settings:
                api_key: 'YOUR_API_KEY_GOES_HERE'
                url: 'http://homeassistant:8123'
                service: media_player.media_play_pause
                data:
                  entity_id: media_player.office_sonos
                state_entity: media_player.office_sonos
                state_map:
                  playing:
                    emoji: ':pause_button:'
                  paused:
                    emoji: ':play_button:'
                  idle:
                    emoji: ':watch:'
            - name: 'devdeck_home_assistant.call_service_control.CallServiceControl'
              key: 4
              settings:
                api_key: 'YOUR_API_KEY_GOES_HERE'
                url: 'http://homeassistant:8123'
                service: script.noop
                state_entity: media_player.office_sonos
                state_map:
                  _default:
                    entity_image: media_player.office_sonos


## Prerequisites

You must have the API enabled by having an `api` entry in your home assistant configuration:

```
api:

```

See the [Home Assistant API docs](https://www.home-assistant.io/integrations/api/) for more details.

You will also need a **Long-Lived Access Token** which can be generated from the profile page (`/profile`).
