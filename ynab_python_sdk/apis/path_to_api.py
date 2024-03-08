import typing_extensions

from ynab_python_sdk.paths import PathValues
from ynab_python_sdk.apis.paths.user import User
from ynab_python_sdk.apis.paths.budgets import Budgets
from ynab_python_sdk.apis.paths.budgets_budget_id import BudgetsBudgetId
from ynab_python_sdk.apis.paths.budgets_budget_id_settings import BudgetsBudgetIdSettings
from ynab_python_sdk.apis.paths.budgets_budget_id_accounts import BudgetsBudgetIdAccounts
from ynab_python_sdk.apis.paths.budgets_budget_id_accounts_account_id import BudgetsBudgetIdAccountsAccountId
from ynab_python_sdk.apis.paths.budgets_budget_id_categories import BudgetsBudgetIdCategories
from ynab_python_sdk.apis.paths.budgets_budget_id_categories_category_id import BudgetsBudgetIdCategoriesCategoryId
from ynab_python_sdk.apis.paths.budgets_budget_id_months_month_categories_category_id import BudgetsBudgetIdMonthsMonthCategoriesCategoryId
from ynab_python_sdk.apis.paths.budgets_budget_id_payees import BudgetsBudgetIdPayees
from ynab_python_sdk.apis.paths.budgets_budget_id_payees_payee_id import BudgetsBudgetIdPayeesPayeeId
from ynab_python_sdk.apis.paths.budgets_budget_id_payee_locations import BudgetsBudgetIdPayeeLocations
from ynab_python_sdk.apis.paths.budgets_budget_id_payee_locations_payee_location_id import BudgetsBudgetIdPayeeLocationsPayeeLocationId
from ynab_python_sdk.apis.paths.budgets_budget_id_payees_payee_id_payee_locations import BudgetsBudgetIdPayeesPayeeIdPayeeLocations
from ynab_python_sdk.apis.paths.budgets_budget_id_months import BudgetsBudgetIdMonths
from ynab_python_sdk.apis.paths.budgets_budget_id_months_month import BudgetsBudgetIdMonthsMonth
from ynab_python_sdk.apis.paths.budgets_budget_id_transactions import BudgetsBudgetIdTransactions
from ynab_python_sdk.apis.paths.budgets_budget_id_transactions_import import BudgetsBudgetIdTransactionsImport
from ynab_python_sdk.apis.paths.budgets_budget_id_transactions_transaction_id import BudgetsBudgetIdTransactionsTransactionId
from ynab_python_sdk.apis.paths.budgets_budget_id_accounts_account_id_transactions import BudgetsBudgetIdAccountsAccountIdTransactions
from ynab_python_sdk.apis.paths.budgets_budget_id_categories_category_id_transactions import BudgetsBudgetIdCategoriesCategoryIdTransactions
from ynab_python_sdk.apis.paths.budgets_budget_id_payees_payee_id_transactions import BudgetsBudgetIdPayeesPayeeIdTransactions
from ynab_python_sdk.apis.paths.budgets_budget_id_scheduled_transactions import BudgetsBudgetIdScheduledTransactions
from ynab_python_sdk.apis.paths.budgets_budget_id_scheduled_transactions_scheduled_transaction_id import BudgetsBudgetIdScheduledTransactionsScheduledTransactionId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.USER: User,
        PathValues.BUDGETS: Budgets,
        PathValues.BUDGETS_BUDGET_ID: BudgetsBudgetId,
        PathValues.BUDGETS_BUDGET_ID_SETTINGS: BudgetsBudgetIdSettings,
        PathValues.BUDGETS_BUDGET_ID_ACCOUNTS: BudgetsBudgetIdAccounts,
        PathValues.BUDGETS_BUDGET_ID_ACCOUNTS_ACCOUNT_ID: BudgetsBudgetIdAccountsAccountId,
        PathValues.BUDGETS_BUDGET_ID_CATEGORIES: BudgetsBudgetIdCategories,
        PathValues.BUDGETS_BUDGET_ID_CATEGORIES_CATEGORY_ID: BudgetsBudgetIdCategoriesCategoryId,
        PathValues.BUDGETS_BUDGET_ID_MONTHS_MONTH_CATEGORIES_CATEGORY_ID: BudgetsBudgetIdMonthsMonthCategoriesCategoryId,
        PathValues.BUDGETS_BUDGET_ID_PAYEES: BudgetsBudgetIdPayees,
        PathValues.BUDGETS_BUDGET_ID_PAYEES_PAYEE_ID: BudgetsBudgetIdPayeesPayeeId,
        PathValues.BUDGETS_BUDGET_ID_PAYEE_LOCATIONS: BudgetsBudgetIdPayeeLocations,
        PathValues.BUDGETS_BUDGET_ID_PAYEE_LOCATIONS_PAYEE_LOCATION_ID: BudgetsBudgetIdPayeeLocationsPayeeLocationId,
        PathValues.BUDGETS_BUDGET_ID_PAYEES_PAYEE_ID_PAYEE_LOCATIONS: BudgetsBudgetIdPayeesPayeeIdPayeeLocations,
        PathValues.BUDGETS_BUDGET_ID_MONTHS: BudgetsBudgetIdMonths,
        PathValues.BUDGETS_BUDGET_ID_MONTHS_MONTH: BudgetsBudgetIdMonthsMonth,
        PathValues.BUDGETS_BUDGET_ID_TRANSACTIONS: BudgetsBudgetIdTransactions,
        PathValues.BUDGETS_BUDGET_ID_TRANSACTIONS_IMPORT: BudgetsBudgetIdTransactionsImport,
        PathValues.BUDGETS_BUDGET_ID_TRANSACTIONS_TRANSACTION_ID: BudgetsBudgetIdTransactionsTransactionId,
        PathValues.BUDGETS_BUDGET_ID_ACCOUNTS_ACCOUNT_ID_TRANSACTIONS: BudgetsBudgetIdAccountsAccountIdTransactions,
        PathValues.BUDGETS_BUDGET_ID_CATEGORIES_CATEGORY_ID_TRANSACTIONS: BudgetsBudgetIdCategoriesCategoryIdTransactions,
        PathValues.BUDGETS_BUDGET_ID_PAYEES_PAYEE_ID_TRANSACTIONS: BudgetsBudgetIdPayeesPayeeIdTransactions,
        PathValues.BUDGETS_BUDGET_ID_SCHEDULED_TRANSACTIONS: BudgetsBudgetIdScheduledTransactions,
        PathValues.BUDGETS_BUDGET_ID_SCHEDULED_TRANSACTIONS_SCHEDULED_TRANSACTION_ID: BudgetsBudgetIdScheduledTransactionsScheduledTransactionId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.USER: User,
        PathValues.BUDGETS: Budgets,
        PathValues.BUDGETS_BUDGET_ID: BudgetsBudgetId,
        PathValues.BUDGETS_BUDGET_ID_SETTINGS: BudgetsBudgetIdSettings,
        PathValues.BUDGETS_BUDGET_ID_ACCOUNTS: BudgetsBudgetIdAccounts,
        PathValues.BUDGETS_BUDGET_ID_ACCOUNTS_ACCOUNT_ID: BudgetsBudgetIdAccountsAccountId,
        PathValues.BUDGETS_BUDGET_ID_CATEGORIES: BudgetsBudgetIdCategories,
        PathValues.BUDGETS_BUDGET_ID_CATEGORIES_CATEGORY_ID: BudgetsBudgetIdCategoriesCategoryId,
        PathValues.BUDGETS_BUDGET_ID_MONTHS_MONTH_CATEGORIES_CATEGORY_ID: BudgetsBudgetIdMonthsMonthCategoriesCategoryId,
        PathValues.BUDGETS_BUDGET_ID_PAYEES: BudgetsBudgetIdPayees,
        PathValues.BUDGETS_BUDGET_ID_PAYEES_PAYEE_ID: BudgetsBudgetIdPayeesPayeeId,
        PathValues.BUDGETS_BUDGET_ID_PAYEE_LOCATIONS: BudgetsBudgetIdPayeeLocations,
        PathValues.BUDGETS_BUDGET_ID_PAYEE_LOCATIONS_PAYEE_LOCATION_ID: BudgetsBudgetIdPayeeLocationsPayeeLocationId,
        PathValues.BUDGETS_BUDGET_ID_PAYEES_PAYEE_ID_PAYEE_LOCATIONS: BudgetsBudgetIdPayeesPayeeIdPayeeLocations,
        PathValues.BUDGETS_BUDGET_ID_MONTHS: BudgetsBudgetIdMonths,
        PathValues.BUDGETS_BUDGET_ID_MONTHS_MONTH: BudgetsBudgetIdMonthsMonth,
        PathValues.BUDGETS_BUDGET_ID_TRANSACTIONS: BudgetsBudgetIdTransactions,
        PathValues.BUDGETS_BUDGET_ID_TRANSACTIONS_IMPORT: BudgetsBudgetIdTransactionsImport,
        PathValues.BUDGETS_BUDGET_ID_TRANSACTIONS_TRANSACTION_ID: BudgetsBudgetIdTransactionsTransactionId,
        PathValues.BUDGETS_BUDGET_ID_ACCOUNTS_ACCOUNT_ID_TRANSACTIONS: BudgetsBudgetIdAccountsAccountIdTransactions,
        PathValues.BUDGETS_BUDGET_ID_CATEGORIES_CATEGORY_ID_TRANSACTIONS: BudgetsBudgetIdCategoriesCategoryIdTransactions,
        PathValues.BUDGETS_BUDGET_ID_PAYEES_PAYEE_ID_TRANSACTIONS: BudgetsBudgetIdPayeesPayeeIdTransactions,
        PathValues.BUDGETS_BUDGET_ID_SCHEDULED_TRANSACTIONS: BudgetsBudgetIdScheduledTransactions,
        PathValues.BUDGETS_BUDGET_ID_SCHEDULED_TRANSACTIONS_SCHEDULED_TRANSACTION_ID: BudgetsBudgetIdScheduledTransactionsScheduledTransactionId,
    }
)
