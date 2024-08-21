# # Licensed to the Apache Software Foundation (ASF) under one
# # or more contributor license agreements.  See the NOTICE file
# # distributed with this work for additional information
# # regarding copyright ownership.  The ASF licenses this file
# # to you under the Apache License, Version 2.0 (the
# # "License"); you may not use this file except in compliance
# # with the License.  You may obtain a copy of the License at
# #
# #   http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing,
# # software distributed under the License is distributed on an
# # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# # KIND, either express or implied.  See the License for the
# # specific language governing permissions and limitations
# # under the License.
# #
# # This file is included in the final Docker image and SHOULD be overridden when
# # deploying the image to prod. Settings configured here are intended for use in local
# # development environments. Also note that superset_config_docker.py is imported
# # as a final step as a means to override "defaults" configured here
# #
# import logging
# import os
# from datetime import timedelta
# from typing import Optional

# from cachelib.file import FileSystemCache
# from celery.schedules import crontab
# from email.mime.multipart import MIMEMultipart
# from typing import (
#     Any,
#     Callable,
#     Dict,
#     List,
#     Literal,
#     Optional,
#     Set,
#     Type,
#     TYPE_CHECKING,
#     Union,
# )
# from superset import security_manager

# logger = logging.getLogger()

# DATABASE_DIALECT = os.getenv("DATABASE_DIALECT")
# DATABASE_USER = os.getenv("DATABASE_USER")
# DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
# DATABASE_HOST = os.getenv("DATABASE_HOST")
# DATABASE_PORT = os.getenv("DATABASE_PORT")
# DATABASE_DB = os.getenv("DATABASE_DB")

# EXAMPLES_USER = os.getenv("EXAMPLES_USER")
# EXAMPLES_PASSWORD = os.getenv("EXAMPLES_PASSWORD")
# EXAMPLES_HOST = os.getenv("EXAMPLES_HOST")
# EXAMPLES_PORT = os.getenv("EXAMPLES_PORT")
# EXAMPLES_DB = os.getenv("EXAMPLES_DB")

# # The SQLAlchemy connection string.
# SQLALCHEMY_DATABASE_URI = (
#     f"{DATABASE_DIALECT}://"
#     f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
#     f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"
# )

# SQLALCHEMY_EXAMPLES_URI = (
#     f"{DATABASE_DIALECT}://"
#     f"{EXAMPLES_USER}:{EXAMPLES_PASSWORD}@"
#     f"{EXAMPLES_HOST}:{EXAMPLES_PORT}/{EXAMPLES_DB}"
# )

# REDIS_HOST = os.getenv("REDIS_HOST", "redis")
# REDIS_PORT = os.getenv("REDIS_PORT", "6379")
# REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", "0")
# REDIS_RESULTS_DB = os.getenv("REDIS_RESULTS_DB", "1")

# RESULTS_BACKEND = FileSystemCache("/app/superset_home/sqllab")

# CACHE_CONFIG = {
#     "CACHE_TYPE": "RedisCache",
#     "CACHE_DEFAULT_TIMEOUT": 300,
#     "CACHE_KEY_PREFIX": "superset_",
#     "CACHE_REDIS_HOST": REDIS_HOST,
#     "CACHE_REDIS_PORT": REDIS_PORT,
#     "CACHE_REDIS_DB": REDIS_RESULTS_DB,
# }
# DATA_CACHE_CONFIG = CACHE_CONFIG
# #-------MyChanges---------------------------------------------------------------------------
# class CeleryConfig:
#     BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
#     CELERY_IMPORTS = ("superset.sql_lab","superset.tasks","superset.tasks.thumbnails")
#     CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
#     CELERYD_LOG_LEVEL = "DEBUG"
#     # CELERYD_PREFETCH_MULTIPLIER = 1
#     # CELERY_ACKS_LATE = False
#     CELERYD_PREFETCH_MULTIPLIER = 10
#     CELERY_ACKS_LATE = True
#     CELERY_ANNOTATIONS = {
#         'sql_lab.get_sql_results': {
#             'rate_limit': '100/s',
#         },
#         'email_reports.send': {
#             'rate_limit': '1/s',
#             'time_limit': 1800,
#             'soft_time_limit': 1800,
#             'ignore_result': False,
#         },
#     }
#     CELERYBEAT_SCHEDULE = {
#         "email_reports.schedule_hourly": {
#             "task": "email_reports.schedule_hourly",
#             "schedule": crontab(minute=1, hour="*"),
#         },
#         "reports.scheduler": {
#             "task": "reports.scheduler",
#             "schedule": crontab(minute="*", hour="*"),
#         },
#         "reports.prune_log": {
#             "task": "reports.prune_log",
#             "schedule": crontab(minute=10, hour=0),
#         },
#         "alerts.schedule_check": {
#             "task": "alerts.schedule_check",
#             "schedule": crontab(minute="*", hour="*"),
#         },
#         #	"cache-warmup-hourly": {
#         #           "task": "cache-warmup",
#         #           "schedule": crontab(minute="*/30", hour="*"),
#         #           "kwargs": {
#         #            	"strategy_name": "top_n_dashboards",
#         #            	"top_n": 10,
#         #            	"since": "7 days ago"
#         #            }
#         #        }
#     }

# CELERY_CONFIG = CeleryConfig
# SQLLAB_CTAS_NO_LIMIT = True
# # ------------------------------------------------------------------edits

# #Is chaching  for 1 day is it good idea think again about it

# FILTER_STATE_CACHE_CONFIG = {
#     'CACHE_TYPE': 'RedisCache',
#     'CACHE_DEFAULT_TIMEOUT': 86400,
#     'CACHE_KEY_PREFIX': 'superset_filter_',
#     'CACHE_REDIS_URL': 'redis://localhost:6379/2'
# }

# DATA_CACHE_CONFIG = {
#     'CACHE_TYPE': 'RedisCache',
#     'CACHE_DEFAULT_TIMEOUT': 80000,
#     'CACHE_KEY_PREFIX': 'superset_data_',
#     'CACHE_REDIS_URL': 'redis://redis:6379/3'
# }

# FILTER_STATE_CACHE_CONFIG = {
#     'CACHE_TYPE': 'RedisCache',
#     'CACHE_DEFAULT_TIMEOUT': int(timedelta(days=1).total_seconds()),
#     'CACHE_KEY_PREFIX': 'superset_filter_',
#     'CACHE_REDIS_URL': 'redis://redis:6379/4'
# }

