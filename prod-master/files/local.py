# -*- coding: utf-8 -*-
import os
import random
import string

# Change this to False if you run it in development
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Configuración de la base de datos usando exclusivamente variables de entorno
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.mysql'),
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT']
    }
}

# Read from env or generate random key
SECRET_KEY = os.getenv('SECRET_KEY', ''.join(random.SystemRandom().choice(string.printable) for _ in range(64)))

SITE_ID = 1

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    )

RECAPTCHA_PUBLIC = os.environ['RECAPTCHA_PUBLIC']
RECAPTCHA_PRIVATE = os.environ['RECAPTCHA_PRIVATE']
