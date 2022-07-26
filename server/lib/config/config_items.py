config_items = [
    {
        'key': 'log_level',
        'env_var': 'LOG_LEVEL',
        'default': 30
    },
    {
        'key': 'test_app_config',
        'env_var': 'TEST_APP_CONFIG',
        'default': 'config.env'
    },
    {
        'key': 'database',
        'default': 'postgresql'
    },
    {
        'key': 'connections',
        'env_var': 'CONNECTIONS',
        'default': ''
    },
    {
        'key': 'shop_system',
        'env_var': 'SHOP_SYSTEM',
        'default': [('machan', 'fire')]
    }
]