# EXPLORE_FORM_DATA_CACHE_CONFIG = {
#     'CACHE_TYPE': 'RedisCache',
#     'CACHE_DEFAULT_TIMEOUT': int(timedelta(days=1).total_seconds()),
#     'CACHE_KEY_PREFIX': 'superset_explore_',
#     'CACHE_REDIS_URL': 'redis://redis:6379/5'
# }

# #-------------------------------------------------------------------------------
# #Ldap configurations

# # from flask_appbuilder.security.manager import AUTH_LDAP

# # AUTH_TYPE = AUTH_LDAP
# # AUTH_ROLE_ADMIN = 'Admin'
# # AUTH_USER_REGISTRATION = True
# # AUTH_LDAP_SERVER = "ldap://172.20.20.8:389/"
# # AUTH_LDAP_SEARCH= "dc=hotwax,dc=io"
# # AUTH_LDAP_UID_FIELD="cn"
# # AUTH_LDAP_FIRSTNAME_FIELD= "admin"
# # AUTH_LDAP_LASTTNAME_FIELD= "sn"
# # AUTH_LDAP_USE_TLS = False

# # AUTH_LDAP_BIND_USER = "cn=admin,dc=hotwax,dc=io"
# # AUTH_LDAP_BIND_PASSWORD = "Ht5@nadm!n"
# #---------------------------------------------------------

# # Visual Customizations
# APP_NAME = "Hotwax"
# APP_ICON = "/static/assets/images/hotwax.png"
# APP_ICON_WIDTH = 300
# # Path for routing when APP_ICON image is clicked
# LOGO_TARGET_PATH = '/' # Forwards to /superset/welcome/home
# LOGO_TOOLTIP = "Go Home" # Text displayed when hovering.
# FAVICONS = [{"href": "/static/assets/images/hotwax.png"}]

# #------------------------------------------------------------------------------------------------------------------------------------------
# #For Avoiding Overflow of sqlAlchemy_pool
# SQLALCHEMY_POOL_SIZE = 100

# SQLALCHEMY_MAX_OVERFLOW = 80

# SQLALCHEMY_POOL_TIMEOUT = 180

# #------------------------------------------------------------------------
# EMAIL_NOTIFICATIONS = True

# # SMTP_HOST = "172.20.20.21"
# # #SMTP_HOST = "172.31.5.109"
# # SMTP_STARTTLS = False
# # SMTP_SSL = False
# # SMTP_USER = ""
# # SMTP_PORT = 25
# # SMTP_PASSWORD = ""
# # SMTP_MAIL_FROM = "noreply@hotwaxsystems.com"

# SMTP_HOST = "smtp.gmail.com"
# SMTP_USER = "rohitpawar28112000@gmail.com"
# SMTP_PASSWORD = "dyalijcrjcfmjgjw"
# SMTP_STARTTLS = True
# SMTP_SSL = False
# #SMTP_PORT = 465
# SMTP_PORT = 587
# SMTP_MAIL_FROM = "rohitpawar28112000@gmail.com"


# FEATURE_FLAGS = {
#     "DYNAMIC_PLUGINS": True,
#     "ENABLE_TEMPLATE_PROCESSING": True,
#     "VERSIONED_EXPORT": True,
#     "ALERT_REPORTS": True,
#     "DASHBOARD_RBAC": False,
#     "GLOBAL_ASYNC_QUERIES": False,
#     "TAGGING_SYSTEM": True,
#     "EMBEDDED_SUPERSET": True,
#     "EMBEDDABLE_CHARTS": True
# }

# ALERT_REPORTS_NOTIFICATION_DRY_RUN = False
# SCREENSHOT_LOCATE_WAIT = 1000
# SCREENSHOT_LOAD_WAIT = 1600
# ENABLE_ALERTS = True

# ENABLE_SCHEDULED_EMAIL_REPORTS = True

# # WEBDRIVER_BASEURL = "http://tathya-uat.hotwax.io"
# WEBDRIVER_BASEURL = "http://localhost:8088"
# # # The base URL for the email report hyperlinks.
# #WEBDRIVER_BASEURL_USER_FRIENDLY = "http://localhost:8088"

# #WEBDRIVER_BASEURL = "http://superset:8088/"
# # The base URL for the email report hyperlinks.
# WEBDRIVER_BASEURL_USER_FRIENDLY = WEBDRIVER_BASEURL

# #--------------------------------------------------------------------------
# ALERT_REPORTS_WORKING_TIME_OUT_KILL = True
# ALERT_REPORTS_WORKING_TIME_OUT_LAG = int(timedelta(seconds=1600).total_seconds())
# ALERT_REPORTS_WORKING_SOFT_TIME_OUT_LAG = int(timedelta(seconds=1600).total_seconds())
# ALERT_REPORTS_QUERY_EXECUTION_MAX_TRIES = 3

# # Time selenium will wait for the page to load and render for the email report.
# EMAIL_PAGE_RENDER_WAIT = int(timedelta(seconds=1600).total_seconds())

# THUMBNAIL_SELENIUM_USER = "admin"
# SQLLAB_TIMEOUT = int(timedelta(minutes=30).total_seconds())
# SUPERSET_WEBSERVER_TIMEOUT = int(timedelta(minutes=30).total_seconds())
# SQLLAB_CTAS_NO_LIMIT = True

# # When adding a new database we try to connect to it. Depending on which parameters are
# # incorrect this could take a couple minutes, until the SQLAlchemy driver pinging the
# # database times out. Instead of relying on the driver timeout we can specify a shorter
# # one here.
# TEST_DATABASE_CONNECTION_TIMEOUT = timedelta(seconds=1600)
# #-----------------------------------------------------------------------------------------------------------------

# GLOBAL_ASYNC_QUERIES_REDIS_CONFIG = {
#     "port": REDIS_PORT,
#     "host": REDIS_HOST,
#     "password": "",
#     "db": 6,
#     "ssl": False,
# }
# GLOBAL_ASYNC_QUERIES_REDIS_STREAM_PREFIX = "async-events-"
# GLOBAL_ASYNC_QUERIES_REDIS_STREAM_LIMIT = 1000
# GLOBAL_ASYNC_QUERIES_REDIS_STREAM_LIMIT_FIREHOSE = 1000000
# GLOBAL_ASYNC_QUERIES_JWT_COOKIE_NAME = "async-token"
# GLOBAL_ASYNC_QUERIES_JWT_COOKIE_SECURE = False
# GLOBAL_ASYNC_QUERIES_JWT_COOKIE_DOMAIN = None
# #GLOBAL_ASYNC_QUERIES_JWT_SECRET = "test-secret-change-me"
# GLOBAL_ASYNC_QUERIES_TRANSPORT = "polling"
# GLOBAL_ASYNC_QUERIES_POLLING_DELAY = int(
#      timedelta(milliseconds=500).total_seconds() * 1000
# )
# GLOBAL_ASYNC_QUERIES_WEBSOCKET_URL = "ws://127.0.0.1:8080/"

