"""Reusable validators."""
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


# Inspired by rest_framework/validators.py


class MaxSizeValidator:
    """Validates that the data is no larger than a given size."""

    message = _("Ensure the binary encoded in this field is no larger than {max_size} bytes. It is {length} bytes.")
    code = "max_size"

    def __init__(self, max_size: int, message: str = None):
        """Initializes the validator.

        :param max_size: The maximum byte size of the binary data.
        :param message: The error message to use when validation fails. Defaults to a generic message.
        """
        self.max_size = max_size
        self.message = message or self.message

    def __call__(self, value):
        """Validates that the data is no larger than a given size."""
        if len(value) > self.max_size:
            raise ValidationError(
                self.message.format(max_size=self.max_size, length=len(value)),
                code=self.code,
            )


class MinSizeValidator:
    """Validates that the data is at least a given size."""

    message = _("Ensure the binary encoded in this field is at least {min_size} bytes. It is {length} bytes.")
    code = "min_size"

    def __init__(self, min_size: int, message: str = None):
        """Initializes the validator.

        :param min_size: The minimum byte size of the binary data.
        :param message: The error message to use when validation fails. Defaults to a generic message.
        """
        self.min_size = min_size
        self.message = message or self.message

    def __call__(self, value):
        """Validates that the data is at least a given size."""
        if len(value) < self.min_size:
            raise ValidationError(
                self.message.format(min_size=self.min_size, length=len(value)),
                code=self.code,
            )
