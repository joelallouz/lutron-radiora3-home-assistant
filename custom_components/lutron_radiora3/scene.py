class LutronScene:
    """Representation of a Lutron scene."""

    def __init__(self, name, lutron_api):
        """Initialize the scene."""
        self._name = name
        self._lutron_api = lutron_api

    @property
    def name(self):
        """Return the name of the scene."""
        return self._name

    def activate(self):
        """Activate the scene."""
        self._lutron_api.activate_scene(self._name)

    def deactivate(self):
        """Deactivate the scene."""
        self._lutron_api.deactivate_scene(self._name)

    def is_active(self):
        """Check if the scene is currently active."""
        return self._lutron_api.is_scene_active(self._name)