# GLOBAL_ASYNC_QUERIES_JWT_SECRET = 'v2jHEh8gG2yw56ReLEvGwGTSgETRu26U'

# #---------------------------------------------------------------------------------------------------------

# SSL_CERT_PATH = "file:///home//rohit.pawar//certs-mysql-client"
# #---------------------------------------------------------
# #jan-30-permission-related-test
# #Just Nothing extra meta data provides here
# FAB_ADD_SECURITY_VIEWS = True
# FAB_ADD_SECURITY_PERMISSION_VIEW = True
# FAB_ADD_SECURITY_VIEW_MENU_VIEW = True
# FAB_ADD_SECURITY_PERMISSION_VIEWS_VIEW = True

# #-------------------------------------------------------------------------------------------------------
# def EMAIL_HEADER_MUTATOR(
#     msg: MIMEMultipart, **kwargs: Any
# ) -> MIMEMultipart:
#     subject = msg["Subject"].split(":")[0].strip()
#     print("Email Subject %s", subject)
#     if subject != "Error occurred for Report":
#         msg.replace_header("Subject", msg["Subject"].split(":")[0])
# #        print("===============new one=========================that my msg in emailrohit %s %s " % (msg["Subject"], msg))
#     return msg
# #---------------------------------------------------------------------------------------------------------
# EMAIL_REPORTS_SUBJECT_PREFIX = ""
# EMAIL_REPORTS_CTA = "Explore in Hotwax-Commerce BA"

# # Slack API Token
# SLACK_API_TOKEN = "xoxb-5375163807412-5369861877973-QLXJvtbQQ7uXFykDxUgR8NY2"

# PREVIOUS_SECRET_KEY = "CHANGE_ME_TO_A_COMPLEX_RANDOM_SECRET"
# SECRET_KEY = "4MLdqTj6eX2FUMqlO3haXnez6D776JKxP59RcE2/vFTS4I8ejw/YHTWz"

# #----------------------------------------------------------------------------------------------------------
# def EXCLUDE_USERS_FROM_FUNC() -> bool:
#     if security_manager.can_access_all_datasources() :
#         return False
#     else :
#         return True
# # ----------------------------------------------------
# # EMAIL_REPORTS_BLANK = False
# #By default its true because previous users are using this
# CSV_INDEX = False

# # ------------------------------------------------------
# WTF_CSRF_ENABLED = False
# TALISMAN_ENABLED = False
# #SESSION_COOKIE_SAMESITE = None
# #SESSION_COOKIE_SECURE = False
# #SESSION_COOKIE_HTTPONLY = False
# #------------------------------------------------------
# # default row limit when requesting chart data
# # It is not affecting the values on UI
# ROW_LIMIT = 100000
# # default row limit when requesting samples from datasource in explore view
# SAMPLES_ROW_LIMIT = 100000
# #------------------------------------------------------
# # Maximum number of rows returned for any analytical database query 10Lakh
# SQL_MAX_ROW = 100000
# #-----------------------------------------------------------------------------
# # Changes right now
# # Embedded config options
# GUEST_ROLE_NAME = "embedded"
# # GUEST_ROLE_NAME = "Embedded"
# GUEST_TOKEN_JWT_SECRET = "4MLdqTj6eX2FUMqlO3haXnez6D776JKxP59RcE2/vFTS4I8ejw/YHTWz"
# GUEST_TOKEN_JWT_ALGO = "HS256"
# GUEST_TOKEN_HEADER_NAME = "X-GuestToken"
# GUEST_TOKEN_JWT_EXP_SECONDS = 18000  # 5 minutes
# # Guest token audience for the embedded superset, either string or callable
# # GUEST_TOKEN_JWT_AUDIENCE: Callable[[], str] | str | None = None

# SESSION_COOKIE_SAMESITE = None
# ENABLE_PROXY_FIX = False
# PUBLIC_ROLE_LIKE_GAMMA = True

# #CORS_OPTIONS = {
# #    'supports_credentials': True,
# #    'allow_headers': ['*'],
# #    'resources':['*'],
# #    'origins': ['http://tathya-uat.hotwax.io','http://tathya-uat.hotwax.io:8088','http://tathya-uat.hotwax.io:3000','http://tathya-uat.hotwax.io:8888','http://tathya-uat.hotwax.io']
# #}

# ENABLE_CORS = True
# CORS_OPTIONS = {
#     'supports_credentials': True,
#     'allow_headers': ['*'],
#     'resources': ['*'],
#     'origins': [
#         '*',
#         'http://tathya-uat.hotwax.io',
#         'http://tathya-uat.hotwax.io:8088',
#         'http://tathya-uat.hotwax.io:3000',
#         'http://tathya-uat.hotwax.io:8888',
#         'http://localhost:3000'  # Add localhost origin here
#     ]
# }
# #-----------------------------------------------------------------
# # we are enabling the logs dumping in superset.log, 1day file  rollover and 30 files should be retained
# ENABLE_TIME_ROTATE = True
# TIME_ROTATE_LOG_LEVEL = "INFO"
# FILENAME = os.path.join("/app/superset_home/logs", "superset.log")
# ROLLOVER = "midnight"
# INTERVAL = 1
# BACKUP_COUNT = 15

# #--------------------------------------------------------------------------
# #Enabling Talisman for CSP
# TALISMAN_ENABLED = True
# TALISMAN_CONFIG = {
#     "force_https": False,
#     "content_security_policy": {
#         "default-src": ["'self'", "'unsafe-inline'", "'unsafe-eval'"],
#         "img-src": ["'self'", "data:"],
#         "worker-src": ["'self'", "blob:"],
#         "connect-src": ["'self'", "https://api.mapbox.com", "https://events.mapbox.com"],
#         "object-src": "'none'",
#     }
# }

# #--------------------------------------------------------------------------






# # Optionally import superset_config_docker.py (which will have been included on
# # the PYTHONPATH) in order to allow for local settings to be overridden
# #
# try:
#     import superset_config_docker
#     from superset_config_docker import *  # noqa

