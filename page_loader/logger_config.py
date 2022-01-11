"""logger configuration."""

configuring_dict = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            'format':
                '{levelname}|{asctime}|{module}|{funcName}:{lineno} {message}',
                'style': '{',
        },
    },

    'handlers': {
        'to_file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            'filename': 'loader.log',
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
