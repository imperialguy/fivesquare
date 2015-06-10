# Flask settings
DEBUG = True
USE_RELOADER = False

# Database settings
DB_SETTINGS = {'LOCAL': {'DB_NAME': 'fivesquare',
                         'DB_HOST': 'localhost',
                         'DB_PORT': 27017},
               'REMOTE': {'DB_NAME': 'heroku_app36529427',
                          'DB_HOST': 'mongodb://ven:ven@ds047581.mongolab.com:47581/heroku_app36529427',
                          'DB_PORT': 47581,
                          'DB_USER': 'ven',
                          'DB_PASS': 'ven'
                          }
               }