#     logger.info(
#         f"Loaded your Docker configuration at " f"[{superset_config_docker.__file__}]"
#     )
# except ImportError:
#     logger.info("Using default Docker config...")
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# This file is included in the final Docker image and SHOULD be overridden when
# deploying the image to prod. Settings configured here are intended for use in local
# development environments. Also note that superset_config_docker.py is imported
# as a final step as a means to override "defaults" configured here
#
import logging
import os
from datetime import timedelta
from typing import Optional

from cachelib.file import FileSystemCache
from celery.schedules import crontab
from email.mime.multipart import MIMEMultipart
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Set,
    Type,
    TYPE_CHECKING,
    Union,
)
from superset import security_manager

logger = logging.getLogger()

DATABASE_DIALECT = os.getenv("DATABASE_DIALECT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_DB = os.getenv("DATABASE_DB")

EXAMPLES_USER = os.getenv("EXAMPLES_USER")
EXAMPLES_PASSWORD = os.getenv("EXAMPLES_PASSWORD")
EXAMPLES_HOST = os.getenv("EXAMPLES_HOST")
EXAMPLES_PORT = os.getenv("EXAMPLES_PORT")
EXAMPLES_DB = os.getenv("EXAMPLES_DB")

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = (
    f"{DATABASE_DIALECT}://"
    f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
    f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"
)

SQLALCHEMY_EXAMPLES_URI = (
    f"{DATABASE_DIALECT}://"
    f"{EXAMPLES_USER}:{EXAMPLES_PASSWORD}@"
    f"{EXAMPLES_HOST}:{EXAMPLES_PORT}/{EXAMPLES_DB}"
)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", "0")
REDIS_RESULTS_DB = os.getenv("REDIS_RESULTS_DB", "1")


# Not recommended for production
# RESULTS_BACKEND = FileSystemCache("/app/superset_home/sqllab")

from flask_caching.backends.rediscache import RedisCache
RESULTS_BACKEND = RedisCache(
    host=REDIS_HOST, port=REDIS_PORT, key_prefix='superset_results')

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": REDIS_PORT,
    "CACHE_REDIS_DB": REDIS_RESULTS_DB,
}
DATA_CACHE_CONFIG = CACHE_CONFIG

#-------Celery-Changes---------------------------------------------------------------------------

class CeleryConfig:
    BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
    CELERY_IMPORTS = ("superset.sql_lab","superset.tasks","superset.tasks.thumbnails")
    CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
    CELERYD_LOG_LEVEL = "DEBUG"
    # CELERYD_PREFETCH_MULTIPLIER = 1
    # CELERY_ACKS_LATE = False
    CELERYD_PREFETCH_MULTIPLIER = 10
    CELERY_ACKS_LATE = True
    CELERY_ANNOTATIONS = {
        'sql_lab.get_sql_results': {
            'rate_limit': '100/s',
        },
        'email_reports.send': {
            'rate_limit': '1/s',
            'time_limit': 1800,
            'soft_time_limit': 1800,
            'ignore_result': False,
        },
    }
    CELERYBEAT_SCHEDULE = {
        "email_reports.schedule_hourly": {
            "task": "email_reports.schedule_hourly",
            "schedule": crontab(minute=1, hour="*"),
        },
        "reports.scheduler": {
            "task": "reports.scheduler",
            "schedule": crontab(minute="*", hour="*"),
        },
        "reports.prune_log": {
            "task": "reports.prune_log",
            "schedule": crontab(minute=10, hour=0),
        },
        "alerts.schedule_check": {
            "task": "alerts.schedule_check",
            "schedule": crontab(minute="*", hour="*"),
        },
        #	"cache-warmup-hourly": {
        #           "task": "cache-warmup",
        #           "schedule": crontab(minute="*/30", hour="*"),
        #           "kwargs": {
        #            	"strategy_name": "top_n_dashboards",
        #            	"top_n": 10,
        #            	"since": "7 days ago"
        #            }
        #        }
    }

CELERY_CONFIG = CeleryConfig
SQLLAB_CTAS_NO_LIMIT = True
# ------------------------------------------------------------------edits

#Is Caching  for 1 day is it good idea think again about it

DATA_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 80000,
    'CACHE_KEY_PREFIX': 'superset_data_',
    'CACHE_REDIS_URL': 'redis://redis:6379/3'
}

FILTER_STATE_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': int(timedelta(days=1).total_seconds()),
    'CACHE_KEY_PREFIX': 'superset_filter_',
    'CACHE_REDIS_URL': 'redis://redis:6379/4'
}

EXPLORE_FORM_DATA_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': int(timedelta(days=1).total_seconds()),
    'CACHE_KEY_PREFIX': 'superset_explore_',
    'CACHE_REDIS_URL': 'redis://redis:6379/5'
}

#-------------------------------------------------------------------------------
#Ldap configurations

from flask_appbuilder.security.manager import AUTH_LDAP

AUTH_TYPE = AUTH_LDAP
AUTH_ROLE_ADMIN = 'Admin'
AUTH_USER_REGISTRATION = True
AUTH_LDAP_SERVER = "ldap://172.20.20.8:389/"
AUTH_LDAP_SEARCH= "dc=hotwax,dc=io"
AUTH_LDAP_UID_FIELD="cn"
AUTH_LDAP_FIRSTNAME_FIELD= "admin"
AUTH_LDAP_LASTTNAME_FIELD= "sn"
AUTH_LDAP_USE_TLS = False

AUTH_LDAP_BIND_USER = "cn=admin,dc=hotwax,dc=io"
AUTH_LDAP_BIND_PASSWORD = "Ht5@nadm!n"
#---------------------------------------------------------

# Visual Customizations
APP_NAME = "Hotwax"
APP_ICON = "/static/assets/images/hotwax.png"
APP_ICON_WIDTH = 300
# Path for routing when APP_ICON image is clicked
LOGO_TARGET_PATH = '/' # Forwards to /superset/welcome/home
LOGO_TOOLTIP = "Go Home" # Text displayed when hovering.
FAVICONS = [{"href": "/static/assets/images/hotwax.png"}]

#------------------------------------------------------------------------------------------------------------------------------------------
#For Avoiding Overflow of sqlAlchemy_pool
SQLALCHEMY_POOL_SIZE = 100

SQLALCHEMY_MAX_OVERFLOW = 80

SQLALCHEMY_POOL_TIMEOUT = 180

#------------------------------------------------------------------------
EMAIL_NOTIFICATIONS = True

SMTP_HOST = "172.20.20.21"
#SMTP_HOST = "172.31.5.109"
SMTP_STARTTLS = False
SMTP_SSL = False
SMTP_USER = ""
SMTP_PORT = 25
SMTP_PASSWORD = ""
SMTP_MAIL_FROM = "noreply@hotwaxsystems.com"

