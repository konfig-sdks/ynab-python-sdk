# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from ynab_python_sdk import schemas  # noqa: F401


class TransactionFlagColor(
    schemas.EnumBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The transaction flag
    """


    class MetaOapg:
        enum_value_to_name = {
            "red": "RED",
            "orange": "ORANGE",
            "yellow": "YELLOW",
            "green": "GREEN",
            "blue": "BLUE",
            "purple": "PURPLE",
            None: "NONE",
        }
    
    @schemas.classproperty
    def RED(cls):
        return cls("red")
    
    @schemas.classproperty
    def ORANGE(cls):
        return cls("orange")
    
    @schemas.classproperty
    def YELLOW(cls):
        return cls("yellow")
    
    @schemas.classproperty
    def GREEN(cls):
        return cls("green")
    
    @schemas.classproperty
    def BLUE(cls):
        return cls("blue")
    
    @schemas.classproperty
    def PURPLE(cls):
        return cls("purple")
    
    @schemas.classproperty
    def NONE(cls):
        return cls(None)


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TransactionFlagColor':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
