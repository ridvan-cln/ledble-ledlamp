from enum import Enum

DOMAIN = "ledble_ledlamp"
CONF_RESET = "reset"
CONF_DELAY = "delay"

SUPPORTED_DEVICE_NAMES = ("LEDBLE-01", "LEDDMX-00")


def get_device_model(name: str) -> str | None:
	"""Return the supported model prefix for a Bluetooth local name."""
	normalized_name = name.lower()
	return next(
		(
			model
			for model in SUPPORTED_DEVICE_NAMES
			if normalized_name.startswith(model.lower())
		),
		None,
	)
