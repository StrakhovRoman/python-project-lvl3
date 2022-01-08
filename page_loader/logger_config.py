"""logger configuration."""

logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            'format':
                '{asctime} - {levelname} - {module}: {funcName}: {lineno} - {message}',
                'style': '{',
        },
        'console_format': {
            'format':
                '{message}',
                'style': '{',
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'console_format',
        },
        'to_file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            'filename': 'apploader.log',
            'mode': 'w',
        },
    },

    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['to_file'],
        },
    },
}
