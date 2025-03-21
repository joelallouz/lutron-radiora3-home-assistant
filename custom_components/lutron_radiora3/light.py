class LutronLight:
    """Representation of a Lutron light entity."""

    def __init__(self, device_id, name, api):
        self._device_id = device_id
        self._name = name
        self._api = api
        self._is_on = False
        self._brightness = 0

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._is_on

    @property
    def brightness(self):
        return self._brightness

    def turn_on(self, brightness=None):
        """Turn the light on."""
        self._is_on = True
        if brightness is not None:
            self._brightness = brightness
        self._api.set_light_state(self._device_id, True, self._brightness)

    def turn_off(self):
        """Turn the light off."""
        self._is_on = False
        self._api.set_light_state(self._device_id, False)

    def update(self):
        """Fetch the latest state from the Lutron API."""
        state = self._api.get_light_state(self._device_id)
        self._is_on = state['is_on']
        self._brightness = state['brightness'] if 'brightness' in state else 0