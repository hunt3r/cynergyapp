#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    deploy.py
    ~~~~~~~~~

    :author: (c) 2011 - Stephane Wirtel <stephane@wirtel.be>
    :license: BSD
"""
from flask import Flask
from flask import render_template_string

# load the middleware from werkzeug
# This middleware can be applied to add HTTP proxy support to an application
# that was not designed with HTTP proxies in mind.
# It sets `REMOTE_ADDR`, `HTTP_POST` from `X-Forwarded` headers.
from werkzeug.contrib.fixers import ProxyFix

from cynergyapp import app

app.wsgi_app = ProxyFix(app.wsgi_app)
