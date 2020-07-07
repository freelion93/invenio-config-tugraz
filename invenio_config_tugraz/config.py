# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Mojib Wali.
#
# invenio-config-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""invenio module that adds tugraz configs."""

from flask_babelex import gettext as _

INVENIO_CONFIG_TUGRAZ_DEFAULT_VALUE = 'foobar'
"""Default value for the application."""

INVENIO_CONFIG_TUGRAZ_BASE_TEMPLATE = 'invenio_config_tugraz/base.html'
"""Default base template for the demo page."""

APP_ALLOWED_HOSTS = ['0.0.0.0',
                     'localhost',
                     '127.0.0.1',
                     'invenio-dev01.tugraz.at',
                     'invenio-test.tugraz.at'
                     ]
"""Allowed Hosts"""

# Invenio-App
# ===========
# See https://invenio-app.readthedocs.io/en/latest/configuration.html

APP_DEFAULT_SECURE_HEADERS = {
    'content_security_policy': {
        'default-src': [
            "'self'",
            'fonts.googleapis.com',
            '*.gstatic.com',
            'data:',
            "'unsafe-inline'",
            "'unsafe-eval'",
            "blob:",
        ],
    },
    'content_security_policy_report_only': False,
    'content_security_policy_report_uri': None,
    'force_file_save': False,
    'force_https': True,
    'force_https_permanent': False,
    'frame_options': 'sameorigin',
    'frame_options_allow_from': None,
    'session_cookie_http_only': True,
    'session_cookie_secure': True,
    'strict_transport_security': True,
    'strict_transport_security_include_subdomains': True,
    'strict_transport_security_max_age': 31556926,  # One year in seconds
    'strict_transport_security_preload': False,
}

# Invenio-Mail
# ===========
# See https://invenio-mail.readthedocs.io/en/latest/configuration.html

MAIL_SERVER = '129.27.11.182'
"""Domain ip where mail server is running."""

SECURITY_EMAIL_SENDER = "info@invenio-test.tugraz.at"
"""Email address used as sender of account registration emails."""
"""Domain name should match the domain used in web server."""

SECURITY_EMAIL_SUBJECT_REGISTER = _("Welcome to RDM!")
"""Email subject for account registration emails."""

MAIL_SUPPRESS_SEND = False
"""Enable email sending by default."""

# CORS - Cross-origin resource sharing
# ===========
# Uncomment to enable the CORS

# CORS_RESOURCES = '*'
# CORS_SEND_WILDCARD = True
# CORS_EXPOSE_HEADERS = [
#    'ETag',
#    'Link',
#    'X-RateLimit-Limit',
#    'X-RateLimit-Remaining',
#    'X-RateLimit-Reset',
#    'Content-Type',
# ]
# REST_ENABLE_CORS = True


# Invenio-saml
# ===========
#

INVENIO_CONFIG_TUGRAZ_SHIBBOLETH = 'True'
"""Set True if SAML is configured"""

USERPROFILES_EXTEND_SECURITY_FORMS = True
"""Set True in order to register user_profile"""

SSO_SAML_IDPS = {}
"""Configuration of IDPS. Actually values can be find in to invenio.cfg file"""

SSO_SAML_DEFAULT_BLUEPRINT_PREFIX = '/shibboleth'
"""Base URL for the extensions endpoint."""

SSO_SAML_DEFAULT_METADATA_ROUTE = '/metadata/<idp>'
"""URL route for the metadata request."""
"""This is also SP entityID https://domain/shibboleth/metadata/<idp>"""

SSO_SAML_DEFAULT_SSO_ROUTE = '/login/<idp>'
"""URL route for the SP login."""

SSO_SAML_DEFAULT_ACS_ROUTE = '/authorized/<idp>'
"""URL route to handle the IdP login request."""

SSO_SAML_DEFAULT_SLO_ROUTE = '/slo/<idp>'
"""URL route for the SP logout."""

SSO_SAML_DEFAULT_SLS_ROUTE = '/sls/<idp>'
"""URL route to handle the IdP logout request."""
