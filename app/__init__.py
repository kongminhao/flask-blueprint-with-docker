#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17/3/21 下午5:02
from flask import Flask, render_template
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(use_native_unicode="utf8")


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app