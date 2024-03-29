# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from ynab_python_sdk.pydantic.save_transactions_response_data_duplicate_import_ids import SaveTransactionsResponseDataDuplicateImportIds
from ynab_python_sdk.pydantic.save_transactions_response_data_transaction_ids import SaveTransactionsResponseDataTransactionIds
from ynab_python_sdk.pydantic.transaction_detail import TransactionDetail

class SaveTransactionsResponseData(BaseModel):
    transaction_ids: SaveTransactionsResponseDataTransactionIds = Field(alias='transaction_ids')

    # The knowledge of the server
    server_knowledge: int = Field(alias='server_knowledge')

    transaction: typing.Optional[TransactionDetail] = Field(None, alias='transaction')

    # If multiple transactions were specified, the transactions that were saved
    transactions: typing.Optional[typing.List[TransactionDetail]] = Field(None, alias='transactions')

    duplicate_import_ids: typing.Optional[SaveTransactionsResponseDataDuplicateImportIds] = Field(None, alias='duplicate_import_ids')
    class Config:
        arbitrary_types_allowed = True