FEATURE_FLAGS = {
    "DYNAMIC_PLUGINS": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "VERSIONED_EXPORT": True,
    "ALERT_REPORTS": True,
    "DASHBOARD_RBAC": False,
    "GLOBAL_ASYNC_QUERIES": False,
    "ALLOW_FULL_CSV_EXPORT" : False,
    "TAGGING_SYSTEM": True,
    "EMBEDDED_SUPERSET": True,
    "EMBEDDABLE_CHARTS": True
}

ALERT_REPORTS_NOTIFICATION_DRY_RUN = False
SCREENSHOT_LOCATE_WAIT = 1000
SCREENSHOT_LOAD_WAIT = 1600
ENABLE_ALERTS = True

ENABLE_SCHEDULED_EMAIL_REPORTS = True

WEBDRIVER_BASEURL = "http://tathya-uat.hotwax.io"
#WEBDRIVER_BASEURL = "http://superset:8088/"
# The base URL for the email report hyperlinks.
WEBDRIVER_BASEURL_USER_FRIENDLY = WEBDRIVER_BASEURL

#-------------------------------------------------------------------------------------------------------------
ALERT_REPORTS_WORKING_TIME_OUT_KILL = True
ALERT_REPORTS_WORKING_TIME_OUT_LAG = int(timedelta(seconds=1600).total_seconds())
ALERT_REPORTS_WORKING_SOFT_TIME_OUT_LAG = int(timedelta(seconds=1600).total_seconds())
ALERT_REPORTS_QUERY_EXECUTION_MAX_TRIES = 3

# Time selenium will wait for the page to load and render for the email report.
EMAIL_PAGE_RENDER_WAIT = int(timedelta(seconds=1600).total_seconds())
#--------------------------------------------------------------------------------------------------------------
# This Changes Ensure that ALERT_REPORTS scheduled run via selinum user superset
from superset.tasks.types import ExecutorType
THUMBNAIL_SELENIUM_USER = "superset"
THUMBNAIL_EXECUTE_AS = [ExecutorType.SELENIUM]
ALERT_REPORTS_EXECUTE_AS = [ExecutorType.SELENIUM]
#--------------------------------------------------------------------------------------------------------------
SQLLAB_TIMEOUT = int(timedelta(minutes=30).total_seconds())
SUPERSET_WEBSERVER_TIMEOUT = int(timedelta(minutes=30).total_seconds())
SQLLAB_CTAS_NO_LIMIT = True

# When adding a new database we try to connect to it. Depending on which parameters are
# incorrect this could take a couple minutes, until the SQLAlchemy driver pinging the
# database times out. Instead of relying on the driver timeout we can specify a shorter
# one here.
TEST_DATABASE_CONNECTION_TIMEOUT = timedelta(seconds=1600)
#-----------------------------------------------------------------------------------------------------------------

GLOBAL_ASYNC_QUERIES_REDIS_CONFIG = {
    "port": REDIS_PORT,
    "host": REDIS_HOST,
    "password": "",
    "db": 6,
    "ssl": False,
}
GLOBAL_ASYNC_QUERIES_REDIS_STREAM_PREFIX = "async-events-"
GLOBAL_ASYNC_QUERIES_REDIS_STREAM_LIMIT = 1000
GLOBAL_ASYNC_QUERIES_REDIS_STREAM_LIMIT_FIREHOSE = 1000000
GLOBAL_ASYNC_QUERIES_JWT_COOKIE_NAME = "async-token"
GLOBAL_ASYNC_QUERIES_JWT_COOKIE_SECURE = False
GLOBAL_ASYNC_QUERIES_JWT_COOKIE_DOMAIN = None
#GLOBAL_ASYNC_QUERIES_JWT_SECRET = "test-secret-change-me"
GLOBAL_ASYNC_QUERIES_TRANSPORT = "polling"
GLOBAL_ASYNC_QUERIES_POLLING_DELAY = int(
     timedelta(milliseconds=500).total_seconds() * 1000
)
GLOBAL_ASYNC_QUERIES_WEBSOCKET_URL = "ws://127.0.0.1:8080/"

GLOBAL_ASYNC_QUERIES_JWT_SECRET = 'v2jHEh8gG2yw56ReLEvGwGTSgETRu26U'

#---------------------------------------------------------------------------------------------------------
SSL_CERT_PATH = "file:///home//rohit.pawar//certs-mysql-client"
#---------------------------------------------------------------------------------------------------------
#Just Nothing extra meta data provides here
FAB_ADD_SECURITY_VIEWS = True
FAB_ADD_SECURITY_PERMISSION_VIEW = True
FAB_ADD_SECURITY_VIEW_MENU_VIEW = True
FAB_ADD_SECURITY_PERMISSION_VIEWS_VIEW = True

#-------------------------------------------------------------------------------------------------------
def EMAIL_HEADER_MUTATOR(
    msg: MIMEMultipart, **kwargs: Any
) -> MIMEMultipart:
    subject = msg["Subject"].split(":")[0].strip()
    print("Email Subject %s", subject)
    if subject != "Error occurred for Report":
        msg.replace_header("Subject", msg["Subject"].split(":")[0])
    return msg
#---------------------------------------------------------------------------------------------------------
EMAIL_REPORTS_SUBJECT_PREFIX = ""
EMAIL_REPORTS_CTA = "Explore in Hotwax-Commerce BA"

# Slack API Token
SLACK_API_TOKEN = "xoxb-5375163807412-5369861877973-QLXJvtbQQ7uXFykDxUgR8NY2"

PREVIOUS_SECRET_KEY = "CHANGE_ME_TO_A_COMPLEX_RANDOM_SECRET"
SECRET_KEY = "4MLdqTj6eX2FUMqlO3haXnez6D776JKxP59RcE2/vFTS4I8ejw/YHTWz"

#----------------------------------------------------------------------------------------------------------
# By using this filter only Admin or who can access all datasource access can view all users
# Similarly, to restrict the roles in the "Roles" dropdown you can provide a custom
# filter callback for the "role" key.

from sqlalchemy.orm.query import Query
from sqlalchemy import and_, or_

def user_filter(query: Query, *args, **kwargs):
    user_model = security_manager.user_model
    if not security_manager.can_access_all_datasources():
        return query.filter(and_(user_model.username.ilike(str(user_model.username))))
    else:
        return query.filter(and_(user_model.username.not_in([])))

EXTRA_RELATED_QUERY_FILTERS = {"user": user_filter}

# ----------------------------------------------------
# EMAIL_REPORTS_BLANK = False
#By default its true because previous users are using this
CSV_INDEX = False

