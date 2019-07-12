from config.settings.base import *

env = os.environ.get('ENVIRONMENT')
if env == 'PROD':
    from .prod import *
elif env == 'DEV':
    from .dev import *
