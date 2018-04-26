#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 17/3/21 下午4:47


class Config:
    SECRET_KEY = 'Don not let other guess it'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        return app


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mysql:@localhost/db'
    WTF_CSRF_ENABLED = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
