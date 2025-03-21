# Lutron RadioRA3 Home Assistant Integration

This custom component allows you to integrate the Lutron RadioRA3 system with Home Assistant, enabling you to monitor and control components, zones, scenes, devices, and more directly from your Home Assistant interface.

## Features

- Control lights, switches, and scenes in your Lutron RadioRA3 system.
- Monitor the status of various devices and sensors.
- Seamless integration with Home Assistant's automation and scripting capabilities.

## Prerequisites

- Home Assistant instance running.
- HACS (Home Assistant Community Store) installed.
- Lutron RadioRA3 system set up and configured.

## Installation

1. **Install HACS**: If you haven't already, install HACS (Home Assistant Community Store) in your Home Assistant instance.

2. **Add the Repository**: Go to HACS > Integrations > Explore & Add Repositories, and add the repository URL for this custom component. The repository URL can be found on the project's GitHub page.

3. **Restart Home Assistant**: After adding the repository, restart your Home Assistant instance to load the new integration.

4. **Configure the Integration**: Add the following configuration to your `configuration.yaml` file:

```yaml
lutron_radiora3:
  host: YOUR_LUTRON_HOST
  username: YOUR_USERNAME
  password: YOUR_PASSWORD
```

Replace `YOUR_LUTRON_HOST`, `YOUR_USERNAME`, and `YOUR_PASSWORD` with your Lutron system's details.

5. **Restart Home Assistant**: Restart your Home Assistant instance to apply the new configuration.

## Usage

Once the integration is set up, you can control your Lutron devices through the Home Assistant dashboard. You can create automations and scripts to enhance your smart home experience.

### Example

To turn on a light, you can use the following service call in your automation:

```yaml
service: lutron_radiora3.turn_on
target:
  entity_id: light.living_room
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. For any issues or feature requests, please open an issue in the repository.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

Thanks to the Home Assistant community and the Lutron developer documentation for their support and resources.