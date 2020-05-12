# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 Mojib Wali.
#
# invenio-config-tugraz is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from invenio_config_tugraz import invenioconfigtugraz


def test_version():
    """Test version import."""
    from invenio_config_tugraz import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = invenioconfigtugraz(app)
    assert 'invenio-config-tugraz' in app.extensions

    app = Flask('testapp')
    ext = invenioconfigtugraz()
    assert 'invenio-config-tugraz' not in app.extensions
    ext.init_app(app)
    assert 'invenio-config-tugraz' in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to invenio-config-tugraz' in str(res.data)
