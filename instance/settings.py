# -*- coding: utf-8 -*-
#: Site title
SITE_TITLE = 'HasGeek Static Assets'
#: Site id (for network bar)
SITE_ID = 'assets'
#: Google Analytics code
GA_CODE = ''
#: Google site verification code (inserted as a meta tag)
GOOGLE_SITE_VERIFICATION = ''
#: Typekit code
TYPEKIT_CODE = ''
#: Secret key
SECRET_KEY = 'this will never be used'
#: Cache type
CACHE_TYPE = 'redis'
#: Timezone
TIMEZONE = 'Asia/Kolkata'
#: Lastuser server (should be blank)
LASTUSER_SERVER = ''
#: Lastuser client id
LASTUSER_CLIENT_ID = ''
#: Lastuser client secret
LASTUSER_CLIENT_SECRET = ''
#: Mail settings
#: MAIL_FAIL_SILENTLY : default True
#: MAIL_SERVER : default 'localhost'
#: MAIL_PORT : default 25
#: MAIL_USE_TLS : default False
#: MAIL_USE_SSL : default False
#: MAIL_USERNAME : default None
#: MAIL_PASSWORD : default None
#: MAIL_DEFAULT_SENDER : default None
MAIL_FAIL_SILENTLY = False
MAIL_SERVER = 'localhost'
MAIL_DEFAULT_SENDER = 'HasGeek <test@example.com>'
DEFAULT_MAIL_SENDER = MAIL_DEFAULT_SENDER  # For compatibility with older Flask-Mail
#: Logging: recipients of error emails
ADMINS = []
#: Log file
LOGFILE = 'error.log'
