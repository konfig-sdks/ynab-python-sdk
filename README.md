<div align="center">

[![Visit You need a budget](./header.png)](https://api.youneedabudget.com)

# You need a budget<a id="you-need-a-budget"></a>

Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`ynab.accounts.create_new_account`](#ynabaccountscreate_new_account)
  * [`ynab.accounts.get_single_account`](#ynabaccountsget_single_account)
  * [`ynab.accounts.list_all`](#ynabaccountslist_all)
  * [`ynab.budgets.get_budget`](#ynabbudgetsget_budget)
  * [`ynab.budgets.get_settings`](#ynabbudgetsget_settings)
  * [`ynab.budgets.list_summary`](#ynabbudgetslist_summary)
  * [`ynab.categories.get_month_category_by_id`](#ynabcategoriesget_month_category_by_id)
  * [`ynab.categories.get_single_category`](#ynabcategoriesget_single_category)
  * [`ynab.categories.list_by_budget_id`](#ynabcategorieslist_by_budget_id)
  * [`ynab.categories.update_category_by_id`](#ynabcategoriesupdate_category_by_id)
  * [`ynab.categories.update_month_category`](#ynabcategoriesupdate_month_category)
  * [`ynab.months.get_single`](#ynabmonthsget_single)
  * [`ynab.months.list`](#ynabmonthslist)
  * [`ynab.payee_locations.get_single`](#ynabpayee_locationsget_single)
  * [`ynab.payee_locations.list_all`](#ynabpayee_locationslist_all)
  * [`ynab.payee_locations.list_by_payee`](#ynabpayee_locationslist_by_payee)
  * [`ynab.payees.get_single_payee`](#ynabpayeesget_single_payee)
  * [`ynab.payees.list_all`](#ynabpayeeslist_all)
  * [`ynab.scheduled_transactions.get_single_scheduled_transaction`](#ynabscheduled_transactionsget_single_scheduled_transaction)
  * [`ynab.scheduled_transactions.list_all`](#ynabscheduled_transactionslist_all)
  * [`ynab.transactions.create_single_or_multiple`](#ynabtransactionscreate_single_or_multiple)
  * [`ynab.transactions.delete_existing_transaction`](#ynabtransactionsdelete_existing_transaction)
  * [`ynab.transactions.get_single_transaction`](#ynabtransactionsget_single_transaction)
  * [`ynab.transactions.import_linked_accounts`](#ynabtransactionsimport_linked_accounts)
  * [`ynab.transactions.list_by_account`](#ynabtransactionslist_by_account)
  * [`ynab.transactions.list_by_category`](#ynabtransactionslist_by_category)
  * [`ynab.transactions.list_by_payee`](#ynabtransactionslist_by_payee)
  * [`ynab.transactions.list_transactions`](#ynabtransactionslist_transactions)
  * [`ynab.transactions.update_existing_transaction`](#ynabtransactionsupdate_existing_transaction)
  * [`ynab.transactions.update_multiple`](#ynabtransactionsupdate_multiple)
  * [`ynab.user.info_get`](#ynabuserinfo_get)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=You%20Need%20A%20Budget&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from ynab_python_sdk import Ynab, ApiException

ynab = Ynab(access_token="YOUR_BEARER_TOKEN")

try:
    # Create a new account
    create_new_account_response = ynab.accounts.create_new_account(
        account={
            "name": "name_example",
            "type": "checking",
            "balance": 1,
        },
        budget_id="budget_id_example",
    )
    print(create_new_account_response)
except ApiException as e:
    print("Exception when calling AccountsApi.create_new_account: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from ynab_python_sdk import Ynab, ApiException

ynab = Ynab(access_token="YOUR_BEARER_TOKEN")


async def main():
    try:
        # Create a new account
        create_new_account_response = await ynab.accounts.acreate_new_account(
            account={
                "name": "name_example",
                "type": "checking",
                "balance": 1,
            },
            budget_id="budget_id_example",
        )
        print(create_new_account_response)
    except ApiException as e:
        print("Exception when calling AccountsApi.create_new_account: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["error"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from ynab_python_sdk import Ynab, ApiException

ynab = Ynab(access_token="YOUR_BEARER_TOKEN")

try:
    # Create a new account
    create_new_account_response = ynab.accounts.raw.create_new_account(
        account={
            "name": "name_example",
            "type": "checking",
            "balance": 1,
        },
        budget_id="budget_id_example",
    )
    pprint(create_new_account_response.body)
    pprint(create_new_account_response.body["data"])
    pprint(create_new_account_response.headers)
    pprint(create_new_account_response.status)
    pprint(create_new_account_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountsApi.create_new_account: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["error"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `ynab.accounts.create_new_account`<a id="ynabaccountscreate_new_account"></a>

Creates a new account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_account_response = ynab.accounts.create_new_account(
    account={
        "name": "name_example",
        "type": "checking",
        "balance": 1,
    },
    budget_id="budget_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account: [`SaveAccount`](./ynab_python_sdk/type/save_account.py)<a id="account-saveaccountynab_python_sdktypesave_accountpy"></a>


##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget (\"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget)

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostAccountWrapper`](./ynab_python_sdk/type/post_account_wrapper.py)
The account to create.

#### 🔄 Return<a id="🔄-return"></a>

[`AccountResponse`](./ynab_python_sdk/pydantic/account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.accounts.get_single_account`<a id="ynabaccountsget_single_account"></a>

Returns a single account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_account_response = ynab.accounts.get_single_account(
    budget_id="budget_id_example",
    account_id="account_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### account_id: `str`<a id="account_id-str"></a>

The id of the account

#### 🔄 Return<a id="🔄-return"></a>

[`AccountResponse`](./ynab_python_sdk/pydantic/account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/accounts/{account_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.accounts.list_all`<a id="ynabaccountslist_all"></a>

Returns all accounts

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = ynab.accounts.list_all(
    budget_id="budget_id_example",
    last_knowledge_of_server=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### last_knowledge_of_server: `int`<a id="last_knowledge_of_server-int"></a>

The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.

#### 🔄 Return<a id="🔄-return"></a>

[`AccountsResponse`](./ynab_python_sdk/pydantic/accounts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.budgets.get_budget`<a id="ynabbudgetsget_budget"></a>

Returns a single budget with all related entities.  This resource is effectively a full budget export.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_budget_response = ynab.budgets.get_budget(
    budget_id="budget_id_example",
    last_knowledge_of_server=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### last_knowledge_of_server: `int`<a id="last_knowledge_of_server-int"></a>

The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.

#### 🔄 Return<a id="🔄-return"></a>

[`BudgetDetailResponse`](./ynab_python_sdk/pydantic/budget_detail_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.budgets.get_settings`<a id="ynabbudgetsget_settings"></a>

Returns settings for a budget

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_settings_response = ynab.budgets.get_settings(
    budget_id="budget_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

#### 🔄 Return<a id="🔄-return"></a>

[`BudgetSettingsResponse`](./ynab_python_sdk/pydantic/budget_settings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/settings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.budgets.list_summary`<a id="ynabbudgetslist_summary"></a>

Returns budgets list with summary information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_summary_response = ynab.budgets.list_summary(
    include_accounts=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### include_accounts: `bool`<a id="include_accounts-bool"></a>

Whether to include the list of budget accounts

#### 🔄 Return<a id="🔄-return"></a>

[`BudgetSummaryResponse`](./ynab_python_sdk/pydantic/budget_summary_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.categories.get_month_category_by_id`<a id="ynabcategoriesget_month_category_by_id"></a>

Returns a single category for a specific budget month.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_month_category_by_id_response = ynab.categories.get_month_category_by_id(
    budget_id="budget_id_example",
    month="1970-01-01",
    category_id="category_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### month: `date`<a id="month-date"></a>

The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))

##### category_id: `str`<a id="category_id-str"></a>

The id of the category

#### 🔄 Return<a id="🔄-return"></a>

[`CategoryResponse`](./ynab_python_sdk/pydantic/category_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/months/{month}/categories/{category_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.categories.get_single_category`<a id="ynabcategoriesget_single_category"></a>

Returns a single category.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_category_response = ynab.categories.get_single_category(
    budget_id="budget_id_example",
    category_id="category_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### category_id: `str`<a id="category_id-str"></a>

The id of the category

#### 🔄 Return<a id="🔄-return"></a>

[`CategoryResponse`](./ynab_python_sdk/pydantic/category_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/categories/{category_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.categories.list_by_budget_id`<a id="ynabcategorieslist_by_budget_id"></a>

Returns all categories grouped by category group.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_budget_id_response = ynab.categories.list_by_budget_id(
    budget_id="budget_id_example",
    last_knowledge_of_server=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### last_knowledge_of_server: `int`<a id="last_knowledge_of_server-int"></a>

The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.

#### 🔄 Return<a id="🔄-return"></a>

[`CategoriesResponse`](./ynab_python_sdk/pydantic/categories_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/categories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.categories.update_category_by_id`<a id="ynabcategoriesupdate_category_by_id"></a>

Update a category

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_category_by_id_response = ynab.categories.update_category_by_id(
    category={},
    budget_id="budget_id_example",
    category_id="category_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category: [`SaveCategory`](./ynab_python_sdk/type/save_category.py)<a id="category-savecategoryynab_python_sdktypesave_categorypy"></a>


##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### category_id: `str`<a id="category_id-str"></a>

The id of the category

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PatchCategoryWrapper`](./ynab_python_sdk/type/patch_category_wrapper.py)
The category to update

#### 🔄 Return<a id="🔄-return"></a>

[`SaveCategoryResponse`](./ynab_python_sdk/pydantic/save_category_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/categories/{category_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.categories.update_month_category`<a id="ynabcategoriesupdate_month_category"></a>

Update a category for a specific month.  Only `budgeted` amount can be updated.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_month_category_response = ynab.categories.update_month_category(
    category={
        "budgeted": 1,
    },
    budget_id="budget_id_example",
    month="1970-01-01",
    category_id="category_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### category: [`SaveMonthCategory`](./ynab_python_sdk/type/save_month_category.py)<a id="category-savemonthcategoryynab_python_sdktypesave_month_categorypy"></a>


##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### month: `date`<a id="month-date"></a>

The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))

##### category_id: `str`<a id="category_id-str"></a>

The id of the category

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PatchMonthCategoryWrapper`](./ynab_python_sdk/type/patch_month_category_wrapper.py)
The category to update.  Only `budgeted` amount can be updated and any other fields specified will be ignored.

#### 🔄 Return<a id="🔄-return"></a>

[`SaveCategoryResponse`](./ynab_python_sdk/pydantic/save_category_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/months/{month}/categories/{category_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.months.get_single`<a id="ynabmonthsget_single"></a>

Returns a single budget month

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_response = ynab.months.get_single(
    budget_id="budget_id_example",
    month="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### month: `date`<a id="month-date"></a>

The budget month in ISO format (e.g. 2016-12-01) (\"current\" can also be used to specify the current calendar month (UTC))

#### 🔄 Return<a id="🔄-return"></a>

[`MonthDetailResponse`](./ynab_python_sdk/pydantic/month_detail_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/months/{month}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.months.list`<a id="ynabmonthslist"></a>

Returns all budget months

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = ynab.months.list(
    budget_id="budget_id_example",
    last_knowledge_of_server=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### last_knowledge_of_server: `int`<a id="last_knowledge_of_server-int"></a>

The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.

#### 🔄 Return<a id="🔄-return"></a>

[`MonthSummariesResponse`](./ynab_python_sdk/pydantic/month_summaries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/months` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.payee_locations.get_single`<a id="ynabpayee_locationsget_single"></a>

Returns a single payee location

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_response = ynab.payee_locations.get_single(
    budget_id="budget_id_example",
    payee_location_id="payee_location_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### payee_location_id: `str`<a id="payee_location_id-str"></a>

id of payee location

#### 🔄 Return<a id="🔄-return"></a>

[`PayeeLocationResponse`](./ynab_python_sdk/pydantic/payee_location_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/payee_locations/{payee_location_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.payee_locations.list_all`<a id="ynabpayee_locationslist_all"></a>

Returns all payee locations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = ynab.payee_locations.list_all(
    budget_id="budget_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

#### 🔄 Return<a id="🔄-return"></a>

[`PayeeLocationsResponse`](./ynab_python_sdk/pydantic/payee_locations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/payee_locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.payee_locations.list_by_payee`<a id="ynabpayee_locationslist_by_payee"></a>

Returns all payee locations for a specified payee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_payee_response = ynab.payee_locations.list_by_payee(
    budget_id="budget_id_example",
    payee_id="payee_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### payee_id: `str`<a id="payee_id-str"></a>

id of payee

#### 🔄 Return<a id="🔄-return"></a>

[`PayeeLocationsResponse`](./ynab_python_sdk/pydantic/payee_locations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/payees/{payee_id}/payee_locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.payees.get_single_payee`<a id="ynabpayeesget_single_payee"></a>

Returns a single payee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_payee_response = ynab.payees.get_single_payee(
    budget_id="budget_id_example",
    payee_id="payee_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### payee_id: `str`<a id="payee_id-str"></a>

The id of the payee

#### 🔄 Return<a id="🔄-return"></a>

[`PayeeResponse`](./ynab_python_sdk/pydantic/payee_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/payees/{payee_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.payees.list_all`<a id="ynabpayeeslist_all"></a>

Returns all payees

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = ynab.payees.list_all(
    budget_id="budget_id_example",
    last_knowledge_of_server=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### last_knowledge_of_server: `int`<a id="last_knowledge_of_server-int"></a>

The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.

#### 🔄 Return<a id="🔄-return"></a>

[`PayeesResponse`](./ynab_python_sdk/pydantic/payees_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/payees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.scheduled_transactions.get_single_scheduled_transaction`<a id="ynabscheduled_transactionsget_single_scheduled_transaction"></a>

Returns a single scheduled transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_scheduled_transaction_response = (
    ynab.scheduled_transactions.get_single_scheduled_transaction(
        budget_id="budget_id_example",
        scheduled_transaction_id="scheduled_transaction_id_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### scheduled_transaction_id: `str`<a id="scheduled_transaction_id-str"></a>

The id of the scheduled transaction

#### 🔄 Return<a id="🔄-return"></a>

[`ScheduledTransactionResponse`](./ynab_python_sdk/pydantic/scheduled_transaction_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/scheduled_transactions/{scheduled_transaction_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.scheduled_transactions.list_all`<a id="ynabscheduled_transactionslist_all"></a>

Returns all scheduled transactions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = ynab.scheduled_transactions.list_all(
    budget_id="budget_id_example",
    last_knowledge_of_server=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### last_knowledge_of_server: `int`<a id="last_knowledge_of_server-int"></a>

The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.

#### 🔄 Return<a id="🔄-return"></a>

[`ScheduledTransactionsResponse`](./ynab_python_sdk/pydantic/scheduled_transactions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/scheduled_transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.transactions.create_single_or_multiple`<a id="ynabtransactionscreate_single_or_multiple"></a>

Creates a single transaction or multiple transactions.  If you provide a body containing a `transaction` object, a single transaction will be created and if you provide a body containing a `transactions` array, multiple transactions will be created.  Scheduled transactions cannot be created on this endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_single_or_multiple_response = ynab.transactions.create_single_or_multiple(
    budget_id="budget_id_example",
    transaction=None,
    transactions=[None],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### transaction: [`NewTransaction`](./ynab_python_sdk/type/new_transaction.py)<a id="transaction-newtransactionynab_python_sdktypenew_transactionpy"></a>


##### transactions: List[`NewTransaction`]<a id="transactions-listnewtransaction"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostTransactionsWrapper`](./ynab_python_sdk/type/post_transactions_wrapper.py)
The transaction or transactions to create.  To create a single transaction you can specify a value for the `transaction` object and to create multiple transactions you can specify an array of `transactions`.  It is expected that you will only provide a value for one of these objects.

#### 🔄 Return<a id="🔄-return"></a>

[`SaveTransactionsResponse`](./ynab_python_sdk/pydantic/save_transactions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/transactions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.transactions.delete_existing_transaction`<a id="ynabtransactionsdelete_existing_transaction"></a>

Deletes a transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_existing_transaction_response = ynab.transactions.delete_existing_transaction(
    budget_id="budget_id_example",
    transaction_id="transaction_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### transaction_id: `str`<a id="transaction_id-str"></a>

The id of the transaction

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionResponse`](./ynab_python_sdk/pydantic/transaction_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/transactions/{transaction_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.transactions.get_single_transaction`<a id="ynabtransactionsget_single_transaction"></a>

Returns a single transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_transaction_response = ynab.transactions.get_single_transaction(
    budget_id="budget_id_example",
    transaction_id="transaction_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### transaction_id: `str`<a id="transaction_id-str"></a>

The id of the transaction

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionResponse`](./ynab_python_sdk/pydantic/transaction_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/transactions/{transaction_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.transactions.import_linked_accounts`<a id="ynabtransactionsimport_linked_accounts"></a>

Imports available transactions on all linked accounts for the given budget.  Linked accounts allow transactions to be imported directly from a specified financial institution and this endpoint initiates that import.  Sending a request to this endpoint is the equivalent of clicking "Import" on each account in the web application or tapping the "New Transactions" banner in the mobile applications.  The response for this endpoint contains the transaction ids that have been imported.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
import_linked_accounts_response = ynab.transactions.import_linked_accounts(
    budget_id="budget_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionsImportResponse`](./ynab_python_sdk/pydantic/transactions_import_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/transactions/import` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.transactions.list_by_account`<a id="ynabtransactionslist_by_account"></a>

Returns all transactions for a specified account

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_account_response = ynab.transactions.list_by_account(
    budget_id="budget_id_example",
    account_id="account_id_example",
    since_date="1970-01-01",
    type="uncategorized",
    last_knowledge_of_server=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### account_id: `str`<a id="account_id-str"></a>

The id of the account

##### since_date: `date`<a id="since_date-date"></a>

If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).

##### type: `str`<a id="type-str"></a>

If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported.

##### last_knowledge_of_server: `int`<a id="last_knowledge_of_server-int"></a>

The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionsResponse`](./ynab_python_sdk/pydantic/transactions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/accounts/{account_id}/transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.transactions.list_by_category`<a id="ynabtransactionslist_by_category"></a>

Returns all transactions for a specified category

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_category_response = ynab.transactions.list_by_category(
    budget_id="budget_id_example",
    category_id="category_id_example",
    since_date="1970-01-01",
    type="uncategorized",
    last_knowledge_of_server=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### category_id: `str`<a id="category_id-str"></a>

The id of the category

##### since_date: `date`<a id="since_date-date"></a>

If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).

##### type: `str`<a id="type-str"></a>

If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported.

##### last_knowledge_of_server: `int`<a id="last_knowledge_of_server-int"></a>

The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.

#### 🔄 Return<a id="🔄-return"></a>

[`HybridTransactionsResponse`](./ynab_python_sdk/pydantic/hybrid_transactions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/categories/{category_id}/transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.transactions.list_by_payee`<a id="ynabtransactionslist_by_payee"></a>

Returns all transactions for a specified payee

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_payee_response = ynab.transactions.list_by_payee(
    budget_id="budget_id_example",
    payee_id="payee_id_example",
    since_date="1970-01-01",
    type="uncategorized",
    last_knowledge_of_server=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### payee_id: `str`<a id="payee_id-str"></a>

The id of the payee

##### since_date: `date`<a id="since_date-date"></a>

If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).

##### type: `str`<a id="type-str"></a>

If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported.

##### last_knowledge_of_server: `int`<a id="last_knowledge_of_server-int"></a>

The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.

#### 🔄 Return<a id="🔄-return"></a>

[`HybridTransactionsResponse`](./ynab_python_sdk/pydantic/hybrid_transactions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/payees/{payee_id}/transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.transactions.list_transactions`<a id="ynabtransactionslist_transactions"></a>

Returns budget transactions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_transactions_response = ynab.transactions.list_transactions(
    budget_id="budget_id_example",
    since_date="1970-01-01",
    type="uncategorized",
    last_knowledge_of_server=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### since_date: `date`<a id="since_date-date"></a>

If specified, only transactions on or after this date will be included.  The date should be ISO formatted (e.g. 2016-12-30).

##### type: `str`<a id="type-str"></a>

If specified, only transactions of the specified type will be included. \"uncategorized\" and \"unapproved\" are currently supported.

##### last_knowledge_of_server: `int`<a id="last_knowledge_of_server-int"></a>

The starting server knowledge.  If provided, only entities that have changed since `last_knowledge_of_server` will be included.

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionsResponse`](./ynab_python_sdk/pydantic/transactions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.transactions.update_existing_transaction`<a id="ynabtransactionsupdate_existing_transaction"></a>

Updates a single transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_existing_transaction_response = ynab.transactions.update_existing_transaction(
    transaction=None,
    budget_id="budget_id_example",
    transaction_id="transaction_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transaction: [`ExistingTransaction`](./ynab_python_sdk/type/existing_transaction.py)<a id="transaction-existingtransactionynab_python_sdktypeexisting_transactionpy"></a>


##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

##### transaction_id: `str`<a id="transaction_id-str"></a>

The id of the transaction

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PutTransactionWrapper`](./ynab_python_sdk/type/put_transaction_wrapper.py)
The transaction to update

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionResponse`](./ynab_python_sdk/pydantic/transaction_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/transactions/{transaction_id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.transactions.update_multiple`<a id="ynabtransactionsupdate_multiple"></a>

Updates multiple transactions, by `id` or `import_id`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_multiple_response = ynab.transactions.update_multiple(
    transactions=[None],
    budget_id="budget_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transactions: List[`SaveTransactionWithIdOrImportId`]<a id="transactions-listsavetransactionwithidorimportid"></a>

##### budget_id: `str`<a id="budget_id-str"></a>

The id of the budget. \"last-used\" can be used to specify the last used budget and \"default\" can be used if default budget selection is enabled (see: https://api.ynab.com/#oauth-default-budget).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PatchTransactionsWrapper`](./ynab_python_sdk/type/patch_transactions_wrapper.py)
The transactions to update. Each transaction must have either an `id` or `import_id` specified. If `id` is specified as null an `import_id` value can be provided which will allow transaction(s) to be updated by its `import_id`. If an `id` is specified, it will always be used for lookup.  You should not specify both `id` and `import_id`.  Updating an `import_id` on an existing transaction is not allowed; if an `import_id` is specified, it will only be used to lookup the transaction.

#### 🔄 Return<a id="🔄-return"></a>

[`SaveTransactionsResponse`](./ynab_python_sdk/pydantic/save_transactions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/budgets/{budget_id}/transactions` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `ynab.user.info_get`<a id="ynabuserinfo_get"></a>

Returns authenticated user information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
info_get_response = ynab.user.info_get()
```

#### 🔄 Return<a id="🔄-return"></a>

[`UserResponse`](./ynab_python_sdk/pydantic/user_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/user` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
