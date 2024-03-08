import typing_extensions

from ynab_python_sdk.apis.tags import TagValues
from ynab_python_sdk.apis.tags.transactions_api import TransactionsApi
from ynab_python_sdk.apis.tags.categories_api import CategoriesApi
from ynab_python_sdk.apis.tags.budgets_api import BudgetsApi
from ynab_python_sdk.apis.tags.accounts_api import AccountsApi
from ynab_python_sdk.apis.tags.payee_locations_api import PayeeLocationsApi
from ynab_python_sdk.apis.tags.payees_api import PayeesApi
from ynab_python_sdk.apis.tags.months_api import MonthsApi
from ynab_python_sdk.apis.tags.scheduled_transactions_api import ScheduledTransactionsApi
from ynab_python_sdk.apis.tags.user_api import UserApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.CATEGORIES: CategoriesApi,
        TagValues.BUDGETS: BudgetsApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.PAYEE_LOCATIONS: PayeeLocationsApi,
        TagValues.PAYEES: PayeesApi,
        TagValues.MONTHS: MonthsApi,
        TagValues.SCHEDULED_TRANSACTIONS: ScheduledTransactionsApi,
        TagValues.USER: UserApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.CATEGORIES: CategoriesApi,
        TagValues.BUDGETS: BudgetsApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.PAYEE_LOCATIONS: PayeeLocationsApi,
        TagValues.PAYEES: PayeesApi,
        TagValues.MONTHS: MonthsApi,
        TagValues.SCHEDULED_TRANSACTIONS: ScheduledTransactionsApi,
        TagValues.USER: UserApi,
    }
)
