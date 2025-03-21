from homeassistant.helpers.entity import Entity
from homeassistant.const import STATE_ON, STATE_OFF

class LutronSensor(Entity):
    """Representation of a Lutron Sensor."""

    def __init__(self, name, device_id, api):
        """Initialize the sensor."""
        self._name = name
        self._device_id = device_id
        self._api = api
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def unique_id(self):
        """Return a unique ID for this sensor."""
        return self._device_id

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Fetch new state data for the sensor."""
        data = await self._api.get_sensor_data(self._device_id)
        self._state = data.get("state")

    @property
    def device_state_attributes(self):
        """Return the state attributes of the sensor."""
        return {
            "device_id": self._device_id,
            "sensor_type": "Lutron",
        }