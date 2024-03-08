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


class AccountType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The type of account
    """
    
    @schemas.classproperty
    def CHECKING(cls):
        return cls("checking")
    
    @schemas.classproperty
    def SAVINGS(cls):
        return cls("savings")
    
    @schemas.classproperty
    def CASH(cls):
        return cls("cash")
    
    @schemas.classproperty
    def CREDIT_CARD(cls):
        return cls("creditCard")
    
    @schemas.classproperty
    def LINE_OF_CREDIT(cls):
        return cls("lineOfCredit")
    
    @schemas.classproperty
    def OTHER_ASSET(cls):
        return cls("otherAsset")
    
    @schemas.classproperty
    def OTHER_LIABILITY(cls):
        return cls("otherLiability")
    
    @schemas.classproperty
    def MORTGAGE(cls):
        return cls("mortgage")
    
    @schemas.classproperty
    def AUTO_LOAN(cls):
        return cls("autoLoan")
    
    @schemas.classproperty
    def STUDENT_LOAN(cls):
        return cls("studentLoan")
    
    @schemas.classproperty
    def PERSONAL_LOAN(cls):
        return cls("personalLoan")
    
    @schemas.classproperty
    def MEDICAL_DEBT(cls):
        return cls("medicalDebt")
    
    @schemas.classproperty
    def OTHER_DEBT(cls):
        return cls("otherDebt")
