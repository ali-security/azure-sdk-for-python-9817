# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import base64
from json import JSONEncoder
from typing import TYPE_CHECKING

from .utils._utils import _FixedOffset

if TYPE_CHECKING:
    from typing import Optional
    from datetime import timedelta


__all__ = ["NULL", "AzureJSONEncoder"]



class _Null(object):
    """To create a Falsy object"""

    def __bool__(self):
        return False

    __nonzero__ = __bool__  # Python2 compatibility


NULL = _Null()
"""
A falsy sentinel object which is supposed to be used to specify attributes
with no data. This gets serialized to `null` on the wire.
"""


def _timedelta_as_isostr(value):
    # type: (timedelta) -> str
    """Converts a datetime.timedelta object into an ISO 8601 formatted string, e.g. 'P4DT12H30M05S'

    Function adapted from the Tin Can Python project: https://github.com/RusticiSoftware/TinCanPython
    """

    # Split seconds to larger units
    seconds = value.total_seconds()
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    days, hours, minutes = list(map(int, (days, hours, minutes)))
    seconds = round(seconds, 6)

    # Build date
    date = ""
    if days:
        date = "%sD" % days

    # Build time
    time = "T"

    # Hours
    bigger_exists = date or hours
    if bigger_exists:
        time += "{:02}H".format(hours)

    # Minutes
    bigger_exists = bigger_exists or minutes
    if bigger_exists:
        time += "{:02}M".format(minutes)

    # Seconds
    try:
        if seconds.is_integer():
            seconds_string = "{:02}".format(int(seconds))
        else:
            # 9 chars long w/ leading 0, 6 digits after decimal
            seconds_string = "%09.6f" % seconds
            # Remove trailing zeros
            seconds_string = seconds_string.rstrip("0")
    except AttributeError:  # int.is_integer() raises
        seconds_string = "{:02}".format(seconds)

    time += "{}S".format(seconds_string)

    return "P" + date + time


try:
    from datetime import timezone

    TZ_UTC = timezone.utc  # type: ignore
except ImportError:
    TZ_UTC = _FixedOffset(0)  # type: ignore


class AzureJSONEncoder(JSONEncoder):
    """A JSON encoder that's capable of serializing datetime objects and bytes."""

    def default(self, o):  # pylint: disable=too-many-return-statements
        try:
            return super(AzureJSONEncoder, self).default(o)
        except TypeError:
            if isinstance(o, (bytes, bytearray)):
                return base64.b64encode(o).decode()
            try:
                # First try datetime.datetime
                if hasattr(o, "year") and hasattr(o, "hour"):
                    # astimezone() fails for naive times in Python 2.7, so make make sure o is aware (tzinfo is set)
                    if not o.tzinfo:
                        iso_formatted = o.replace(tzinfo=TZ_UTC).isoformat()
                    else:
                        iso_formatted = o.astimezone(TZ_UTC).isoformat()
                    # Replace the trailing "+00:00" UTC offset with "Z" (RFC 3339: https://www.ietf.org/rfc/rfc3339.txt)
                    return iso_formatted.replace("+00:00", "Z")
                # Next try datetime.date or datetime.time
                return o.isoformat()
            except AttributeError:
                pass
            # Last, try datetime.timedelta
            try:
                return _timedelta_as_isostr(o)
            except AttributeError:
                # This will be raised when it hits value.total_seconds in the method above
                pass
            return super(AzureJSONEncoder, self).default(o)

def _deserialize(item):
    return item

class mark:
    def __init__(self, original_name):
        self._original_name = original_name

    def __call__(self, func):
        original_name = self._original_name
        def wrapper(self, *args, **kwargs):
            self._attr_name_to_original_name[func.__name__] = original_name
            return func(self, *args, **kwargs)
        return wrapper

_MY_MODEL_PROPERTIES = [
    "_attr_name_to_original_name",
    "_attr_name_to_original_name_var",
]

class Model(dict):

    def __eq__(self, other):
        """Compare objects by comparing all attributes."""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    @property
    def _attr_name_to_original_name(self):
        if not hasattr(self, "_attr_name_to_original_name_var"):
            self._attr_name_to_original_name_var = {}
        return self._attr_name_to_original_name_var

    @_attr_name_to_original_name.setter
    def _attr_name_to_original_name(self, value):
        self._attr_name_to_original_name_var = value

    def __getattr__(self, attr):
        if attr in _MY_MODEL_PROPERTIES:
            return super().__getattribute__(attr)
        if not self.__hasattr__(attr):
            raise AttributeError(
                "{} instance has no attribute '{}'".format(
                    type(self).__name__,
                    attr
                )
            )

        return self.__getitem__[self._attr_name_to_original_name[attr]]

    def __setattr__(self, name, value):
        # the properties on the base class
        if name in _MY_MODEL_PROPERTIES:
            super().__setattr__(name, value)
        else:
            self.__setitem__(self._attr_name_to_original_name[name], value)

    def __delattr__(self, attr):
        if attr in _MY_MODEL_PROPERTIES:
            return super().__delattr__(attr)
        return self.__delitem__(self._attr_name_to_original_name[attr])

    def __hasattr__(self, attr):
        if attr in _MY_MODEL_PROPERTIES:
            return True
        try:
            return bool(self.__getitem__(self._attr_name_to_original_name[attr]))
        except KeyError:
            return False

    def copy(self):
        return Model(self.__dict__)
