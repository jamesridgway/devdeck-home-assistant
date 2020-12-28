# DevDeck - Home Assistant
![CI](https://github.com/jamesridgway/devdeck-home-assistant/workflows/CI/badge.svg?branch=main)

Home Assistant controls for [DevDeck](https://github.com/jamesridgway/devdeck).

## Installing
Simplify install *DevDeck - Home Assistant* into the same python environment that you have installed DevDeck.

    pip install devdeck-home-assistant

You can then update your DevDeck configuration to use decks and controls from this package.

## Controls

* `SwitchToggleControl`

   Can be used to toggle the state of a switch entity

* `LightToggleControl`

   Can be used to toggle the state of a light entity

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
                url: 'htts://homeassistant:8123'
            - name: 'devdeck_home_assistant.switch_toggle_control.SwitchToggleControl'
              key: 1
              settings:
                api_key: 'YOUR_API_KEY_GOES_HERE'
                entity_id: 'switch.your_switch_entity_id'
                url: 'htts://homeassistant:8123'

## Prerequisites

You must have the API enabled by having an `api` entry in your home assistant configuration:

```
api:

```

See the [Home Assistant API docs](https://www.home-assistant.io/integrations/api/) for more details.

You will also need a **Long-Lived Access Token** which can be generated from the profile page (`/profile`).
