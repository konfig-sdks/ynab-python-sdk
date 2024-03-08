# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from ynab_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    USER = "/user"
    BUDGETS = "/budgets"
    BUDGETS_BUDGET_ID = "/budgets/{budget_id}"
    BUDGETS_BUDGET_ID_SETTINGS = "/budgets/{budget_id}/settings"
    BUDGETS_BUDGET_ID_ACCOUNTS = "/budgets/{budget_id}/accounts"
    BUDGETS_BUDGET_ID_ACCOUNTS_ACCOUNT_ID = "/budgets/{budget_id}/accounts/{account_id}"
    BUDGETS_BUDGET_ID_CATEGORIES = "/budgets/{budget_id}/categories"
    BUDGETS_BUDGET_ID_CATEGORIES_CATEGORY_ID = "/budgets/{budget_id}/categories/{category_id}"
    BUDGETS_BUDGET_ID_MONTHS_MONTH_CATEGORIES_CATEGORY_ID = "/budgets/{budget_id}/months/{month}/categories/{category_id}"
    BUDGETS_BUDGET_ID_PAYEES = "/budgets/{budget_id}/payees"
    BUDGETS_BUDGET_ID_PAYEES_PAYEE_ID = "/budgets/{budget_id}/payees/{payee_id}"
    BUDGETS_BUDGET_ID_PAYEE_LOCATIONS = "/budgets/{budget_id}/payee_locations"
    BUDGETS_BUDGET_ID_PAYEE_LOCATIONS_PAYEE_LOCATION_ID = "/budgets/{budget_id}/payee_locations/{payee_location_id}"
    BUDGETS_BUDGET_ID_PAYEES_PAYEE_ID_PAYEE_LOCATIONS = "/budgets/{budget_id}/payees/{payee_id}/payee_locations"
    BUDGETS_BUDGET_ID_MONTHS = "/budgets/{budget_id}/months"
    BUDGETS_BUDGET_ID_MONTHS_MONTH = "/budgets/{budget_id}/months/{month}"
    BUDGETS_BUDGET_ID_TRANSACTIONS = "/budgets/{budget_id}/transactions"
    BUDGETS_BUDGET_ID_TRANSACTIONS_IMPORT = "/budgets/{budget_id}/transactions/import"
    BUDGETS_BUDGET_ID_TRANSACTIONS_TRANSACTION_ID = "/budgets/{budget_id}/transactions/{transaction_id}"
    BUDGETS_BUDGET_ID_ACCOUNTS_ACCOUNT_ID_TRANSACTIONS = "/budgets/{budget_id}/accounts/{account_id}/transactions"
    BUDGETS_BUDGET_ID_CATEGORIES_CATEGORY_ID_TRANSACTIONS = "/budgets/{budget_id}/categories/{category_id}/transactions"
    BUDGETS_BUDGET_ID_PAYEES_PAYEE_ID_TRANSACTIONS = "/budgets/{budget_id}/payees/{payee_id}/transactions"
    BUDGETS_BUDGET_ID_SCHEDULED_TRANSACTIONS = "/budgets/{budget_id}/scheduled_transactions"
    BUDGETS_BUDGET_ID_SCHEDULED_TRANSACTIONS_SCHEDULED_TRANSACTION_ID = "/budgets/{budget_id}/scheduled_transactions/{scheduled_transaction_id}"
