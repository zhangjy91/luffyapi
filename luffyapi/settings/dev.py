"""
Django settings for luffyapi project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#更改settings为系统环境变量
import sys
print(sys.path)
sys.path.insert(0,BASE_DIR)
sys.path.insert(1,os.path.join(BASE_DIR,'apps'))

#导入文件时飘红，把apps文件夹改成source root即可


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pf27uu6*)4)t%(qz_te(jp_tu#4y(avg=vbs^)=h4g2$gsk6ol'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'corsheaders',

    'xadmin',
    'crispy_forms',
    'reversion',
    'django.conf',

    'home',
    'user',
    'course',

    'django_filters',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    #第三方处理跨域中间件
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #自己编写的处理跨域
    # 'luffyapi.utils.middle.MyMiddle',



]


ROOT_URLCONF = 'luffyapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'luffyapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'luffyapi',
        'USER':'luffapi',
        'PASSWORD':'luffyapi',
        'HOST':'127.0.0.1',
        'OPTIONS':{
                "init_command":"SET foreign_key_checks = 0;",
                }
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

# AUTH_USER_MODEL='user.user'


REST_FRAMEWORK = {
    'EXCEPTION_HANDLER':'luffyapi.utils.exceptions.common_exception_handler',
}



LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {  # 日志格式定义
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(lineno)d %(process)d %(thread)d %(message)s"
        },
        "simple": {
            "format": "%(levelname)s %(module)s %(lineno)d %(message)s"
        },
    },
    "filters": {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "filters": ['require_debug_true'],
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            # "filename": "/var/log/xiangmu/default.log",    # 日志存放路径
            "filename":os.path.join(os.path.dirname(BASE_DIR),"logs","luffyapi.log"),
            "maxBytes": 1024*1024*50,  # 5MB
            "backupCount": 10,
            "formatter": "verbose",
            "encoding":"utf-8"
        },
        # "mail_admins": {
        #     "level": "ERROR",
        #     "class": "django.utils.log.AdminEmailHandler",
        #     "filters": [],
        # },
    },

    #日志对象
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            # "level": "INFO",
            "propagate": True,
        },
#         "django.request": {
#             "handlers": ["console"],
#             "level": "ERROR",
#             "propagate": False,  # 不让特定的logger传播到它的上级
#         },
# """’django’是’django.request’的上级。这种层级关系的设计，使得低层次logger接收到的日志信息，也可以被上级logger收到。
# 实践中，我们可以定义一个顶级的logger，用来接收所有下级logger的日志信息。这种传播可以在每个logger基础上进行控制.
# 如果你不想让特定的logger传播到它的上级，可以关闭这个行为。通过设置'propagate': False,来实现。"""
#         "xiangmu": {
#             "handlers": ["console"],
#             "level": "INFO",
#             "filters": []
#         },
#         "app01": {
#             "handlers": ["console", "default"],
#             "level": "INFO",
#             "filters": [],
#             "propagate": True,
#         },
#         "app02": {
#             "handlers": ["console"],
#             "level": "INFO",
#             "filters": [],
#         },
#         "app03": {
#             "handlers": ["console"],
#             "level": "INFO",
#             "filters": [],
#         }
    }
}

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:*',
    'http://localhost:8080',
]
CORS_ALLOW_METHODS = (
 'DELETE',
 'GET',
 'OPTIONS',
 'PATCH',
 'POST',
 'PUT',
 'VIEW',
)
CORS_ALLOW_HEADERS = (
 'XMLHttpRequest',
 'X_FILENAME',
 'accept-encoding',
 'authorization',
 'content-type',
 'dnt',
 'origin',
 'user-agent',
 'x-csrftoken',
 'x-requested-with',
 'Pragma',
)

# BANNER_COUNTER = 3

from .const import *


# AUTH_USER_MODEL = 'users.User'
AUTH_USER_MODEL = 'user.User'

import datetime

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA':datetime.timedelta(days=7),
    # 'JWT_RESPONSE_PAYLOAD_HANDLER':'user.utils.jwt_response_payload_handler',
}

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES':{
        'sms':'1/m'
    }
}

# redis配置
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "CONNECTION_POOL_KWARGS": {"max_connections": 100}
            # "PASSWORD": "123",
        }
    }
}
