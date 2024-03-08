operation_parameter_map = {
    '/budgets/{budget_id}/accounts-POST': {
        'parameters': [
            {
                'name': 'account'
            },
            {
                'name': 'budget_id'
            },
        ]
    },
    '/budgets/{budget_id}/accounts/{account_id}-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'account_id'
            },
        ]
    },
    '/budgets/{budget_id}/accounts-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'last_knowledge_of_server'
            },
        ]
    },
    '/budgets/{budget_id}-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'last_knowledge_of_server'
            },
        ]
    },
    '/budgets/{budget_id}/settings-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
        ]
    },
    '/budgets-GET': {
        'parameters': [
            {
                'name': 'include_accounts'
            },
        ]
    },
    '/budgets/{budget_id}/months/{month}/categories/{category_id}-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'month'
            },
            {
                'name': 'category_id'
            },
        ]
    },
    '/budgets/{budget_id}/categories/{category_id}-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'category_id'
            },
        ]
    },
    '/budgets/{budget_id}/categories-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'last_knowledge_of_server'
            },
        ]
    },
    '/budgets/{budget_id}/categories/{category_id}-PATCH': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'budget_id'
            },
            {
                'name': 'category_id'
            },
        ]
    },
    '/budgets/{budget_id}/months/{month}/categories/{category_id}-PATCH': {
        'parameters': [
            {
                'name': 'category'
            },
            {
                'name': 'budget_id'
            },
            {
                'name': 'month'
            },
            {
                'name': 'category_id'
            },
        ]
    },
    '/budgets/{budget_id}/months/{month}-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'month'
            },
        ]
    },
    '/budgets/{budget_id}/months-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'last_knowledge_of_server'
            },
        ]
    },
    '/budgets/{budget_id}/payee_locations/{payee_location_id}-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'payee_location_id'
            },
        ]
    },
    '/budgets/{budget_id}/payee_locations-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
        ]
    },
    '/budgets/{budget_id}/payees/{payee_id}/payee_locations-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'payee_id'
            },
        ]
    },
    '/budgets/{budget_id}/payees/{payee_id}-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'payee_id'
            },
        ]
    },
    '/budgets/{budget_id}/payees-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'last_knowledge_of_server'
            },
        ]
    },
    '/budgets/{budget_id}/scheduled_transactions/{scheduled_transaction_id}-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'scheduled_transaction_id'
            },
        ]
    },
    '/budgets/{budget_id}/scheduled_transactions-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'last_knowledge_of_server'
            },
        ]
    },
    '/budgets/{budget_id}/transactions-POST': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'transaction'
            },
            {
                'name': 'transactions'
            },
        ]
    },
    '/budgets/{budget_id}/transactions/{transaction_id}-DELETE': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'transaction_id'
            },
        ]
    },
    '/budgets/{budget_id}/transactions/{transaction_id}-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'transaction_id'
            },
        ]
    },
    '/budgets/{budget_id}/transactions/import-POST': {
        'parameters': [
            {
                'name': 'budget_id'
            },
        ]
    },
    '/budgets/{budget_id}/accounts/{account_id}/transactions-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'account_id'
            },
            {
                'name': 'since_date'
            },
            {
                'name': 'type'
            },
            {
                'name': 'last_knowledge_of_server'
            },
        ]
    },
    '/budgets/{budget_id}/categories/{category_id}/transactions-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'category_id'
            },
            {
                'name': 'since_date'
            },
            {
                'name': 'type'
            },
            {
                'name': 'last_knowledge_of_server'
            },
        ]
    },
    '/budgets/{budget_id}/payees/{payee_id}/transactions-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'payee_id'
            },
            {
                'name': 'since_date'
            },
            {
                'name': 'type'
            },
            {
                'name': 'last_knowledge_of_server'
            },
        ]
    },
    '/budgets/{budget_id}/transactions-GET': {
        'parameters': [
            {
                'name': 'budget_id'
            },
            {
                'name': 'since_date'
            },
            {
                'name': 'type'
            },
            {
                'name': 'last_knowledge_of_server'
            },
        ]
    },
    '/budgets/{budget_id}/transactions/{transaction_id}-PUT': {
        'parameters': [
            {
                'name': 'transaction'
            },
            {
                'name': 'budget_id'
            },
            {
                'name': 'transaction_id'
            },
        ]
    },
    '/budgets/{budget_id}/transactions-PATCH': {
        'parameters': [
            {
                'name': 'transactions'
            },
            {
                'name': 'budget_id'
            },
        ]
    },
    '/user-GET': {
        'parameters': [
        ]
    },
};