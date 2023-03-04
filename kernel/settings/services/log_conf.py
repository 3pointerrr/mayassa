import toml
import logging.config
import os

from kernel.settings.base import BASE_DIR

if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.makedirs(os.path.join(BASE_DIR, 'logs'))

if not os.path.exists(os.path.join(BASE_DIR, 'logs', 'auth')):
    os.makedirs(os.path.join(BASE_DIR, 'logs', 'auth'))

if not os.path.exists(os.path.join(BASE_DIR, 'logs', 'core')):
    os.makedirs(os.path.join(BASE_DIR, 'logs', 'core'))


with open('logging.toml') as config_file:
    log_config = toml.load(config_file)
    logging.config.dictConfig(log_config)


# LOGGING = {

#     'version': 1,
#     'disable_existing_loggers': False,

#     'loggers': {
#         'core': {
#             'handlers': [

#             ]
#         }
#     }
# }
