class LutronDevice:
    """Representation of a Lutron device."""

    def __init__(self, device_id, name, device_type, api):
        self.device_id = device_id
        self.name = name
        self.device_type = device_type
        self.api = api

    def get_status(self):
        """Retrieve the current status of the device."""
        return self.api.get_device_status(self.device_id)

    def turn_on(self):
        """Turn on the device."""
        self.api.send_command(self.device_id, "on")

    def turn_off(self):
        """Turn off the device."""
        self.api.send_command(self.device_id, "off")

    def set_brightness(self, level):
        """Set the brightness of the device (if applicable)."""
        if self.device_type == "light":
            self.api.set_device_brightness(self.device_id, level)

    def __str__(self):
        return f"{self.name} (ID: {self.device_id}, Type: {self.device_type})"