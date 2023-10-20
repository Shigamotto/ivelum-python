import sys

from ..env import config

__all__ = [
    "LOGGING",
]

# fmt: off
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s.%(module)s->%(funcName)s(%(lineno)d): %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': config.get('LOGGING_CONSOLE_FORMAT', default='standard'),
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': config.get('LOGGER_ROOT_LEVEL', default='INFO'),
            'propagate': True
        },
        'django': {
            'handlers': ['console'],
            'level': config.get('LOGGER_DJANGO_LEVEL', default='INFO'),
            'propagate': False
        },
        'django.request': {
            'handlers': ['console'],
            'level': config.get('LOGGER_DJANGO_REQUEST_LEVEL', default='INFO'),
            'propagate': False
        },
        'django.template': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False
        },
        'proxy_service.': {
            'handlers': ['console'],
            'level': config.get('LOGGER_APP_LEVEL', default='INFO'),
            'propagate': False
        },
        'proxy_service.apps.hacker_news.client': {
            'handlers': ['console'],
            'level': config.get('LOGGER_HACKER_NEWS_CLIENT_LEVEL', default='INFO'),
            'propagate': False
        },
        'proxy_service.apps.hacker_news.rules.common': {
            'handlers': ['console'],
            'level': config.get('LOGGER_HACKER_NEWS_RULES_RENDERER_LEVEL', default='INFO'),
            'propagate': False
        },
    },
}
# fmt: on