# ------------------------------------------------------
WTF_CSRF_ENABLED = False
SESSION_COOKIE_SAMESITE = None
#SESSION_COOKIE_SECURE = False
#SESSION_COOKIE_HTTPONLY = False
#--------------------------------------------------------------------------------
# default row limit when requesting chart data
# It is not affecting the values on UI
ROW_LIMIT = 100000
# default row limit when requesting samples from datasource in explore view
SAMPLES_ROW_LIMIT = 100000
#---------------------------------------------------------------------------------
# Maximum number of rows returned for any analytical database query 10Lakh
SQL_MAX_ROW = 100000
#---------------------------------------------------------------------------------
# Embedded config options
GUEST_ROLE_NAME = "embedded"
# GUEST_ROLE_NAME = "Embedded"
GUEST_TOKEN_JWT_SECRET = "4MLdqTj6eX2FUMqlO3haXnez6D776JKxP59RcE2/vFTS4I8ejw/YHTWz"
GUEST_TOKEN_JWT_ALGO = "HS256"
GUEST_TOKEN_HEADER_NAME = "X-GuestToken"
GUEST_TOKEN_JWT_EXP_SECONDS = 18000  # 5 minutes
# Guest token audience for the embedded superset, either string or callable
# GUEST_TOKEN_JWT_AUDIENCE: Callable[[], str] | str | None = None
#----------------------------------------------------------------------------------
ENABLE_PROXY_FIX = False
PUBLIC_ROLE_LIKE_GAMMA = True

ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources': ['*'],
    'origins': [
        '*',
        'http://tathya-uat.hotwax.io',
        'http://tathya-uat.hotwax.io:8088',
        'http://tathya-uat.hotwax.io:3000',
        'http://tathya-uat.hotwax.io:8888',
        'http://localhost:3000'  # Add localhost origin here
    ]
}
#-----------------------------------------------------------------
# We are enabling the logs dumping in superset.log, 1day file  rollover and 30 files should be retained
ENABLE_TIME_ROTATE = True
TIME_ROTATE_LOG_LEVEL = "INFO"
FILENAME = os.path.join("/app/superset_home/logs", "superset.log")
ROLLOVER = "midnight"
INTERVAL = 1
BACKUP_COUNT = 20

#--------------------------------------------------------------------------
#Enabling Talisman for CSP
TALISMAN_ENABLED = True
TALISMAN_CONFIG = {
    "force_https": False,
    "content_security_policy": {
        "default-src": ["'self'", "'unsafe-inline'", "'unsafe-eval'"],
        "img-src": ["'self'", "data:"],
        "worker-src": ["'self'", "blob:"],
        "connect-src": ["'self'", "https://api.mapbox.com", "https://events.mapbox.com"],
        "object-src": "'none'",
    }
}

#--------------------------------------------------------------------------


# Optionally import superset_config_docker.py (which will have been included on
# the PYTHONPATH) in order to allow for local settings to be overridden
#
try:
    import superset_config_docker
    from superset_config_docker import *  # noqa

    logger.info(
        f"Loaded your Docker configuration at " f"[{superset_config_docker.__file__}]"
    )
except ImportError:
    logger.info("Using default Docker config...")



# Prod Superset Configurations

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# This file is included in the final Docker image and SHOULD be overridden when
# deploying the image to prod. Settings configured here are intended for use in local
# development environments. Also note that superset_config_docker.py is imported
# as a final step as a means to override "defaults" configured here
#
import logging
import os
from datetime import timedelta
from typing import Optional

from cachelib.file import FileSystemCache
from celery.schedules import crontab
from email.mime.multipart import MIMEMultipart
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Literal,
    Optional,
    Set,
    Type,
    TYPE_CHECKING,
    Union,
)
from superset import security_manager

logger = logging.getLogger()

DATABASE_DIALECT = os.getenv("DATABASE_DIALECT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_DB = os.getenv("DATABASE_DB")

EXAMPLES_USER = os.getenv("EXAMPLES_USER")
EXAMPLES_PASSWORD = os.getenv("EXAMPLES_PASSWORD")
EXAMPLES_HOST = os.getenv("EXAMPLES_HOST")
EXAMPLES_PORT = os.getenv("EXAMPLES_PORT")
EXAMPLES_DB = os.getenv("EXAMPLES_DB")

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = (
    f"{DATABASE_DIALECT}://"
    f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
    f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"
)

SQLALCHEMY_EXAMPLES_URI = (
    f"{DATABASE_DIALECT}://"
    f"{EXAMPLES_USER}:{EXAMPLES_PASSWORD}@"
    f"{EXAMPLES_HOST}:{EXAMPLES_PORT}/{EXAMPLES_DB}"
)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = os.getenv("REDIS_PORT", "6379")
REDIS_CELERY_DB = os.getenv("REDIS_CELERY_DB", "0")
REDIS_RESULTS_DB = os.getenv("REDIS_RESULTS_DB", "1")


# Not recommended for production
# RESULTS_BACKEND = FileSystemCache("/app/superset_home/sqllab")

from flask_caching.backends.rediscache import RedisCache
RESULTS_BACKEND = RedisCache(
    host=REDIS_HOST, port=REDIS_PORT, key_prefix='superset_results')

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": REDIS_HOST,
    "CACHE_REDIS_PORT": REDIS_PORT,
    "CACHE_REDIS_DB": REDIS_RESULTS_DB,
}
DATA_CACHE_CONFIG = CACHE_CONFIG

#-------Celery-Changes---------------------------------------------------------------------------

class CeleryConfig:
    BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
    CELERY_IMPORTS = ("superset.sql_lab","superset.tasks","superset.tasks.thumbnails")
    CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
    CELERYD_LOG_LEVEL = "DEBUG"
    # CELERYD_PREFETCH_MULTIPLIER = 1
    # CELERY_ACKS_LATE = False
    CELERYD_PREFETCH_MULTIPLIER = 10
    CELERY_ACKS_LATE = True
    CELERY_ANNOTATIONS = {
        'sql_lab.get_sql_results': {
            'rate_limit': '100/s',
        },
        'email_reports.send': {
            'rate_limit': '1/s',
            'time_limit': 1800,
            'soft_time_limit': 1800,
            'ignore_result': False,
        },
    }
    CELERYBEAT_SCHEDULE = {
        "email_reports.schedule_hourly": {
            "task": "email_reports.schedule_hourly",
            "schedule": crontab(minute=1, hour="*"),
        },
        "reports.scheduler": {
            "task": "reports.scheduler",
            "schedule": crontab(minute="*", hour="*"),
        },
        "reports.prune_log": {
            "task": "reports.prune_log",
            "schedule": crontab(minute=10, hour=0),
        },
        "alerts.schedule_check": {
            "task": "alerts.schedule_check",
            "schedule": crontab(minute="*", hour="*"),
        },
        #	"cache-warmup-hourly": {
        #           "task": "cache-warmup",
        #           "schedule": crontab(minute="*/30", hour="*"),
        #           "kwargs": {
        #            	"strategy_name": "top_n_dashboards",
        #            	"top_n": 10,
        #            	"since": "7 days ago"
        #            }
        #        }
    }

