class LutronSwitch:
    """Representation of a Lutron switch."""

    def __init__(self, device_id, name, api):
        self._device_id = device_id
        self._name = name
        self._api = api
        self._state = False

    @property
    def name(self):
        """Return the name of the switch."""
        return self._name

    @property
    def is_on(self):
        """Return true if the switch is on."""
        return self._state

    def turn_on(self):
        """Turn the switch on."""
        self._api.set_switch_state(self._device_id, True)
        self._state = True

    def turn_off(self):
        """Turn the switch off."""
        self._api.set_switch_state(self._device_id, False)
        self._state = False

    def update(self):
        """Fetch new state data for the switch."""
        self._state = self._api.get_switch_state(self._device_id)