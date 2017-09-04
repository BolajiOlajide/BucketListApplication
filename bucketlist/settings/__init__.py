import dotenv

dotenv.load()

if dotenv.get('HEROKU'):
    from .prod import *
else:
    from .dev import *
