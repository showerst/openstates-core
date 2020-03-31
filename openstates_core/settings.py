import os
import dj_database_url
from .utils import transformers

DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgis://openstates:openstates@localhost/openstates"
)
SECRET_KEY = "non-secret"
INSTALLED_APPS = (
    "django.contrib.contenttypes",
    "openstates_core.data",
    "openstates_core.reports",
)

# scrape settings

SCRAPELIB_RPM = 60
SCRAPELIB_TIMEOUT = 60
SCRAPELIB_RETRY_ATTEMPTS = 3
SCRAPELIB_RETRY_WAIT_SECONDS = 10
SCRAPELIB_VERIFY = True

CACHE_DIR = os.path.join(os.getcwd(), "_cache")
SCRAPED_DATA_DIR = os.path.join(os.getcwd(), "_data")

# import settings

ENABLE_BILLS = True
ENABLE_VOTES = True
ENABLE_PEOPLE_AND_ORGS = False
ENABLE_EVENTS = False

IMPORT_TRANSFORMERS = {"bill": {"identifier": transformers.fix_bill_id}}

# Django settings
DEBUG = False
TEMPLATE_DEBUG = False

MIDDLEWARE_CLASSES = ()
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(levelname)s %(name)s: %(message)s",
            "datefmt": "%H:%M:%S",
        }
    },
    "handlers": {
        "default": {
            "level": "DEBUG",
            "class": "openstates_core.utils.ansistrm.ColorizingStreamHandler",
            "formatter": "standard",
        }
    },
    "loggers": {
        "": {"handlers": ["default"], "level": "DEBUG", "propagate": True},
        "scrapelib": {"handlers": ["default"], "level": "INFO", "propagate": False},
        "requests": {"handlers": ["default"], "level": "WARN", "propagate": False},
        "boto": {"handlers": ["default"], "level": "WARN", "propagate": False},
    },
}

DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}
DATABASES["default"]["ENGINE"] = "django.contrib.gis.db.backends.postgis"
