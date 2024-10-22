import base64
import binascii

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from drf_base64_binaryfield.validators import MaxSizeValidator
from drf_base64_binaryfield.validators import MinSizeValidator


class Base64BinaryField(serializers.Field):
    """A field that converts base64 encoded data to binary and vice versa.

    This field is intended to be used with used with raw binary data.
    It only cares about converting base64 to binary and is oblivious as to the meaning of the binary data.
    You can pass additional validators if you want to validate the binary data.

    The field will output base64 encoded data when serialized. You can control whether the output is web-safe
    by setting the `url_safe` argument to True or False. The default is False.
    """

    default_error_messages = {
        "invalid_type": _("Incorrect type. Expected a string, but got {input_type}"),
        "invalid_format": _("Base64 is incorrectly formatted. Please check that the input is valid base64."),
        "invalid_characters": _("Base64 contains invalid character(s). It must contain ASCII characters only."),
        "max_size": _(
            "Ensure the binary encoded in this field is no larger than {max_size} bytes. It is {length} bytes."
        ),
        "min_size": _("Ensure the binary encoded in this field is at least {min_size} bytes. It is {length} bytes."),
    }

    def __init__(
        self,
        *,
        # Base arguments, passed to super()
        # We don't use kwargs because we want to be explicit about the arguments
        # and not obscure them with **kwargs.
        read_only=False,
        write_only=False,
        required=None,
        default=serializers.empty,
        initial=serializers.empty,
        source=None,
        label=None,
        help_text=None,
        style=None,
        error_messages=None,
        validators=None,
        allow_null=False,
        # Custom arguments
        max_size=None,
        min_size=None,
        url_safe=False,
    ):
        """Initializes the field.

        :param max_size: The maximum byte size of the binary data.
        :param min_size: The minimum byte size of the binary data.
        :param url_safe: Whether to use web-safe encoding. Defaults to False.
        """
        super().__init__(
            read_only=read_only,
            write_only=write_only,
            required=required,
            default=default,
            initial=initial,
            source=source,
            label=label,
            help_text=help_text,
            style=style,
            error_messages=error_messages,
            validators=validators,
            allow_null=allow_null,
        )

        self.max_size = max_size
        self.min_size = min_size
        self.url_safe = url_safe

        if self.max_size is not None:
            self.validators.append(MaxSizeValidator(self.max_size, message=self.error_messages["max_size"]))
        if self.min_size is not None:
            self.validators.append(MinSizeValidator(self.min_size, message=self.error_messages["min_size"]))

    def from_base64(self, data: str) -> bytes:
        """Convert base64 encoded data to binary.

        Override this method if you want to control how base64 is decoded.
        """
        data = self._correct_padding(data)
        if self.url_safe:
            # Base64 uses + and /, but these characters are not safe to use in URLs.
            # We allow these characters to be replaced with - and _.
            websafe_substitution_chars = "-_"

            # Call b64decode instead of urlsafe_b64decode because we want to pass validate=True
            return base64.b64decode(data, altchars=websafe_substitution_chars, validate=True)
        return base64.b64decode(data, validate=True)

    def _correct_padding(self, data: str) -> str:
        """Correct base64 padding, if necessary.

        Padding could have been truncated, so we add it back to make sure the data is valid base64.
        """
        padding = len(data) % 4
        if padding:
            data += "=" * (4 - padding)
        return data

    def to_base64(self, data: bytes) -> bytes:
        """Convert binary data to base64.

        Override this method if you want to control how base64 is encoded.
        """
        if self.url_safe:
            return base64.urlsafe_b64encode(data)
        return base64.b64encode(data)

    def to_internal_value(self, data):
        """Deserialize base64 encoded data to binary.

        Override this method if you want to control how the binary data is deserialized.
        For example, if your binary data is in a custom format, you could deserialize it to a Python object in this method.
        """
        if not isinstance(data, str):
            self.fail("invalid_type", input_type=type(data).__name__)
        try:
            return self.from_base64(data)
        except binascii.Error:
            self.fail("invalid_format")
        except ValueError:
            self.fail("invalid_characters")

    def to_representation(self, value):
        """Serialize binary data to base64."""
        if not isinstance(value, bytes):
            self.fail("invalid_type", input_type=type(value).__name__)
        return self.to_base64(value).decode("utf-8")