CELERY_CONFIG = CeleryConfig
SQLLAB_CTAS_NO_LIMIT = True
# ------------------------------------------------------------------edits

#Is Caching  for 1 day is it good idea think again about it

DATA_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 80000,
    'CACHE_KEY_PREFIX': 'superset_data_',
    'CACHE_REDIS_URL': 'redis://redis:6379/3'
}

FILTER_STATE_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': int(timedelta(days=1).total_seconds()),
    'CACHE_KEY_PREFIX': 'superset_filter_',
    'CACHE_REDIS_URL': 'redis://redis:6379/4'
}

EXPLORE_FORM_DATA_CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': int(timedelta(days=1).total_seconds()),
    'CACHE_KEY_PREFIX': 'superset_explore_',
    'CACHE_REDIS_URL': 'redis://redis:6379/5'
}

#-------------------------------------------------------------------------------
#Ldap configurations

from flask_appbuilder.security.manager import AUTH_LDAP

AUTH_TYPE = AUTH_LDAP
AUTH_ROLE_ADMIN = 'Admin'
AUTH_USER_REGISTRATION = True
AUTH_LDAP_SERVER = "ldap://ldap.hotwax.io/389"
AUTH_LDAP_SEARCH= "dc=hotwax,dc=io"
AUTH_LDAP_UID_FIELD="cn"
AUTH_LDAP_FIRSTNAME_FIELD= "admin"
#AUTH_LDAP_LASTTNAME_FIELD= "sn"
AUTH_LDAP_USE_TLS = False

AUTH_LDAP_BIND_USER = "cn=admin,dc=hotwax,dc=io"
AUTH_LDAP_BIND_PASSWORD = "Ht5@nadm!n"
#---------------------------------------------------------

# Visual Customizations
APP_NAME = "Hotwax"
APP_ICON = "/static/assets/images/hotwax.png"
APP_ICON_WIDTH = 250
# Path for routing when APP_ICON image is clicked
LOGO_TARGET_PATH = '/' # Forwards to /superset/welcome/home
LOGO_TOOLTIP = "Go Home" # Text displayed when hovering.
FAVICONS = [{"href": "/static/assets/images/hotwax.png"}]

#------------------------------------------------------------------------------------------------------------------------------------------
#For Avoiding Overflow of sqlAlchemy_pool
SQLALCHEMY_POOL_SIZE = 100

SQLALCHEMY_MAX_OVERFLOW = 80

SQLALCHEMY_POOL_TIMEOUT = 180

#------------------------------------------------------------------------
EMAIL_NOTIFICATIONS = True

SMTP_HOST = "172.31.5.109"
SMTP_USER = ""
SMTP_PASSWORD = ""
SMTP_STARTTLS = False
SMTP_SSL = False
#SMTP_PORT = 465
SMTP_PORT = 25
SMTP_MAIL_FROM = "no-reply@hotwax.co"

FEATURE_FLAGS = {
    "DYNAMIC_PLUGINS": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "VERSIONED_EXPORT": True,
    "ALERT_REPORTS": True,
    "DASHBOARD_RBAC": False,
    "GLOBAL_ASYNC_QUERIES": False,
    "ALLOW_FULL_CSV_EXPORT" : False,
    "TAGGING_SYSTEM": True,
    "EMBEDDED_SUPERSET": True,
    "EMBEDDABLE_CHARTS": True
}

ALERT_REPORTS_NOTIFICATION_DRY_RUN = False
SCREENSHOT_LOCATE_WAIT = 1000
SCREENSHOT_LOAD_WAIT = 1600
ENABLE_ALERTS = True

ENABLE_SCHEDULED_EMAIL_REPORTS = True

WEBDRIVER_BASEURL = "https://tathya.hotwax.io"
#WEBDRIVER_BASEURL = "http://superset:8088/"
# The base URL for the email report hyperlinks.
WEBDRIVER_BASEURL_USER_FRIENDLY = WEBDRIVER_BASEURL

#-------------------------------------------------------------------------------------------------------------
#ALERT_REPORTS_WORKING_TIME_OUT_KILL = True
#ALERT_REPORTS_WORKING_TIME_OUT_LAG = int(timedelta(seconds=1600).total_seconds())
#ALERT_REPORTS_WORKING_SOFT_TIME_OUT_LAG = int(timedelta(seconds=1600).total_seconds())
#ALERT_REPORTS_QUERY_EXECUTION_MAX_TRIES = 3

# Time selenium will wait for the page to load and render for the email report.
EMAIL_PAGE_RENDER_WAIT = int(timedelta(seconds=1600).total_seconds())
#--------------------------------------------------------------------------------------------------------------
# This Changes Ensure that ALERT_REPORTS scheduled run via selinum user superset

from superset.tasks.types import ExecutorType
THUMBNAIL_SELENIUM_USER = "superset"
THUMBNAIL_EXECUTE_AS = [ExecutorType.SELENIUM]
ALERT_REPORTS_EXECUTE_AS = [ExecutorType.SELENIUM]
#--------------------------------------------------------------------------------------------------------------
SQLLAB_TIMEOUT = int(timedelta(minutes=50).total_seconds())
SUPERSET_WEBSERVER_TIMEOUT = int(timedelta(minutes=50).total_seconds())
SQLLAB_CTAS_NO_LIMIT = True

# When adding a new database we try to connect to it. Depending on which parameters are
# incorrect this could take a couple minutes, until the SQLAlchemy driver pinging the
# database times out. Instead of relying on the driver timeout we can specify a shorter
# one here.
TEST_DATABASE_CONNECTION_TIMEOUT = timedelta(seconds=1600)
#-----------------------------------------------------------------------------------------------------------------

