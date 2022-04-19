# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
dalian-stc-dev@cisco.com
Copyright 2019 Cisco Systems, Inc.
All rights reserved.
"""

from .base import *
import json


CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://localhost:8080',
    'https://localhost:3000',
    'https://localhost:8000',
    'http://127.0.0.1:8000'
]

# INSTALLED_APPS = [
#     'channels',
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     # 3rd party extensions
#     'corsheaders',
#     'django_extensions',
#     'import_export',
#     'djcelery',
#     'axes',
#     'django_filters',
#     # apps
#     'account',
#     'company',
#     'dashboard',
#     'user_interface',
#     'pivot_table',
#     'etisalat',
#     'proxy',
#     'rest_framework',
#     'rest_framework.authtoken',
#     'rest_framework_filters',
# ]


# Telmo request to change the three group to du_bgp_devices
DEVICE_GROUP_EMIX_IPT_ISG_DEVICES = "du_bgp_devices"
DEVICE_GROUP_IPT_DEVICES = "du_bgp_devices"
DEVICE_GROUP = "du_bgp_devices"

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# DU DATABASE SETTINGS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'du_db',
        'USER': 'postgres',
        'PASSWORD': 'postgresRon@ld07',
        'HOST': 'uop-pg',
        'PORT': 5432
        # 'PORT': 6999
    }
}

# DU REDIS SETTINGS
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6380/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "redisDU123!",

        }
    },
    "du": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6380/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "SERIALIZER": "django_redis.serializers.json.JSONSerializer",
            "PASSWORD": "redisDU123!",
        },
    },
    "user": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6380/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SERIALIZER": "django_redis.serializers.json.JSONSerializer",
            "PASSWORD": "redisDU123!",
        },
        "KEY_PREFIX": "etisalat",
    }
}


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": ["redis://:redisDU123!@redis:6380/1"],
        },
    },
    "etisalat": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": ["redis://:redisDU123!@redis:6380/1"],
        },
    },
    "du": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": ["redis://:redisDU123!@redis:6380/1"],
        },
    }
}


# DU NSO SETTINGS
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']
NSO_SERVICE_HOST_FILE_DOWNLOAD = ''
NSO_SERVICE_HOST = 'https://172.20.237.100:8888'
NSO_SERVICE_USER = 'nsoadmin'
NSO_SERVICE_PASSWORD = 'nsoadmin'
CS_SERVICE_HOST_FILE_DOWNLOAD = 'https://172.20.237.100:8888'
CS_NSO_SERVICE_HOST = 'https://172.20.237.100:8888'
CS_NSO_SERVICE_USER = 'nsoadmin'
CS_NSO_SERVICE_PASSWORD = 'nsoadmin'
OLT_SERVICE_HOST_FILE_DOWNLOAD = 'https://172.20.237.100:8888'
OLT_NSO_SERVICE_HOST = 'https://172.20.237.100:8888'
OLT_NSO_SERVICE_USER = 'nsoadmin'
OLT_NSO_SERVICE_PASSWORD = 'nsoadmin'
# BPA
# BPA_SERVICE_HOST = os.environ.get("BPA_SERVICE_HOST", "http://195.229.10.41:30101")
# BPA_SERVICE_HOST = os.environ.get("BPA_SERVICE_HOST", "http://127.0.0.1:3010")
BPA_SERVICE_HOST = os.environ.get("BPA_SERVICE_HOST", "https://172.23.125.30")
BPA_SERVICE_USER = os.environ.get("BPA_SERVICE_USER", "admin")
BPA_SERVICE_PASSWORD = os.environ.get("BPA_SERVICE_PASSWORD", "admin")
BPA_APIKEY = "1bdfa0fa91553359ad716a8aad2637bd"

# ACl
ACL_SERVICE_HOST = "http://10.48.69.114:8080"
ACL_SERVICE_USER = "nsoadmin"
ACL_SERVICE_PASSWORD = "nsoadmin"
# LSP
LSP_SERVICE_HOST = 'http://10.105.217.74:8080'
LSP_SERVICE_USER = 'admin'
LSP_SERVICE_PASSWORD = 'Admin@123'
LSP_SERVICE_NETWORK = 'etisalat-xtc-dare-111'

ARBOR_REPORT_PARSER_HOST = 'http://10.48.190.141:8765'

EXFO_SERVER_URL = 'http://10.48.69.114:443'
EXFO_USER = 'administrator'
EXFO_PWD = 'P@ssw0rdeti'

SITE_URL = 'http://10.48.69.108:81'

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
#     'DEFAULT_FILTER_BACKENDS': (
#         # 'django_filters.rest_framework.DjangoFilterBackend',
#         'rest_framework.filters.OrderingFilter',
#         'rest_framework_filters.backends.DjangoFilterBackend',
#     ),
#     'DEFAULT_PAGINATION_CLASS': 'etisalat.paginator.EtisPaginator',
#     'PAGE_SIZE': 10,
# }

REST_FRAMEWORK = {
"DEFAULT_AUTHENTICATION_CLASSES": (
# "rest_framework.authentication.BasicAuthentication",
# "rest_framework.authentication.SessionAuthentication",
),
"DEFAULT_PERMISSION_CLASSES": (),
"DEFAULT_FILTER_BACKENDS": (
# 'django_filters.rest_framework.DjangoFilterBackend',
"rest_framework.filters.OrderingFilter",
"rest_framework_filters.backends.DjangoFilterBackend",
),
"DEFAULT_PAGINATION_CLASS": "etisalat.paginator.EtisPaginator",
"PAGE_SIZE": 10,
}

DEBUG = True
SPIS_HOST = "http://spis-backend-service/"
STATIC_URL = "/etis_automation_static/"
STATICFILES_DIRS = [
os.path.join(PROJECT_DIR, "static"),
os.path.join(PROJECT_DIR, "static_etis"),
os.path.join(PROJECT_DIR, "kpi", "static"),
os.path.join(PROJECT_DIR, "kpi_plot", "static"),
os.path.join(PROJECT_DIR, "automation", "static"),
]

BPA_KAFKA_CONFIG = {
    "bootstrap_servers": ["172.23.125.30:30700"],
    "auto_offset_reset": "earliest",
    "group_id": "kafka-python-consumer_test",
    "security_protocol": "SASL_SSL",
    "ssl_check_hostname": False,
    "sasl_mechanism": "OAUTHBEARER",
    "api_version": (0, 10),
}
KAFKA_CERT_FILE = os.path.join(PROJECT_DIR, "olt", "license", "kafka-server-cert.pem")

ARBOR_MOCK_FILE_PATH = os.path.join(PROJECT_DIR, "mock", "arbor_mock.json")

with open(ARBOR_MOCK_FILE_PATH, "r") as arbor_json:
    arbor_mock_data = json.load(arbor_json)

ARBOR_MOCK_FILE = arbor_mock_data
