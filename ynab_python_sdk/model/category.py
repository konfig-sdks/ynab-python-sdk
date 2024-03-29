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


class Category(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "deleted",
            "activity",
            "balance",
            "hidden",
            "name",
            "id",
            "category_group_id",
            "budgeted",
        }
        
        class properties:
            id = schemas.UUIDSchema
            category_group_id = schemas.UUIDSchema
            name = schemas.StrSchema
            hidden = schemas.BoolSchema
            budgeted = schemas.Int64Schema
            activity = schemas.Int64Schema
            balance = schemas.Int64Schema
            deleted = schemas.BoolSchema
            category_group_name = schemas.StrSchema
            
            
            class original_category_group_id(
                schemas.UUIDBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uuid'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, uuid.UUID, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'original_category_group_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class note(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'note':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class goal_type(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "TB": "TB",
                        "TBD": "TBD",
                        "MF": "MF",
                        "NEED": "NEED",
                        "DEBT": "DEBT",
                        None: "NONE",
                    }
                
                @schemas.classproperty
                def TB(cls):
                    return cls("TB")
                
                @schemas.classproperty
                def TBD(cls):
                    return cls("TBD")
                
                @schemas.classproperty
                def MF(cls):
                    return cls("MF")
                
                @schemas.classproperty
                def NEED(cls):
                    return cls("NEED")
                
                @schemas.classproperty
                def DEBT(cls):
                    return cls("DEBT")
                
                @schemas.classproperty
                def NONE(cls):
                    return cls(None)
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'goal_type':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class goal_day(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'goal_day':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class goal_cadence(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'goal_cadence':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class goal_cadence_frequency(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'goal_cadence_frequency':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class goal_creation_month(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'goal_creation_month':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class goal_target(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'goal_target':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class goal_target_month(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'goal_target_month':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class goal_percentage_complete(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'goal_percentage_complete':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class goal_months_to_budget(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'goal_months_to_budget':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class goal_under_funded(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'goal_under_funded':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class goal_overall_funded(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'goal_overall_funded':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class goal_overall_left(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'goal_overall_left':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "category_group_id": category_group_id,
                "name": name,
                "hidden": hidden,
                "budgeted": budgeted,
                "activity": activity,
                "balance": balance,
                "deleted": deleted,
                "category_group_name": category_group_name,
                "original_category_group_id": original_category_group_id,
                "note": note,
                "goal_type": goal_type,
                "goal_day": goal_day,
                "goal_cadence": goal_cadence,
                "goal_cadence_frequency": goal_cadence_frequency,
                "goal_creation_month": goal_creation_month,
                "goal_target": goal_target,
                "goal_target_month": goal_target_month,
                "goal_percentage_complete": goal_percentage_complete,
                "goal_months_to_budget": goal_months_to_budget,
                "goal_under_funded": goal_under_funded,
                "goal_overall_funded": goal_overall_funded,
                "goal_overall_left": goal_overall_left,
            }
    
    deleted: MetaOapg.properties.deleted
    activity: MetaOapg.properties.activity
    balance: MetaOapg.properties.balance
    hidden: MetaOapg.properties.hidden
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    category_group_id: MetaOapg.properties.category_group_id
    budgeted: MetaOapg.properties.budgeted
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category_group_id"]) -> MetaOapg.properties.category_group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hidden"]) -> MetaOapg.properties.hidden: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["budgeted"]) -> MetaOapg.properties.budgeted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activity"]) -> MetaOapg.properties.activity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balance"]) -> MetaOapg.properties.balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category_group_name"]) -> MetaOapg.properties.category_group_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["original_category_group_id"]) -> MetaOapg.properties.original_category_group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal_type"]) -> MetaOapg.properties.goal_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal_day"]) -> MetaOapg.properties.goal_day: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal_cadence"]) -> MetaOapg.properties.goal_cadence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal_cadence_frequency"]) -> MetaOapg.properties.goal_cadence_frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal_creation_month"]) -> MetaOapg.properties.goal_creation_month: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal_target"]) -> MetaOapg.properties.goal_target: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal_target_month"]) -> MetaOapg.properties.goal_target_month: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal_percentage_complete"]) -> MetaOapg.properties.goal_percentage_complete: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal_months_to_budget"]) -> MetaOapg.properties.goal_months_to_budget: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal_under_funded"]) -> MetaOapg.properties.goal_under_funded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal_overall_funded"]) -> MetaOapg.properties.goal_overall_funded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["goal_overall_left"]) -> MetaOapg.properties.goal_overall_left: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "category_group_id", "name", "hidden", "budgeted", "activity", "balance", "deleted", "category_group_name", "original_category_group_id", "note", "goal_type", "goal_day", "goal_cadence", "goal_cadence_frequency", "goal_creation_month", "goal_target", "goal_target_month", "goal_percentage_complete", "goal_months_to_budget", "goal_under_funded", "goal_overall_funded", "goal_overall_left", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category_group_id"]) -> MetaOapg.properties.category_group_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hidden"]) -> MetaOapg.properties.hidden: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["budgeted"]) -> MetaOapg.properties.budgeted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activity"]) -> MetaOapg.properties.activity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balance"]) -> MetaOapg.properties.balance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category_group_name"]) -> typing.Union[MetaOapg.properties.category_group_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["original_category_group_id"]) -> typing.Union[MetaOapg.properties.original_category_group_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> typing.Union[MetaOapg.properties.note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal_type"]) -> typing.Union[MetaOapg.properties.goal_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal_day"]) -> typing.Union[MetaOapg.properties.goal_day, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal_cadence"]) -> typing.Union[MetaOapg.properties.goal_cadence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal_cadence_frequency"]) -> typing.Union[MetaOapg.properties.goal_cadence_frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal_creation_month"]) -> typing.Union[MetaOapg.properties.goal_creation_month, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal_target"]) -> typing.Union[MetaOapg.properties.goal_target, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal_target_month"]) -> typing.Union[MetaOapg.properties.goal_target_month, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal_percentage_complete"]) -> typing.Union[MetaOapg.properties.goal_percentage_complete, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal_months_to_budget"]) -> typing.Union[MetaOapg.properties.goal_months_to_budget, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal_under_funded"]) -> typing.Union[MetaOapg.properties.goal_under_funded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal_overall_funded"]) -> typing.Union[MetaOapg.properties.goal_overall_funded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["goal_overall_left"]) -> typing.Union[MetaOapg.properties.goal_overall_left, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "category_group_id", "name", "hidden", "budgeted", "activity", "balance", "deleted", "category_group_name", "original_category_group_id", "note", "goal_type", "goal_day", "goal_cadence", "goal_cadence_frequency", "goal_creation_month", "goal_target", "goal_target_month", "goal_percentage_complete", "goal_months_to_budget", "goal_under_funded", "goal_overall_funded", "goal_overall_left", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        deleted: typing.Union[MetaOapg.properties.deleted, bool, ],
        activity: typing.Union[MetaOapg.properties.activity, decimal.Decimal, int, ],
        balance: typing.Union[MetaOapg.properties.balance, decimal.Decimal, int, ],
        hidden: typing.Union[MetaOapg.properties.hidden, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        category_group_id: typing.Union[MetaOapg.properties.category_group_id, str, uuid.UUID, ],
        budgeted: typing.Union[MetaOapg.properties.budgeted, decimal.Decimal, int, ],
        category_group_name: typing.Union[MetaOapg.properties.category_group_name, str, schemas.Unset] = schemas.unset,
        original_category_group_id: typing.Union[MetaOapg.properties.original_category_group_id, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        note: typing.Union[MetaOapg.properties.note, None, str, schemas.Unset] = schemas.unset,
        goal_type: typing.Union[MetaOapg.properties.goal_type, None, str, schemas.Unset] = schemas.unset,
        goal_day: typing.Union[MetaOapg.properties.goal_day, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        goal_cadence: typing.Union[MetaOapg.properties.goal_cadence, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        goal_cadence_frequency: typing.Union[MetaOapg.properties.goal_cadence_frequency, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        goal_creation_month: typing.Union[MetaOapg.properties.goal_creation_month, None, str, date, schemas.Unset] = schemas.unset,
        goal_target: typing.Union[MetaOapg.properties.goal_target, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        goal_target_month: typing.Union[MetaOapg.properties.goal_target_month, None, str, date, schemas.Unset] = schemas.unset,
        goal_percentage_complete: typing.Union[MetaOapg.properties.goal_percentage_complete, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        goal_months_to_budget: typing.Union[MetaOapg.properties.goal_months_to_budget, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        goal_under_funded: typing.Union[MetaOapg.properties.goal_under_funded, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        goal_overall_funded: typing.Union[MetaOapg.properties.goal_overall_funded, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        goal_overall_left: typing.Union[MetaOapg.properties.goal_overall_left, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Category':
        return super().__new__(
            cls,
            *args,
            deleted=deleted,
            activity=activity,
            balance=balance,
            hidden=hidden,
            name=name,
            id=id,
            category_group_id=category_group_id,
            budgeted=budgeted,
            category_group_name=category_group_name,
            original_category_group_id=original_category_group_id,
            note=note,
            goal_type=goal_type,
            goal_day=goal_day,
            goal_cadence=goal_cadence,
            goal_cadence_frequency=goal_cadence_frequency,
            goal_creation_month=goal_creation_month,
            goal_target=goal_target,
            goal_target_month=goal_target_month,
            goal_percentage_complete=goal_percentage_complete,
            goal_months_to_budget=goal_months_to_budget,
            goal_under_funded=goal_under_funded,
            goal_overall_funded=goal_overall_funded,
            goal_overall_left=goal_overall_left,
            _configuration=_configuration,
            **kwargs,
        )
