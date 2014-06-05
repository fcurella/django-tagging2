import os
DIRNAME = os.path.dirname(__file__)

DEFAULT_CHARSET = 'utf-8'

test_engine = os.environ.get("TAGGING_TEST_ENGINE", "sqlite3")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.%s' % test_engine,
        'NAME': os.environ.get("TAGGING_DATABASE_NAME", "tagging_test"),
        'USER': os.environ.get("TAGGING_DATABASE_USER", ""),
        'PASSWORD': os.environ.get("TAGGING_DATABASE_PASSWORD", ""),
        'HOST': os.environ.get("TAGGING_DATABASE_HOST", "localhost")
    }
}

if test_engine == "sqlite":
    DATABASES['default']['NAME'] = os.path.join(DIRNAME, ':memory:')
    DATABASES['default']['HOST'] = ""
elif test_engine == "mysql":
    DATABASES['default']['PORT'] = os.environ.get("TAGGING_DATABASE_PORT", 3306)
elif test_engine == "postgresql_psycopg2":
    DATABASES['default']['PORT'] = os.environ.get("TAGGING_DATABASE_PORT", 5432)



INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'tagging',
    'tagging.tests',
)

SECRET_KEY = '1234'
