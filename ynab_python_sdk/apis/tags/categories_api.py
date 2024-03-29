# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by: https://konfigthis.com
"""

from ynab_python_sdk.paths.budgets_budget_id_months_month_categories_category_id.get import GetMonthCategoryById
from ynab_python_sdk.paths.budgets_budget_id_categories_category_id.get import GetSingleCategory
from ynab_python_sdk.paths.budgets_budget_id_categories.get import ListByBudgetId
from ynab_python_sdk.paths.budgets_budget_id_categories_category_id.patch import UpdateCategoryById
from ynab_python_sdk.paths.budgets_budget_id_months_month_categories_category_id.patch import UpdateMonthCategory
from ynab_python_sdk.apis.tags.categories_api_raw import CategoriesApiRaw


class CategoriesApi(
    GetMonthCategoryById,
    GetSingleCategory,
    ListByBudgetId,
    UpdateCategoryById,
    UpdateMonthCategory,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CategoriesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CategoriesApiRaw(api_client)