GLOBAL_ASYNC_QUERIES_REDIS_CONFIG = {
    "port": REDIS_PORT,
    "host": REDIS_HOST,
    "password": "",
    "db": 6,
    "ssl": False,
}
GLOBAL_ASYNC_QUERIES_REDIS_STREAM_PREFIX = "async-events-"
GLOBAL_ASYNC_QUERIES_REDIS_STREAM_LIMIT = 1000
GLOBAL_ASYNC_QUERIES_REDIS_STREAM_LIMIT_FIREHOSE = 1000000
GLOBAL_ASYNC_QUERIES_JWT_COOKIE_NAME = "async-token"
GLOBAL_ASYNC_QUERIES_JWT_COOKIE_SECURE = False
GLOBAL_ASYNC_QUERIES_JWT_COOKIE_DOMAIN = None
#GLOBAL_ASYNC_QUERIES_JWT_SECRET = "test-secret-change-me"
GLOBAL_ASYNC_QUERIES_TRANSPORT = "polling"
GLOBAL_ASYNC_QUERIES_POLLING_DELAY = int(
     timedelta(milliseconds=500).total_seconds() * 1000
)
GLOBAL_ASYNC_QUERIES_WEBSOCKET_URL = "ws://127.0.0.1:8080/"

GLOBAL_ASYNC_QUERIES_JWT_SECRET = 'v2jHEh8gG2yw56ReLEvGwGTSgETRu26U'

#---------------------------------------------------------------------------------------------------------
SSL_CERT_PATH = "file:///home//rohit.pawar//certs-mysql-client"
#---------------------------------------------------------------------------------------------------------
#Just Nothing extra meta data provides here
FAB_ADD_SECURITY_VIEWS = True
FAB_ADD_SECURITY_PERMISSION_VIEW = True
FAB_ADD_SECURITY_VIEW_MENU_VIEW = True
FAB_ADD_SECURITY_PERMISSION_VIEWS_VIEW = True

#-------------------------------------------------------------------------------------------------------
def EMAIL_HEADER_MUTATOR(
    msg: MIMEMultipart, **kwargs: Any
) -> MIMEMultipart:
    subject = msg["Subject"].split(":")[0].strip()
    print("Email Subject %s", subject)
    if subject != "Error occurred for Report":
        msg.replace_header("Subject", msg["Subject"].split(":")[0])
    return msg
#---------------------------------------------------------------------------------------------------------
EMAIL_REPORTS_SUBJECT_PREFIX = ""
EMAIL_REPORTS_CTA = "Explore in Hotwax Reports"

# Slack API Token
SLACK_API_TOKEN = "xoxb-5375163807412-5369861877973-QLXJvtbQQ7uXFykDxUgR8NY2"

PREVIOUS_SECRET_KEY = "CHANGE_ME_TO_A_COMPLEX_RANDOM_SECRET"
SECRET_KEY = "4MLdqTj6eX2FUMqlO3haXnez6D776JKxP59RcE2/vFTS4I8ejw/YHTWz"

#----------------------------------------------------------------------------------------------------------
# By using this filter only Admin or who can access all datasource access can view all users
# Similarly, to restrict the roles in the "Roles" dropdown you can provide a custom
# filter callback for the "role" key.

from sqlalchemy.orm.query import Query
from sqlalchemy import and_, or_

def user_filter(query: Query, *args, **kwargs):
    user_model = security_manager.user_model
    if not security_manager.can_access_all_datasources():
        return query.filter(and_(user_model.username.ilike(str(user_model.username))))
    else:
        return query.filter(and_(user_model.username.not_in([])))

EXTRA_RELATED_QUERY_FILTERS = {"user": user_filter}

# ----------------------------------------------------
# EMAIL_REPORTS_BLANK = False
#By default its true because previous users are using this
CSV_INDEX = False

# ------------------------------------------------------
WTF_CSRF_ENABLED = False
SESSION_COOKIE_SAMESITE = None
#SESSION_COOKIE_SECURE = False
#SESSION_COOKIE_HTTPONLY = False
#--------------------------------------------------------------------------------
# default row limit when requesting chart data
# It is not affecting the values on UI
ROW_LIMIT = 100000
# default row limit when requesting samples from datasource in explore view
SAMPLES_ROW_LIMIT = 100000
#---------------------------------------------------------------------------------
# Maximum number of rows returned for any analytical database query 10Lakh
SQL_MAX_ROW = 100000
#---------------------------------------------------------------------------------
# Embedded config options
GUEST_ROLE_NAME = "embedded"
GUEST_TOKEN_JWT_SECRET = "4MLdqTj6eX2FUMqlO3haXnez6D776JKxP59RcE2/vFTS4I8ejw/YHTWz"
GUEST_TOKEN_JWT_ALGO = "HS256"
GUEST_TOKEN_HEADER_NAME = "X-GuestToken"
GUEST_TOKEN_JWT_EXP_SECONDS = 18000  # 5 minutes
# Guest token audience for the embedded superset, either string or callable
# GUEST_TOKEN_JWT_AUDIENCE: Callable[[], str] | str | None = None
#----------------------------------------------------------------------------------
ENABLE_PROXY_FIX = False
PUBLIC_ROLE_LIKE_GAMMA = True

ENABLE_CORS = True
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources':['*'],
    'origins': ['*','http://tathya.hotwax.io','http://tathya.hotwax.io:8088','http://tathya.hotwax.io:3000','http://tathya.hotwax.io:8888','http://tathya.hotwax.io']
}

#-----------------------------------------------------------------
# We are enabling the logs dumping in superset.log, 1day file  rollover and 30 files should be retained
ENABLE_TIME_ROTATE = True
TIME_ROTATE_LOG_LEVEL = "INFO"
FILENAME = os.path.join("/app/superset_home/logs", "superset.log")
ROLLOVER = "midnight"
INTERVAL = 1
BACKUP_COUNT = 20

#--------------------------------------------------------------------------
#Enabling Talisman for CSP
TALISMAN_ENABLED = True
TALISMAN_CONFIG = {
    "force_https": False,
    "content_security_policy": {
        "default-src": ["'self'", "'unsafe-inline'", "'unsafe-eval'"],
        "img-src": ["'self'", "data:"],
        "worker-src": ["'self'", "blob:"],
        "connect-src": ["'self'", "https://api.mapbox.com", "https://events.mapbox.com"],
        "object-src": "'none'",
    }
}

#--------------------------------------------------------------------------


# Optionally import superset_config_docker.py (which will have been included on
# the PYTHONPATH) in order to allow for local settings to be overridden
#
try:
    import superset_config_docker
    from superset_config_docker import *  # noqa

    logger.info(
        f"Loaded your Docker configuration at " f"[{superset_config_docker.__file__}]"
    )
except ImportError:
    logger.info("Using default Docker config...")
